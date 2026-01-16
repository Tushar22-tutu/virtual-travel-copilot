import os, requests, re, json
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def clean_json(text):
    text = re.sub(r"```json|```", "", text)
    return text.strip()

def process_message(message: str):
    model = "gemini-2.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"

    prompt = f"""
Extract travel info in JSON.
Message: "{message}"

Return only JSON:
{{
  "intent": "",
  "destination": "",
  "budget": "",
  "trip_type": ""
}}
"""

    body = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(url, json=body)
    data = response.json()

    ai_text = data["candidates"][0]["content"]["parts"][0]["text"]

    # CLEAN
    cleaned = clean_json(ai_text)

    # PARSE to real JSON
    parsed = json.loads(cleaned)

    return parsed
