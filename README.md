# 📚 Streamlit RAG Chat App (FAISS + HuggingFace + LM Studio)

Aplikasi **RAG (Retrieval-Augmented Generation)** berbasis **Streamlit** yang memungkinkan Anda melakukan chat dengan dokumen PDF menggunakan:

- **PyPDFLoader** → untuk load & chunking dokumen PDF  
- **HuggingFace Embeddings (bge-base-en-v1.5)**  
- **FAISS Vector Store**  
- **LM Studio (local LLM server)** → sebagai model bahasa  
- **LangChain LCEL** → untuk pipeline RAG modular  
- **Excel Export** → menyimpan riwayat percakapan  

Aplikasi ini sangat cocok untuk membuat chatbot knowledge base lokal sepenuhnya tanpa API berbayar.

---

## 🚀 Fitur Utama

### 🔍 Retrieval-Augmented Generation (RAG)
- Query user akan diambil konteks relevan dari dokumen PDF.
- Kemudian dijawab menggunakan model LLM dari LM Studio.

### 📁 Chat History Tracking
- Semua chat otomatis dicatat ke DataFrame.
- Tracking:
  - chat_id
  - created_at
  - query
  - response_text
  - run_time (detik)

### 📥 Export Chat History
- Riwayat chat dapat **di-download dalam format Excel (.xlsx)**.

### 🧠 Local Embeddings + Local LLM
- Embeddings menggunakan HuggingFace BGE.
- LLM berjalan di **http://localhost:1234/v1** (LM Studio).

---

## 📦 Instalasi

### 1️⃣ Clone repository
```bash
git clone <repo-url>
cd <folder>
```

### 2️⃣ Buat environment (opsional tapi direkomendasikan)
```bash
conda create -n rag_streamlit python=3.10 -y
conda activate rag_streamlit
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Pastikan LM Studio sudah berjalan

* Open LM Studio
* Load model, misalnya: qwen/qwen3-vl-4b (atau model lain)
* Start server:
```bash
Server URL: http://localhost:1234/v1
```

### ▶️ Menjalankan Aplikasi
```bash
streamlit run app.py
```

Aplikasi akan tampil pada
```bash
http://localhost:8501
```

### 📁 Struktur Direktori
```kotlin
project/
│── app.py
│── data/
│   └── modul_streamlit.pdf
│── requirements.txt
└── README.md
```

### 🛠 Teknologi yang Digunakan

| Komponen        | Library                           |
| --------------- | --------------------------------- |
| PDF Loader      | langchain_community (PyPDFLoader) |
| Embeddings      | HuggingFaceEmbeddings             |
| Vector Database | FAISS                             |
| LLM             | OpenAI-compatible API (LM Studio) |
| UI              | Streamlit                         |
| Export Excel    | pandas + xlsxwriter               |

### 📝 Catatan Penting
* Model LM Studio wajib mendukung OpenAI API format.
* Embedding model dapat diganti sesuai kebutuhan.
* PDF bisa diganti dengan dokumen lain tinggal ubah path.

### 📄 Lisensi

MIT License – bebas digunakan untuk edukasi & produksi.

### 🙌 Kontribusi

Pull request dipersilakan!