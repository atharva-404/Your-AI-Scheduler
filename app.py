import streamlit as st
import requests

st.title("Your AI Scheduler")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("You: ", "")

if user_input:
    st.session_state.chat.append(("user", user_input))
    response = requests.post("http://localhost:8000/chat", json={"message": user_input})
    ai_response = response.json()["response"]
    st.session_state.chat.append(("agent", ai_response))

for role, message in st.session_state.chat:
    st.markdown(f"**{role.capitalize()}**: {message}")
