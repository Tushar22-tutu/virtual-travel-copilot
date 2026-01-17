import os
import requests
import json
import re
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"

URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={GEMINI_API_KEY}"

def clean_json(text):
    text = re.sub(r"```json|```", "", text)
    return text.strip()

def process_message(message: str):
    prompt = f"""
You are an API. Return ONLY valid JSON.
No markdown, no explanation.

Allowed intents (pick exactly one):
- flight
- hotel
- plan trip

Message: "{message}"

JSON format:
{{
  "intent": "flight | hotel | plan trip",
  "destination": "",
  "budget": "",
  "trip_type": ""
}}
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(URL, json=payload, timeout=20)
        data = response.json()
    except Exception as e:
        print("Request error:", e)
        return fallback()

    if "candidates" not in data:
        print("Gemini error:", data)
        return fallback()

    try:
        raw_text = data["candidates"][0]["content"]["parts"][0]["text"]
        cleaned = clean_json(raw_text)
        parsed = json.loads(cleaned)
        return parsed
    except Exception as e:
        print("Parse error:", e)
        print("Raw:", raw_text)
        return fallback()


def fallback():
    return {
        "intent": "plan trip",
        "destination": "",
        "budget": "",
        "trip_type": ""
    }


