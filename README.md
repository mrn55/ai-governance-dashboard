# 🧠 AI Governance Dashboard (RAG + Ethics Tracker)

This project is a demonstration of a Retrieval-Augmented Generation (RAG) system designed to showcase core AI/ML skills aligned with ORNL's mission and tech stack.

It includes:

- ⚙️ FAISS vector search for semantic document retrieval
- 🤖 SentenceTransformers for LLM-friendly embeddings
- 🚀 FastAPI backend with `/ask` endpoint
- 🔐 Designed for future expansion with PDF ingestion, Power Apps frontend, and ethical usage logging

---

## 📐 Architecture

```

User Query
↓
FastAPI Endpoint (/ask)
↓
Embed with SentenceTransformer
↓
Search FAISS Vector Index
↓
Retrieve Top Matching Chunk(s)
↓
Return Response + Metadata

```

---

## 🧪 Quickstart

### ▶️ Run Locally

```bash
# Optional but recommended (I'm using PS)
python -m venv venv

# Activate the venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start API
uvicorn app.api.main:app --reload
```

### 🧠 Example Query

```bash
curl -X POST http://localhost:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"query": "Tell me about CI/CD"}'
```

### 🔍 Sample Response

```json
{
  "answer": "CI/CD pipelines help automate software deployment in production environments.",
  "metadata": {
    "source": "demo-corpus",
    "similarity_score": 0.12
  }
}
```

---

## 📅 Roadmap

### Week 1 (✅ You Are Here)

- [x] Build FastAPI RAG backend with test corpus
- [x] Set up FAISS vector search
- [x] Test query endpoint

### Week 2 (Coming Next)

- [ ] Ingest and chunk PDF documents
- [ ] Expand index dynamically
- [ ] Return top 3 matches + source metadata
