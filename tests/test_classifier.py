from agents.classify import classify_agent

def test_classifier_state_propagation(mocker):
    mock_llm = mocker.patch("agents.classify.ChatOllama")

    mock_llm.return_value.invoke.return_value.content = (
        '{"classification": "complaint", "sentiment": "negative"}'
    )
    
    state = {"user_message": "I am unhappy with the service"}
    result = classify_agent(state)

    assert "classification" in result
    assert "sentiment" in result
    assert result["sentiment"] == "negative"
    assert result["user_message"] == state["user_message"]
