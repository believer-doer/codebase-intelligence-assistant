from app.retrieval.semantic_search import retrieve
from app.retrieval.keyword_search import bm25_search


def hybrid_retrieve(
    query: str,
    k: int = 5,
    extension: str | None = None,
    show_expanded_query: bool = False
):

    keyword_results = bm25_search(
        query,
        k
    )

    semantic_results = retrieve(
        query,
        k,
        extension,
        show_expanded_query
    )

    merged = []
    seen = set()

    # BM25 first
    for result in keyword_results:

        meta = result["metadata"]

        chunk_id = (
            meta["file_path"],
            meta["chunk_index"]
        )

        if chunk_id in seen:
            continue

        seen.add(chunk_id)

        merged.append(result)

    # Semantic second
    for doc, meta in zip(
        semantic_results["documents"][0],
        semantic_results["metadatas"][0]
    ):

        chunk_id = (
            meta["file_path"],
            meta["chunk_index"]
        )

        if chunk_id in seen:
            continue

        seen.add(chunk_id)

        merged.append(
            {
                "document": doc,
                "metadata": meta,
                "score": None,
                "source": "semantic"
            }
        )

    return merged[:k]