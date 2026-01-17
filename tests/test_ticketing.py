from agents.ticketing import ticketing_agent

def test_ticket_created_for_negative_feedback():
    state = {
        "classification": "feedback_negative",
        "sentiment": "negative"
    }

    result = ticketing_agent(state)

    assert result["ticket_id"] is not None
    assert result["ticket_status"] == "OPEN"


def test_no_ticket_for_positive_feedback():
    state = {
        "classification": "feedback_positive",
        "sentiment": "positive"
    }

    result = ticketing_agent(state)

    assert result["ticket_id"] is None
