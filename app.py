import streamlit as st
import requests

# -----------------------------
# Page Setup
# -----------------------------
st.set_page_config(page_title="Banking Support AI", layout="wide")
st.title("Banking Support AI Agent POC")

# Dark theme styling
st.markdown(
    """
    <style>
    body {
        background-color: #000000;
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        background-color: #333333;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
    
if "customer_input" not in st.session_state:
    st.session_state.customer_input = ""

# -----------------------------
# Input Form
# -----------------------------

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Type your message here",
        key="customer_input"
    )
    submit_button = st.form_submit_button("Send")
# -----------------------------
# API Call
# -----------------------------
if submit_button and user_input.strip():
    st.session_state.messages.append({
        "role": "customer",
        "content": user_input
    })

    try:
        response = requests.post(
            "http://api:8000/support", 
            json={"message": user_input},
            timeout=20
        )
        data = response.json()

        assistant_message = data.get("response", "No response generated.")
        ticket_id = data.get("ticket_id")
        ticket_status = data.get("ticket_status")
        sentiment = data.get("sentiment")
        classification = data.get("classification")

        agent_text = f"{assistant_message}\n\n"
        #agent_text += f"**Classification:** {classification}\n"
        #agent_text += f"**Sentiment:** {sentiment}\n"
        if ticket_id:
            agent_text += f"**Ticket ID:** {ticket_id} ({ticket_status})"

        st.session_state.messages.append({
            "role": "agent",
            "content": agent_text
        })

    except requests.exceptions.RequestException as e:
        st.session_state.messages.append({
            "role": "agent",
            "content": f"API error: {e}"
        })

# -----------------------------
# Chat Display
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] == "customer":
        st.markdown(
            f"""
            <div style="
                background-color:#111111;
                color:#ffffff;
                padding:12px;
                border-radius:10px;
                margin:8px 0;
                text-align:right;
            ">
                <strong>Customer:</strong><br/>
                {msg['content']}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style="
                background-color:#222222;
                color:#ffffff;
                padding:12px;
                border-radius:10px;
                margin:8px 0;
                text-align:left;
            ">
                <strong>Agent:</strong><br/>
                {msg['content']}
            </div>
            """,
            unsafe_allow_html=True
        )
