# Agentic RAG Pipeline

An agentic AI application built using **LangGraph**, **LangChain**, **Qdrant**, and **LangSmith**, demonstrating intelligent tool routing between real-time weather data and Retrieval-Augmented Generation (RAG) over documents, with a simple **Streamlit chat UI**.

This project is designed to showcase **clean architecture**, **agentic decision-making**, and **production-ready GenAI engineering practices**.

---

## 🚀 Features

- **Agentic workflow with LangGraph**
  - LLM-based router decides between tools at runtime
- **Real-time Weather Tool**
  - Fetches live weather data using OpenWeatherMap
- **RAG over PDF documents**
  - PDF ingestion, chunking, embedding, and retrieval
  - Vector storage using **Qdrant**
- **Local LLM & Embeddings**
  - Powered by **Ollama (Llama 3 + nomic-embed-text)**
- **LangSmith Tracing & Evaluation**
  - Full visibility into agent decisions and LLM calls
- **Streamlit Chat UI**
  - Interactive interface for demonstrating the agent

---

## 🛠 Tech Stack

- **Python 3.13**
- **LangChain** – LLM orchestration
- **LangGraph** – Agentic workflows
- **Qdrant** – Vector database
- **Ollama** – Local LLM & embeddings
- **LangSmith** – Tracing & evaluation
- **Streamlit** – UI
- **Pytest** – Testing

---

## 📂 Project Structure

agentic-rag-pipeline/
├── app.py # Streamlit UI
├── graph/
│ ├── graph.py # LangGraph wiring
│ ├── router.py # LLM-based router
│ ├── nodes.py # Weather node
│ └── state.py # Shared graph state
├── rag/
│ ├── loader.py # PDF loading & chunking
│ ├── embeddings.py # Qdrant vector store
│ └── retriever.py # Retriever logic
├── tools/
│ └── weather.py # Weather tool
├── llm/
│ └── provider.py # Ollama LLM setup
├── data/
│ └── world_cities.pdf # Sample document for RAG
├── scripts/
│ ├── test_graph.py # Graph sanity check
│ └── test_rag.py # RAG smoke test
├── tests/ # Unit tests
├── README.md
└── .gitignore

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/agentic-rag-pipeline.git
cd agentic-rag-pipeline

### 2️⃣ Create & Activate Virtual Environment

python3.13 -m venv venv
source venv/bin/activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Install & Run Ollama

Install Ollama: https://ollama.com
ollama pull llama3
ollama pull nomic-embed-text

### 5️⃣ Set Environment Variables

#### OpenWeather API
export OPENWEATHER_API_KEY="your_openweather_api_key"

#### Langsmith
export LANGCHAIN_TRACING_V2="true"
export LANGCHAIN_API_KEY="your_langsmith_api_key"
export LANGCHAIN_PROJECT="agentic-rag-pipeline"

### ▶️ Running the Application
streamlit run app.py

📌 Design Decisions

- LLM-based routing instead of keyword matching for robustness

- Dependency injection for LLMs to enable easy provider swaps

- Qdrant vector store with pinned client version for stability

- Local LLMs for reproducibility and zero API cost

- Explicit state management via LangGraph