import re

from rank_bm25 import BM25Okapi


bm25 = None
documents = []
metadatas = []


def tokenize_code(text: str):
    return re.findall(
        r"[A-Za-z_][A-Za-z0-9_]*",
        text.lower()
    )


def build_bm25_index(chunks):

    global bm25
    global documents
    global metadatas

    documents = [
        chunk.page_content
        for chunk in chunks
    ]

    metadatas = [
        chunk.metadata
        for chunk in chunks
    ]

    tokenized_docs = [
        tokenize_code(doc)
        for doc in documents
    ]

    bm25 = BM25Okapi(tokenized_docs)


def bm25_search(query: str, k: int = 5):

    if bm25 is None:
        return []

    query_tokens = tokenize_code(query)

    scores = bm25.get_scores(
        query_tokens
    )

    ranked = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )

    results = []

    for index, score in ranked:

        if score <= 0:
            continue

        results.append(
            {
                "document": documents[index],
                "metadata": metadatas[index],
                "score": float(score),
                "source": "bm25"
            }
        )

        if len(results) >= k:
            break

    return results