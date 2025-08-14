import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
USE_GENAI = bool(OPENAI_API_KEY)

try:
    from openai import OpenAI
    client = OpenAI(api_key=OPENAI_API_KEY) if USE_GENAI else None
except ImportError:
    client = None
    USE_GENAI = False

def get_genai_advice(role, skills, missing):
    if not USE_GENAI:
        return [
            f"Focus on learning: {', '.join(missing)}",
            "Build 1 mini-project weekly.",
            "Do mock interviews regularly."
        ]
    
    prompt = f"""
    You are a career coach. The user wants to be a {role}.
    They have skills: {skills}
    They are missing: {missing}
    Give short, actionable advice in bullet points.
    """
    
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip().split("\n")
