# agents/response.py
from langchain_community.chat_models import ChatOllama
import os

OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")

llm = ChatOllama(
    model="llama3.2:3b",
    base_url=OLLAMA_URL,
    temperature=0.3
)

def response_agent(state):
    message = state.get("user_message", "")
    classification = state.get("classification", "query")
    sentiment = state.get("sentiment", "neutral")

    prompt = f"""
            You are a banking customer support assistant.

            Message: "{message}"

            Classification: {classification}
            Sentiment: {sentiment}

            Guidelines:
            - Be polite and professional
            - If sentiment is negative, be empathetic
            - If it's a query, provide a clear helpful answer
            - Do NOT mention internal systems or AI

            Respond with plain text only.
            """

    response = llm.invoke(prompt).content.strip()

    return {
        **state,               
        "response": response
    }
