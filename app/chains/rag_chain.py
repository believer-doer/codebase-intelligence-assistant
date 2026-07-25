# app/chains/rag_chain.py

from app.retrieval.hybrid_retriever import hybrid_retrieve
from langchain_ollama import  ChatOllama

llm = ChatOllama(
        model="qwen2.5:3b"
    )

def build_context(results):

    sections = []

    for result in results:
        doc = result["document"]
        metadata = result["metadata"]

        sections.append(
            f"""
    === FILE: {metadata["file_path"]} ===

    {doc}
    """
        )

    return "\n\n".join(sections)



def build_prompt(
    question: str,
    context: str
):
    return f"""
        You are a codebase assistant.

        Use only the provided context.

        If the answer cannot be found in the context,
        say:

        "I could not find that information in the indexed repository."

        When possible:
        - Mention file names.
        - Mention function names.
        - Be concise.

        Context:
        {context}

        Question:
        {question}
    """

def answer_question(question, show_context: bool = False, show_scores: bool = False, show_expanded_query: bool = False):
    
    results = hybrid_retrieve(
        question,
        extension=".py",
        show_expanded_query = show_expanded_query
    )

    if not results:
        return "No relevant documents found."
    
    if show_context:
        print("\n" + "=" * 80)

        for index, result in enumerate(
            results,
            start=1
        ):
            print(f"\nRetrieved Chunk {index}\n")

            print(result["document"])

            print("\n" + "-" * 80)
                

    if show_scores:

        print("\n" + "=" * 80)
        print("Retrieval Scores")

        for index, result in enumerate(
            results,
            start=1
        ):

            print(
                f"Chunk {index} | "
                f"Source: {result['source']} | "
                f"Score: {result['score']}"
            )
            

    context = build_context(results)

    prompt = build_prompt(
        question,
        context
    )


    response = llm.invoke(prompt)

    sources = {
        result["metadata"]["file_path"]
        for result in results
    }
    
    return (
        response.content
        + "\n\nSources:\n"
        + "\n".join(f"- {s}" for s in sources)
    )