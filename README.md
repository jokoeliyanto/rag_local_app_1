# 📚 Streamlit RAG Chat App (FAISS + HuggingFace + LM Studio)

A **Retrieval-Augmented Generation (RAG)** application built with
**Streamlit**, allowing you to chat with PDF documents using:

-   **PyPDFLoader** for PDF loading and chunking
-   **HuggingFace Embeddings (bge-base-en-v1.5)**
-   **FAISS Vector Store**
-   **LM Studio (local LLM server)**
-   **LangChain LCEL** for modular RAG pipeline
-   **Excel Export** for saving chat history

This app is ideal for building a fully local knowledge-base chatbot
without paid API services.

------------------------------------------------------------------------

## 🚀 Key Features

### 🔍 Retrieval-Augmented Generation (RAG)

-   User queries retrieve relevant context from PDF chunks.
-   Responses generated using a local model served via LM Studio.

### 💬 Chat History Tracking

All chats are automatically saved with: 
- chat_id
- created_at
- query
- response_text
- run_time (seconds)

### 📥 Export Chat History

-   Chat history can be downloaded as **Excel (.xlsx)**.

### 🧠 Local Embeddings + Local LLM

-   Embeddings powered by HuggingFace BGE models.
-   LLM runs on **http://localhost:1234/v1** via LM Studio.

------------------------------------------------------------------------

## 📦 Installation

### 1️⃣ Clone the repository

``` bash
git clone <repo-url>
cd <folder>
```

### 2️⃣ Create environment (optional but recommended)

``` bash
conda create -n rag_streamlit python=3.10 -y
conda activate rag_streamlit
```

### 3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Ensure LM Studio is running

Steps: 1. Open LM Studio\
2. Load any supported model (e.g., `qwen/qwen3-vl-4b`)\
3. Start the local server:

    Server URL: http://localhost:1234/v1

### ▶️ Run the App

``` bash
streamlit run app.py
```

Access via:

    http://localhost:8501

------------------------------------------------------------------------

## 📁 Directory Structure

``` text
project/
│── app.py
│── data/
│   └── modul_streamlit.pdf
│── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## 🛠 Tech Stack

  Component         Library
  ----------------- -----------------------------------
  PDF Loader        langchain_community (PyPDFLoader)
  Embeddings        HuggingFaceEmbeddings
  Vector Database   FAISS
  LLM               LM Studio (OpenAI-compatible API)
  UI                Streamlit
  Excel Export      pandas + xlsxwriter

------------------------------------------------------------------------

## 📝 Notes

-   LM Studio model must support OpenAI API compatibility.
-   Embeddings can be swapped depending on needs.
-   PDF path can be modified depending on your dataset.

------------------------------------------------------------------------

## 📄 License

MIT License -- free for educational and production use.

------------------------------------------------------------------------

## 🙌 Contributions

Pull requests are welcome!
