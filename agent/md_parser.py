import re


def split_problems(md: str) -> list[str]:
    md = md.replace("\r\n", "\n")

    parts = re.split(r"(?m)^##\s+", md)
    if len(parts) > 2:
        out = []
        for p in parts[1:]:
            chunk = "## " + p.strip()
            if chunk.strip():
                out.append(chunk)
        return out

    hr_parts = re.split(r"(?m)^---\s*$", md)
    return [p.strip() for p in hr_parts if p.strip()]


def ensure_single_problem(md: str) -> str:
    md2 = md.strip()
    if not md2:
        return ""
    # if user didn't provide any separators, wrap as one problem
    if (re.search(r"(?m)^##\s+", md2) is None) and (re.search(r"(?m)^---\s*$", md2) is None):
        return "## Problem\n\n" + md2
    return md2


def pick_title(problem_md: str) -> str:
    lines = [line.strip() for line in problem_md.split("\n") if line.strip()]
    if not lines:
        return ""
    if lines[0].startswith("##"):
        return lines[0].lstrip("#").strip()
    return lines[0][:80]
