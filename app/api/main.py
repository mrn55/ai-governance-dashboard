import os
from fastapi import FastAPI, Request, UploadFile, File
from rag.rag_engine import get_answer
from rag.ingestion import process_pdf_upload

app = FastAPI()

@app.on_event("startup")
def ensure_index_loaded():
    if not os.path.exists("faiss.index") or not os.path.exists("document_store.json"):
        print("Index not found — rebuilding")
        from rag.reset_index import main as reset_main
        reset_main()
    else:
        print("Index and store loaded.")

@app.get("/")
def read_root():
    return {"status":"up"}

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    query = data.get("query", "")
    answer, metadata = get_answer(query)
    return {"answer": answer, "metadata": metadata}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error":"Only PDF files are supported right now."}

    contents = await file.read()
    success, details = process_pdf_upload(file.filename, contents)
    return {"success":success, "details":details}

@app.get("/health")
def health_check():
    return {"status": "healthy"}