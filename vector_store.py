from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(chunks):

    texts = [chunk["text"] for chunk in chunks]

    metadatas = [
    {
        "page": chunk["page"],
        "source": chunk["source"]
    }
    for chunk in chunks
]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(
        texts,
        embeddings,
        metadatas=metadatas
    )

    return vector_store


def search_vector_store(vector_store, question):

    results = vector_store.similarity_search(
        question,
        k=3
    )

    return results