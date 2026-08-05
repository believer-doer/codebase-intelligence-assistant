from langchain_ollama import  ChatOllama
from app.agent.retrieval_agent import agent_retrieve

llm = ChatOllama(
        model="qwen2.5:3b"
    )

def build_context(results):

    sections = []

    for result in results:

        metadata = result["metadata"]

        sections.append(
            f"""
=== FILE ===
{metadata["file_path"]}

=== CHUNK ===
{metadata["chunk_index"]}

{result["document"]}
"""
        )

    return "\n\n".join(sections)



def build_prompt(question, context):

    return f"""
You are an expert software engineering assistant.

Answer ONLY using the retrieved repository context.

Rules:

- Never invent code.
- If unsure, say so.
- Mention relevant file names.
- Mention function names.
- Explain relationships between files when possible.
- Prefer concrete code over summaries.

Repository Context:

{context}

User Question:

{question}
"""


    
def answer_question(
    question,
    show_context=False,
    show_scores=False,
    show_expanded_query=False,
):


    results = agent_retrieve(
        question,
        extension=".py",
        show_plan=True,
        show_reasoning=True,
        show_expanded_query=True,
    )
    if not results:
        return "No relevant documents found."

    if show_context:

        print("\n" + "=" * 80)

        for i, result in enumerate(results, start=1):

            print(f"\nRetrieved Chunk {i}\n")
            print(result["document"])
            print("\n" + "-" * 80)

    if show_scores:

        print("\n" + "=" * 80)
        print("Retrieval Scores")

        for i, result in enumerate(results, start=1):

            print(
                f"Chunk {i} | "
                f"Source: {result['source']} | "
                f"Score: {result['score']:.3f}"
            )

    context = build_context(results)

    prompt = build_prompt(
        question,
        context,
    )

    response = llm.invoke(prompt)

    sources = sorted({
        result["metadata"]["file_path"]
        for result in results
    })

    return (
        response.content
        + "\n\nSources:\n"
        + "\n".join(f"- {s}" for s in sources)
    )