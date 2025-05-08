import os
import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

INDEX_PATH = "faiss.index"
DOC_STORE_PATH = "document_store.json"

# Sample corpus and model
corpus = [
    "Oak Ridge National Laboratory is a multiprogram science and technology national laboratory.",
    "Generative AI can enhance research and operations in government labs.",
    "CI/CD pipelines help automate software deployment in production environments.",
]

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(corpus)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 = Euclidean distance
index.add(embeddings)

document_store = {i: doc for i, doc in enumerate(corpus)}

def query_faiss(query: str, k: int = 3):
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, k=k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        doc = document_store.get(idx, {})
        results.append({
            "text": doc.get("text", "[Missing text]"),
            "source": doc.get("source", "unknown"),
            "chunk": doc.get("chunk", idx),
            "similarity_score": float(dist)
        })
    return results

if os.path.exists(INDEX_PATH) and os.path.exists(DOC_STORE_PATH):
    print("Loading saved FAISS index and document store")
    index = faiss.read_index(INDEX_PATH)
    with open(DOC_STORE_PATH, "r") as f:
        document_store = {
            int(k): (v if isinstance(v, dict) else {"text": v, "source": "unknown", "chunk": -1})
            for k, v in document_store.items()
        }

else:
    print("no saved index found. starting fresh memory")
    dimension = 384
    index = faiss.IndexFlatL2(dimension)
    document_store = {}