from app.rag.embedding_loader import query_faiss

def get_answer(query: str):
    answer, distance = query_faiss(query)
    metadata = {"source": "demo-corpus", "similarity_score": distance}
    return answer, metadata