from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b"
)


def generate_followup_queries(
    question: str,
    analysis: dict
):
    if analysis["enough_context"]:
        return []

    prompt = f"""
You are helping retrieve source code.

Question:
{question}

Retrieval analysis:
{analysis}

Generate 3 better search queries.

Rules:
- One query per line
- No explanations
- Focus on identifiers, definitions,
  implementations, classes, functions
"""

    response = llm.invoke(prompt)

    return [
        line.strip()
        for line in response.content.splitlines()
        if line.strip()
    ]