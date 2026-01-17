# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from graph import support_graph

app = FastAPI(title="GenAI Banking Support POC")

class SupportRequest(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/support")
def handle_support(req: SupportRequest):
    # Invoke LangGraph with the user_message
    state = support_graph.invoke({"user_message": req.message})

    # Safely extract keys from the final state
    classification = state.get("classification", "query")
    sentiment = state.get("sentiment", "neutral")
    response_text = state.get("response", "Sorry, I couldn't generate a response.")
    ticket_id = state.get("ticket_id", None)
    ticket_status = state.get("ticket_status", None)

    return {
        "classification": classification,
        "sentiment": sentiment,
        "response": response_text,
        "ticket_id": ticket_id,
        "ticket_status": ticket_status
    }
