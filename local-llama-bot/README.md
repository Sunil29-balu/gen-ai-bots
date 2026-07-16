# Local AI Chatbot 🦙

A fully private, offline, ChatGPT-style conversational web application built using Python, Streamlit, and Ollama. This project runs modern large language models (LLMs) entirely on your local machine—meaning no API keys are required, data privacy is guaranteed, and it works completely offline.

## 🚀 Features
* **100% Private & Local:** All text processing happens on your local hardware. No data is sent to external servers.
* **Streaming Responses:** Text wraps out word-by-word in real-time, matching the modern ChatGPT user experience.
* **Persistent Session State:** Remembers the conversation context dynamically during your active browser session.

## 🛠️ Tech Stack
* **Frontend/UI:** [Streamlit](https://streamlit.io/) (Python web framework)
* **Backend Engine:** [Ollama](https://ollama.com/) (Local LLM runner)
* **AI Model:** Meta's `llama3.2` (Lightweight, fast, and optimized for local compute)
* **API Bridge:** `openai` Python SDK (Configured to intercept and route requests locally)

---

## ⚙️ Setup & Installation

Follow these steps to get the application running on your Windows machine:

### 1. Install & Launch Ollama
1. Download and install Ollama from the official site: [ollama.com](https://ollama.com).
2. Open your terminal or Command Prompt and download the Llama 3.2 model:
   ```bash
   ollama run llama3.2

   Clone or download this repository, open the project folder in VS Code, and open the integrated terminal (Ctrl + ~).

Install the required dependencies using pip:pip install streamlit openai
🏃 How to Run the App
Execute the following command in your VS Code terminal to launch the Streamlit web server:python -m streamlit run chatbot.py