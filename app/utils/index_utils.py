import os
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

INDEX_PATH = "faiss.index"
DOC_STORE_PATH = "document_store.json"

def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def get_default_corpus():
    return [
        "Oak Ridge National Laboratory is a multiprogram science and technology national laboratory.",
        "Generative AI can enhance research and operations in government labs.",
        "CI/CD pipelines help automate software deployment in production environments.",
    ]

def create_document_store(corpus):
    return {
        i: {
            "text": text,
            "source": "demo.txt",
            "chunk": i
        }
        for i, text in enumerate(corpus)
    }

def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def save_index(index, store):
    faiss.write_index(index, INDEX_PATH)
    with open(DOC_STORE_PATH, "w") as f:
        json.dump(store, f)

def load_index_and_store():
    if os.path.exists(INDEX_PATH) and os.path.exists(DOC_STORE_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(DOC_STORE_PATH, "r") as f:
            raw_store = json.load(f)
            document_store = {
                int(k): v if isinstance(v, dict) else {
                    "text": v, "source": "unknown", "chunk": -1
                }
                for k, v in raw_store.items()
            }
        return index, document_store
    else:
        return None, None
