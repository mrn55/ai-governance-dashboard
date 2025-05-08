import tempfile
import faiss
import json
import numpy as np
from app.utils.pdf_loader import extract_text_from_pdf
from app.utils.text_splitter import split_text
from app.rag.embedding_loader import model, index, document_store, INDEX_PATH, DOC_STORE_PATH

def process_pdf_upload(filename: str, pdf_bytes: bytes):
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
        tmp.write(pdf_bytes)
        tmp_path = tmp.name

    try:
        text = extract_text_from_pdf(tmp_path)
        chunks = split_text(text)
        embeddings = model.encode(chunks)

        start_id = len(document_store)

        for i, chunk in enumerate(chunks):
            document_store[start_id + i] = {
                "text": chunk,
                "source": filename,
                "chunk": i
            }

        index.add(np.array(embeddings))
        faiss.write_index(index, INDEX_PATH)
        with open(DOC_STORE_PATH, "w") as f:
            json.dump(document_store, f)

        return True, f"Indexed {len(chunks)} chunks from {filename}"
    except Exception as e:
        return False, str(e)