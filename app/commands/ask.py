from app.vectorstore.chroma_store import ( get_collection)
from app.chains.rag_chain import (answer_question)


def  ask_question(query, show_context = False, show_scores = False, show_expanded_query = False):
    collection = get_collection()

    count = collection.count()

    if count == 0:
        print(
            "No index found.\n"
            "Run: python main.py index ."
        )
        return
    
    

    answer = answer_question(query, show_context = show_context, show_scores = show_scores, show_expanded_query = show_expanded_query)
    print(answer)