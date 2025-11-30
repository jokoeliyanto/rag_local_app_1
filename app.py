import streamlit as st
import pandas as pd
from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
import io
import uuid
import time

# Load And Chunking Document
file_path = "data/modul_streamlit.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()

# Embeddings
emb = HuggingFaceEmbeddings(
    model_name="BAAI/bge-base-en-v1.5",   # atau BGE, Qwen, dll
    model_kwargs={"device": "cpu"},           # "cuda" kalau ada GPU
    encode_kwargs={"normalize_embeddings": True}
)

# Vector Store & Retriever
vector_store = FAISS.from_documents(documents = docs, embedding = emb)
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# LLM
llm = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model_name="qwen/qwen3-vl-4b"   # isi model LM Studio
)


# RAG Chain
# Custom QA prompt
prompt = PromptTemplate.from_template("""
Jawab dengan jawaban profesional.
Gunakan konteks berikut untuk menjawab pertanyaan:

Konteks:
{context}

Pertanyaan:
{question}

Jawaban:
""")

# LCEL pipeline
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough(),
    }
    | prompt
    | llm
)



st.set_page_config(page_title="Chat with RAG", layout="wide")

# --- Init Session State ---

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of (query, response)

if "chat_df" not in st.session_state:
    st.session_state.chat_df = pd.DataFrame(columns=[
        "chat_id", "created_at", "query", "response_text", "run_time"
    ])

tab_chat, tab_history = st.tabs(["💬 Chat", "📊 Chat History"])

# --- Chat Tab ---
with tab_chat:
    st.subheader("Chat with RAG")

    history_container = st.container(height=600)
    with history_container:
        for q, a in st.session_state.chat_history:
            with st.chat_message("user"):
                st.markdown(q)
            with st.chat_message("assistant"):
                st.markdown(a)

    query = st.chat_input("Type your message...")

    if query:
        with history_container:
            with st.chat_message("user"):
                st.markdown(query)
            ai_placeholder = st.chat_message("assistant")
            with ai_placeholder:
                msg_placeholder = st.empty()
                msg_placeholder.markdown("RAG systems is preparing response...")

        with st.spinner("Processing request..."):
            start = time.time()
            response_text= rag_chain.invoke(query)
            end = time.time()
            elapsed = end-start
        msg_placeholder.empty()

        if response_text == None:
            response_text = f"🚨 **Error:** Response is{response_text}"
            st.session_state.chat_history.append((query, response_text))
            with history_container:
                with ai_placeholder:
                    msg_placeholder.error(response_text)
        else:

            st.session_state.chat_history.append((query, response_text))

            chat_id = str(uuid.uuid4())
            created_at = pd.Timestamp.now()
            new_row = {
                "chat_id": chat_id,
                "created_at": created_at,
                "query": query,
                "response_text": response_text,
                "run_time": elapsed,
            }
            st.session_state.chat_df = pd.concat(
                [st.session_state.chat_df, pd.DataFrame([new_row])],
                ignore_index=True
            )

            with history_container:
                with ai_placeholder:
                    msg_placeholder.markdown(response_text)


# --- History Tab ---
with tab_history:
    st.subheader("Chat History DataFrame")

    st.dataframe(
        st.session_state.chat_df,
        use_container_width=True,
        height=700
    )

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        st.session_state.chat_df.to_excel(writer, sheet_name="ChatHistory", index=False)
    excel_data = output.getvalue()

    timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{file_path}_{timestamp}.xlsx"

    st.download_button(
        label="📥 Download Chat History (Excel)",
        data=excel_data,
        file_name=file_name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
