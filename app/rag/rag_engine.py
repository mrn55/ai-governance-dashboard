from app.rag.embedding_loader import query_faiss

def get_answer(query: str):
    results = query_faiss(query, k=3)

    combined_answer = "\n\n---\n\n".join([r["text"] for r in results])
    metadata = {"matches": results}

    return combined_answer, metadata