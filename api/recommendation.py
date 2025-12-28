import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=api_key)

MODEL = "gemini-2.5-flash-lite"  # ✅ confirmed working in your test


def generate_recommendations(
    signal: str,
    domain: str,
    impact: int,
    stakeholders: str,
) -> str:
    prompt = f"""
You are a neutral public policy advisor AI.

Policy Signal: {signal}
Policy Domain: {domain}
Impact Severity (1–10): {impact}
Affected Stakeholders: {stakeholders}

Task:
- Provide 3–5 concise, actionable policy recommendations
- Focus on mitigation and response
- Avoid political bias
- Use a professional advisory tone
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text.strip()
