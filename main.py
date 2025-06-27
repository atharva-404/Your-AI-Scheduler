from fastapi import FastAPI, Request
from langgraph_workflow import process_message

app = FastAPI()

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_input = data.get("message")
    response = process_message(user_input)
    return {"response": response}
