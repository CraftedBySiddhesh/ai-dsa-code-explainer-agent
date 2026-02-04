import os
from groq import Groq

DEFAULT_MODEL = "llama-3.1-70b-versatile"

def get_groq_client() -> Groq:
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise RuntimeError("Missing GROQ_API_KEY in environment/.env")
    return Groq(api_key=key)

def get_model_name() -> str:
    model = (os.getenv("GROQ_MODEL") or DEFAULT_MODEL).strip()
    if "guard" in model.lower():
        return DEFAULT_MODEL
    return model
