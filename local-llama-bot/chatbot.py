# import streamlit as st
# from openai import OpenAI
# st.title("My local AI chatbot")
# Client = OpenAI(
#     base_url="http://localhost:11434",
#     api_key="no_needed"
# )
# if "messages" not in st.session_state:
#     st.session_state_messages=[{"role":"assistant", "content": "I am runing locally on your PC! How can I help?"}]
#     for msg in st.session_state.messages:
#         st.chat_messages(msg["role"]).write(msg["content"])
#     if prompt:=st.chat_input("Type your message here...."):
#         st.session_state.messages.append({"role:" "user", "content": prompt})
#         st.chat_message("user").write(prompt)

#         with st.chat_message("assistant"):
#             stream=Client.chat.completions.create(
#                 model="llama3.2",
#                 messages=st.session_state.messages,
#                 stream=True
#             )
#             ai_response=st.write_stream(stream)
#             st.session_state.messages.append({"role": "assistant","content": ai_response})
import streamlit as st
from openai import OpenAI

st.title("My local AI chatbot 🦙")

# 1. Added /v1/ to the URL so Ollama knows how to parse the OpenAI commands.
# Also added the missing comma between the arguments.
client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="not-needed"
)

# 2. Fixed the typo from 'st.session_state_messages' to 'st.session_state.messages'
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "I am running locally on your PC! How can I help?"}]

# 3. UN-INDENTED the rendering loop! 
# This needs to run on every page refresh, not just the very first time.
# Also changed 'st.chat_messages' (plural) to 'st.chat_message' (singular).
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 4. UN-INDENTED the chat input logic so it is always active.
if prompt := st.chat_input("Type your message here...."):
    # Fixed the dictionary typo: changed {"role:" "user"} to {"role": "user"}
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