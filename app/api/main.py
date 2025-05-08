from fastapi import FastAPI, Request
from app.rag.rag_engine import get_answer

app = FastAPI()

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    query = data.get("query", "")
    answer, metadata = get_answer(query)
    return {"answer": answer, "metadata": metadata}
