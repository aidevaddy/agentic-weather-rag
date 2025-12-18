import streamlit as st
from graph.graph import app
from graph.state import GraphState

st.set_page_config(page_title="Agentic RAG Pipeline", layout="centered")

st.title("🦾 Agentic AI Guide")
st.caption("Langgraph-powered agent with Weather + RAG (Qdrant)")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask about weather or world cities....")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    state = GraphState(query=user_input)
    result = app.invoke(state)

    if result.get("answer"):
        response_text = result["answer"]
    elif result.get("context"):
        ctx = result["context"]
        response_text = (
            f"🌦 **Weather in {ctx['city']}**\n\n"
            f"- Temperature: {ctx['temperature']}° {ctx['unit']}\n"
            f"- Condition: {ctx['description']}"
        )
    else:
        response_text = "Sorry, I couldn't find an answer"
    
    st.session_state.messages.append(
        {"role":"assistant", "content":response_text}
    )
    with st.chat_message("assistant"):
        st.markdown(response_text)