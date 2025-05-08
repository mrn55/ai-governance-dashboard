from fastapi import FastAPI, Request, UploadFile, File
from app.rag.rag_engine import get_answer
from app.rag.ingestion import process_pdf_upload

app = FastAPI()

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
