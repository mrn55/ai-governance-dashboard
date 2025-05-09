import tempfile
import faiss
import json
import numpy as np
from utils.pdf_loader import extract_text_from_pdf
from utils.text_splitter import split_text
from utils.index_utils import INDEX_PATH, DOC_STORE_PATH, load_model
from rag.embedding_loader import index, document_store

model = load_model()

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