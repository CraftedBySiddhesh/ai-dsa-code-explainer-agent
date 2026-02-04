import json
from .llm import groq_chat, groq_chat_json
from . import prompts
from .md_parser import pick_title

class NotebookAgent:
    def __init__(self, repair_rounds: int = 2):
        self.repair_rounds = repair_rounds

    def run_one(self, problem_md: str):
        problem = groq_chat_json(
            prompts.EXTRACT_SYSTEM,
            prompts.EXTRACT_USER.format(md=problem_md[:140000]),
            max_tokens=2200
        )

        if "error" in problem:
            title = pick_title(problem_md) or "Problem"
            md = (
                "### ERROR\n\n"
                f"{problem['error']}\n\n"
                "Raw model output (truncated):\n\n"
                f"```\n{problem.get('raw','')}\n```\n"
            )
            return title, md, {"problem_json": problem, "planner_json": {}}

        problem.setdefault("title", "")
        problem.setdefault("statement", "")
        problem.setdefault("constraints", [])
        problem.setdefault("examples", [])

        plan = groq_chat_json(
            prompts.PLAN_SYSTEM,
            prompts.PLAN_USER.format(problem_json=json.dumps(problem, ensure_ascii=False)),
            max_tokens=1200
        )
        if "error" in plan:
            plan = {"strategy_name":"", "key_observation":"", "pitfalls":[plan["error"]]}

        md = groq_chat(
            prompts.SOLVE_SYSTEM,
            prompts.SOLVE_USER.format(
                problem_json=json.dumps(problem, ensure_ascii=False),
                planner_json=json.dumps(plan, ensure_ascii=False),
            ),
            temperature=0.2,
            max_tokens=3800
        )

        for _ in range(self.repair_rounds):
            v = groq_chat_json(
                prompts.VALIDATE_SYSTEM,
                prompts.VALIDATE_USER.format(md=md[:180000]),
                max_tokens=800
            )
            if v.get("error"):
                break
            if v.get("ok"):
                break
            issues_list = v.get("issues", []) or []
            issues = "\n- " + "\n- ".join(issues_list) if issues_list else "\n- (no issues provided)"
            md = groq_chat(
                prompts.REPAIR_SYSTEM,
                prompts.REPAIR_USER.format(
                    problem_json=json.dumps(problem, ensure_ascii=False),
                    issues=issues,
                    md=md[:180000]
                ),
                temperature=0.2,
                max_tokens=3800
            )

        title = problem.get("title") or pick_title(problem_md) or "Problem"
        return title, md, {"problem_json": problem, "planner_json": plan}
