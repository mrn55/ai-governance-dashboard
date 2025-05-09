# 🧠 AI Governance Dashboard (RAG + Ethics Tracker)

This project is a demonstration of a Retrieval-Augmented Generation (RAG) system designed to showcase core AI/ML skills aligned with **ORNL’s mission** and Microsoft Azure’s ecosystem.

It includes:

- ⚙️ **FAISS** vector search for semantic retrieval
- 🤖 **SentenceTransformers** for embedding generation
- 🚀 **FastAPI** backend with `/ask`, `/upload`, and `/health` endpoints
- 📄 **PDF ingestion pipeline** with metadata tracking
- 🔐 Designed for future expansion: Power Apps frontend + ethics auditing

---

## 📐 Architecture

```
User Query
   ↓
FastAPI Endpoint (/ask)
   ↓
SentenceTransformer Embedding
   ↓
FAISS Vector Similarity Search
   ↓
Top K Chunk(s) with Metadata
   ↓
JSON Response
```

---

## 🧪 Quickstart

### ▶️ Run Locally

```bash
# Optional but recommended
python -m venv venv
.\venv\Scripts\activate  # On Windows

pip install -r requirements.txt

uvicorn app.api.main:app --reload
```

### 💬 Query Example

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
    "matches": [
      {
        "text": "...",
        "source": "demo.txt",
        "chunk": 2,
        "similarity_score": 0.12
      }
    ]
  }
}
```

---

## ☁️ Infrastructure

📘 For setup instructions, see [Infrastructure Guide](./infra/infrastructure_guide.md)

---

## 📅 Roadmap

### ✅ Milestone 1: RAG Core + Local API

- [x] FastAPI scaffold with `/ask` and test corpus
- [x] FAISS index from sentence embeddings
- [x] Return top K matches via semantic search

### ✅ Milestone 2: PDF Ingestion

- [x] Upload PDF endpoint (`/upload`)
- [x] Chunking + embedding of uploaded content
- [x] FAISS index updated and persisted

### ✅ Milestone 3: CI/CD + Azure Infra

- [x] GitHub Actions workflow: build → push → deploy
- [x] Azure Container Registry + Container Apps
- [x] Secure ACR pull via registry credentials

### 🟡 Milestone 4: RAG Features + Frontend Integration

- [ ] Integrate Power Apps (or Streamlit prototype)
- [ ] Add audit logging for queries / compliance
- [ ] Support multiple PDF sources with tagging
- [ ] Deploy with custom domain / HTTPS cert
