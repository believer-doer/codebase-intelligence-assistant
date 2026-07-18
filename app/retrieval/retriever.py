from app.vectorstore.chroma_store import get_collection
from app.embeddings.embedder import embed_text


def retrieve(query:str, k:int =5,  extension: str | None = None):
    collection = get_collection()
    embedding = embed_text(query).tolist()

    query_args = {
        "query_embeddings": [embedding],
        "n_results": k,
    }

    if extension:
        query_args["where"] = {
            "extension": extension
        }

    results = collection.query(**query_args)

    return results