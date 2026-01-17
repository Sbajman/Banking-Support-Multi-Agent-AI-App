import uuid

def ticketing_agent(state):
    classification = state["classification"]
    sentiment = state["sentiment"]

    # POC logic
    if classification in ["feedback_negative", "query"]:
        ticket_id = f"TICKET-{uuid.uuid4().hex[:6]}"
        status = "OPEN"
    else:
        ticket_id = None
        status = "LOGGED_ONLY"

    return {
        **state,
        "ticket_id": ticket_id,
        "ticket_status": status
    }