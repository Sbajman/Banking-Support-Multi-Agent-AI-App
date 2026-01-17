from agents.response import response_agent

def test_response_generation():
    state = {
        "user_message": "My card is blocked",
        "classification": "query",
        "sentiment": "neutral"
    }

    result = response_agent(state)

    assert "response" in result
    assert result["response"]
