# 📄 Personalized Document Summarizer (GenAI + MLOps)

Summarize any PDF based on your **target audience** — like a Student, Executive, or Researcher — using open-source models **fully offline**.

> 🧠 Powered by [Ollama](https://ollama.com), [FAISS](https://github.com/facebookresearch/faiss), and [FastAPI](https://fastapi.tiangolo.com/).

---

## 🚀 Features

✅ Summarize any PDF  
✅ Personalize summary to your audience  
✅ Works **offline** — no OpenAI key needed  
✅ Built for **MLOps** — FastAPI + CI/CD + Docker + Unit Tests  
✅ Bonus: Streamlit UI  

---

## 🧱 Architecture

PDF → Extract → Embed → Vector Store → Prompt → Ollama → Summary


---

## 🛠️ Tech Stack

| Component     | Tool                    |
|---------------|--------------------------|
| Frontend      | Streamlit (optional)     |
| API           | FastAPI                  |
| LLM           | Mistral via Ollama       |
| Embeddings    | MiniLM (SentenceTransformer) |
| Vector Store  | FAISS                    |
| Container     | Docker                   |
| CI/CD         | GitHub Actions           |
| Testing       | PyTest                   |

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/your-username/personalized-doc-summarizer.git
cd personalized-doc-summarizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start Ollama (on host)

```bash
ollama run mistral
```

### 4. Run API

```bash
uvicorn app.main:app --reload
```

### 5. Use it via curl

```bash
curl -X POST "http://localhost:8000/summarize" \
  -F "file=@app/pdf/sample.pdf" \
  -F "persona=Student"
```
