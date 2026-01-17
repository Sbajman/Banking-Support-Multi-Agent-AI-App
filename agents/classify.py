# agents/classifier.py
from langchain_community.chat_models import ChatOllama
import json
import re
import os

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")

llm = ChatOllama(
    model="llama3.2:3b",
    base_url=OLLAMA_URL,
    temperature=0
)

def extract_json(text: str) -> dict:
    """Safely extract JSON from model output."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError("No valid JSON found in model output")

def classify_agent(state):
    prompt = f"""
                Classify the customer message.

                Allowed classifications:
                - feedback_positive
                - feedback_negative
                - query

                Sentiment:
                - positive
                - neutral
                - negative

                Return ONLY valid JSON using this EXACT schema:
                {{
                "classification": "feedback_positive | feedback_negative | query",
                "sentiment": "positive | neutral | negative",
                "confidence": 0.0
                }}

                Message:
                "{state['user_message']}"
                """

    raw = llm.invoke(prompt).content
    print(raw)
    data = extract_json(raw)

    return {
        "user_message": state["user_message"],
        "classification": data.get("classification", "query"),
        "sentiment": data.get("sentiment", "neutral"),
        "confidence": float(data.get("confidence", 0.5)),
    }
