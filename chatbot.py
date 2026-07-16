import streamlit as st
from openai import OpenAI

st.title("My local AI chatbot 🦙")
client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="not-needed"
)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "I am running locally on your PC! How can I help?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Type your message here...."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="llama3.2",
            messages=st.session_state.messages,
            stream=True
        )
        ai_response = st.write_stream(stream)
        
    st.session_state.messages.append({"role": "assistant", "content": ai_response})