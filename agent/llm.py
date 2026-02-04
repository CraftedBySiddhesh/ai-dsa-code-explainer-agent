import json
import re

from .groq_client import get_groq_client, get_model_name


def groq_chat(system: str, user: str, *, temperature: float = 0.2, max_tokens: int = 4000) -> str:
    client = get_groq_client()
    resp = client.chat.completions.create(
        model=get_model_name(),
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return (resp.choices[0].message.content or "").strip()


def groq_chat_json(system: str, user: str, *, max_tokens: int = 2000) -> dict:
    system2 = (system or "").strip() + "\n\nReturn ONLY valid JSON. No markdown. No extra text."
    txt = groq_chat(system2, user, temperature=0.0, max_tokens=max_tokens).strip()

    m = re.search(r"\{[\s\S]*\}", txt)
    if not m:
        return {"error": "MODEL_DID_NOT_RETURN_JSON", "raw": (txt[:1200] if txt else "<EMPTY>")}

    js = m.group(0)
    try:
        return json.loads(js)
    except json.JSONDecodeError:
        return {"error": "JSON_PARSE_FAILED", "raw": js[:1200]}
