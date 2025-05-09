import numpy as np
from utils.index_utils import (
    load_model, load_index_and_store,
    get_default_corpus, create_faiss_index,
    create_document_store
)

model = load_model()
index, document_store = load_index_and_store()

if index is None or not document_store:
    print("⚠️ No saved index found. Rebuilding in-memory...")
    corpus = get_default_corpus()
    embeddings = model.encode(corpus)
    index = create_faiss_index(embeddings)
    document_store = create_document_store(corpus)

def query_faiss(query: str, k: int = 3):
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, k=k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        doc = document_store.get(idx, {})
        results.append({
            "text": doc.get("text", "[Missing text]"),
            "source": doc.get("source", "unknown"),
            "chunk": int(doc.get("chunk", idx)),
            "similarity_score": float(dist)
        })
    return results
