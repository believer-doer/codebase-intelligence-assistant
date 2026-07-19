from app.vectorstore.chroma_store import ( get_collection)
from app.chains.rag_chain import (answer_question)


def  ask_question(query):
    collection = get_collection()

    count = collection.count()

    if count == 0:
        print(
            "No index found.\n"
            "Run: python main.py index ."
        )
        return
    
    

    answer = answer_question(query)
    print(answer)