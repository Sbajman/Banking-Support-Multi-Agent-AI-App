
## Banking Support AI Agent
** A POC Banking Support Multi-agent GenAI system tailored for banking customer support workflows **  

The objective is to design and implement a multi-agent AI assistant that handles:

This model aims to:

* Classification of incoming user messages into feedback (positive or negative) or queries
* Personalized responses based on classification and user sentiment
* Ticket tracking and updates through integration with a support database


Key Components :
1. Ollama LLM Server: Local LLM inference engine for AI processing
2. LangGraph Agents: Modular AI agents for classification, response generation, and workflow orchestration
3. FastAPI Backend: Handles requests, orchestrates agents, and interacts with LLM.
4. Streamlit UI: User-friendly chat interface for customers and agents.

##  Architecture Diagram

```mermaid
flowchart LR
    Customer[Customer] --> UI[Streamlit UI]
    UI --> API[FastAPI Backend]
    API --> Graph[LangGraph]

    subgraph Agents["LangGraph Multi-Agent Workflow"]
        Classifier["Classification Agent"]
        Responder["Response Agent"]
        Ticketing["Ticketing Agent"]

        Classifier --> Responder
        Responder --> Ticketing
    end

    Graph --> LLM[Ollama Local LLM]
    Ticketing --> DB[(Ticket Store)]
```


## Sequence Diagram

```mermaid
sequenceDiagram
    participant Customer
    participant API as FastAPI
    participant Graph as LangGraph
    participant C as Classifier Agent
    participant R as Response Agent
    participant T as Ticketing Agent

    Customer->>API: Message
    API->>Graph: user_message
    Graph->>C: classify
    C-->>Graph: classification, sentiment
    Graph->>R: generate response
    R-->>Graph: response
    Graph->>T: ticket decision
    T-->>Graph: ticket_id, status
    Graph-->>API: final state
    API-->>Customer: response
```

## TECH STACK
Python 3.11

Streamlit – Interactive chat UI
FastAPI – Backend API framework
Ollama – Local LLM server
Docker & Docker Compose – Containerization and orchestration
LangGraph / LangChain Community – AI agent orchestration

## Setup & Installation

```
Clone the repository:
git clone https://github.com/yourusername/banking-support-ai.git
cd banking-support-ai
```

Runnning the app locally
1. ollama serve (Start Ollama Server)
2. Ollama pull llama3.2:3b
3. export OLLAMA_BASE_URL=http://localhost:11434
Also make sure the streamlit request us sent to http://localhost:8000/support)
4. uvicorn main:app --host 0.0.0.0 --port 8000
5. streamlit run app.py


# Use Docker to run the app
Build and start services using Docker Compose:
```docker compose up --build```


This will start:

FastAPI backend at http://localhost:8000
Streamlit UI at http://localhost:8501
Ollama LLM server at port 11434

## Usage

Open Streamlit UI in your browser:

http://localhost:8501


Type a banking support query in the customer chatbox.
The AI agent classifies the message and generates a response.
Responses from Agents appear in the chat window under Agent:
Customer messages appear under Customer:

![alt text](image-1.png)

![alt text](image.png)



## Testing
Unit tests for agents are included:

```
pytest tests/ -vvvv
```

The Tests included:
1. Classify state propagation: Assert on the sentiment of user message
2. Test Response generation
3. Test ticket generation for negative feedback. No ticket should be generated for positive feedback.
