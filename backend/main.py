from fastapi import FastAPI
from ai_brain import process_message
from decision_engine import decide_action

app = FastAPI()

@app.post("/copilot")
def copilot(data: dict):
    ai_json = process_message(data["message"])
    result = decide_action(ai_json)
    return result
