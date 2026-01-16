from fastapi import FastAPI
from ai_brain import process_message

app = FastAPI()

@app.post("/ai-brain")
def ai_brain_api(data: dict):
    try:
        user_message = data["message"]
        return process_message(user_message)
    except Exception as e:
        return {"error": str(e)}
