from app.vectorstore.chroma_store import get_collection
from app.embeddings.embedder import embed_text


def retrieve(query:str, k:int =5):
    collection = get_collection()
    embedding = embed_text(query).tolist()

    results = collection.query(
        query_embeddings = [embedding],
        n_results = k,
    )

    return results