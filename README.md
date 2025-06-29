# Agentic AI Blog Generator

An autonomous AI system that generates SEO-optimized blog posts by researching topics in real-time using Google search data. This project leverages CrewAI to orchestrate intelligent agents that perform sequential research and writing tasks powered by the Gemini 1.5 Flash language model.

---

## Features

- **Multi-agent Architecture:** Separate researcher and writer agents coordinate seamlessly to produce comprehensive blog content.
- **Real-time Web Search:** Integrates Serper API for dynamic Google search queries to ensure up-to-date and relevant information.
- **Markdown Output:** Automatically generates well-structured, Markdown-formatted blog posts ready for publishing.
- **Streamlit Interface:** A clean and interactive front-end built with Streamlit lets users input topics and download generated blogs instantly.
- **Secure Configuration:** Uses `dotenv` for environment variable management to handle API keys securely.

---

## Tech Stack

- Python
- [CrewAI](https://github.com/subhamkumarpadhy/Agentic_AI_News_Reporter_Gemini) — for agent orchestration
- Gemini 1.5 Flash LLM — for natural language understanding and generation
- Serper API — for Google search integration
- Streamlit — for building the user interface
- dotenv — for managing environment variables

---

## Setup Instructions

1. **Clone the repository:**

   git clone https://github.com/subhamkumarpadhy/Agentic_AI_News_Reporter_Gemini


2. Create a virtual environment:
   python -m venv .venv

3. Activate the virtual environment:
    .venv\Scripts\activate


4. Install dependencies:
    pip install -r requirements.txt

5. Create a .env file and add your API keys:
    GEMINI_API_KEY=your_gemini_api_key_here
    SERPER_API_KEY=your_serper_api_key_here

6. Run the Streamlit app:
    streamlit run app.py
