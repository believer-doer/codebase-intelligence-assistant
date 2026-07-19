from app.vectorstore.chroma_store import ( get_collection)
from app.retrieval.retriever import retrieve


def  ask_question(query):
    collection = get_collection()

    count = collection.count()

    if count == 0:
        print(
            "No index found.\n"
            "Run: python main.py index ."
        )
        return
    
    results = retrieve(query)

    for i, doc in enumerate(
        results["documents"][0]
    ):
        print("\n" + "=" * 80)

        print(
            results["metadatas"][0][i]
        )

        print()

        print(doc[:500])