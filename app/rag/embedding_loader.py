from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

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

def query_faiss(query: str):
    query_vector = model.encode([query])
    distances, indices = index.search(query_vector, k=1)
    top_idx = indices[0][0]
    return document_store[top_idx], float(distances[0][0])
