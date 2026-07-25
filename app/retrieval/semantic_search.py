from app.vectorstore.chroma_store import get_collection
from app.embeddings.embedder import embed_text
from langchain_ollama import ChatOllama

llm = ChatOllama(
        model="qwen2.5:3b"
    )


def retrieve(query:str, k:int =5,  extension: str | None = None, show_expanded_query: bool = False):
    collection = get_collection()

    expanded_query = expand_query(query)
    search_query = (
        query
        + " "
        + expanded_query
    )

    if show_expanded_query:
            print(f"Expanded Query: {search_query}")

    embedding = embed_text(search_query).tolist()

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

def expand_query(query):

    prompt = f"""
    You are helping retrieve source code.

    Question:
    {query}

    Return ONLY a comma-separated list of likely
    function names, class names, variable names,
    library names, and technical keywords that may
    appear in source code.

    Do not explain anything.
    Do not mention companies.
    Do not mention products unless they are libraries.

    Output:
    """

    response = llm.invoke(prompt)

    return response.content