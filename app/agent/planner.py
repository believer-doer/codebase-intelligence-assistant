# app/agent/planner.py

import json

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b"
)


def create_retrieval_plan(question: str) -> dict:
    prompt = f"""
You are an expert software engineer.

The user asked:

{question}

Before searching the repository,
decide what information should be retrieved.

Return ONLY valid JSON.

Example:

{{
    "goal": "Locate embed_text implementation",
    "searches": [
        "embed_text definition",
        "def embed_text",
        "embed_text implementation"
    ]
}}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except Exception:
        return {
            "goal": question,
            "searches": [question],
        }