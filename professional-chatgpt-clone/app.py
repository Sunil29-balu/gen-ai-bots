import streamlit as st
from openai import OpenAI
import requests

st.set_page_config(page_title="AI Workspace", page_icon="⚡", layout="wide")
client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="not-needed"
)

@st.cache_data(ttl=60)
def get_installed_models():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            models = [model["name"] for model in response.json().get("models", [])]
            return models if models else ["llama3.2"]
    except requests.exceptions.RequestException:  # 2. Fixed missing colon here
        pass
    return ["llama3.2"]


available_models = get_installed_models()


with st.sidebar:
    st.title("⚙️ Control Panel")
    st.caption("Configure your local model parameters in real-time.")
    st.markdown("---")
    selected_model = st.selectbox("🤖 Choose LLM Model", available_models)
    temperature = st.slider("🌡️ Temperature (Creativity)", min_value=0.0, max_value=1.5, value=0.7, step=0.1)
    system_prompt = st.text_area("🧠 System Instructions / Persona", value="You are a helpful AI assistant.")
    
    st.markdown("---")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()


st.title("⚡ Professional ChatGPT Workspace")
st.subheader(f"Active Engine: `{selected_model}`", divider="rainbow")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


for message in st.session_state.chat_history:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


if prompt := st.chat_input("Send a message..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    api_messages = [{"role": "system", "content": system_prompt}]
    for msg in st.session_state.chat_history:
        api_messages.append(msg)


    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=selected_model,
                messages=api_messages,
                temperature=temperature,
                stream=True
            )
            ai_response = st.write_stream(stream)
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        except Exception as e:
            st.error(f"Execution Error: Could not connect to Ollama. Details: {e}")