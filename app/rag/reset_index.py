from utils.index_utils import (
    load_model, get_default_corpus,
    create_document_store, create_faiss_index,
    save_index
)

def main():
    model = load_model()
    corpus = get_default_corpus()
    embeddings = model.encode(corpus)

    index = create_faiss_index(embeddings)
    document_store = create_document_store(corpus)

    save_index(index, document_store)
    print("✅ FAISS index and document store rebuilt.")

if __name__ == "__main__":
    main()
