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
You are an intelligent travel-planning API.

Return ONLY valid JSON.
No markdown, no extra text, no explanation.

First, understand the user's intent and classify it into exactly one:
- flight
- hotel
- plan trip

Then analyze the user's budget:
- If the budget is too LOW for the destination, reply with intent "plan trip" and set trip_type to "increase_budget".
- If the budget is HIGH, suggest a luxury option and set trip_type to "luxury".
- If the budget is NORMAL, set trip_type to "standard".

Assume:
- Domestic trips usually need at least 8k–15k INR
- International trips usually need at least 40k–60k INR
- Budget > 1 lakh INR = luxury

Message: "{message}"

JSON format:
{{
  "intent": "flight | hotel | plan trip",
  "destination": "",
  "budget": "",
  "trip_type": "increase_budget | standard | luxury"
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


