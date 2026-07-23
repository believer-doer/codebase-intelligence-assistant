# app/chains/rag_chain.py

from app.retrieval.retriever import retrieve
from langchain_ollama import  ChatOllama

llm = ChatOllama(
        model="qwen2.5:3b"
    )

def build_context(results):

    sections = []

    for doc, metadata in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):

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
    
    results = retrieve(
        question,
        extension=".py",
        show_expanded_query = show_expanded_query
    )

    if not results["documents"][0]:
        return "No relevant documents found."
    
    if show_context:
        print("\n" + "=" * 80)

        for index, document in enumerate(
            results["documents"][0],
            start=1
        ):
            print(
                f"\nRetrieved Chunk {index}\n"
            )

            print(document)

            print("\n" + "-" * 80)

    if show_scores:

        print("\n" + "=" * 80)
        print("Retrieval Scores")

        for index, distance in enumerate(
            results["distances"][0],
            start=1
        ):
            similarity = 1 / (1 + distance)

            print(
                f"Chunk {index} | "
                f"Distance: {distance:.4f} | "
                f"Score: {similarity:.3f}"
            )

    context = build_context(results)

    prompt = build_prompt(
        question,
        context
    )


    response = llm.invoke(prompt)

    sources = {
        meta["file_path"]
        for meta in results["metadatas"][0]
    }
    
    return (
        response.content
        + "\n\nSources:\n"
        + "\n".join(f"- {s}" for s in sources)
    )