from langchain_ollama import ChatOllama
from pathlib import Path

llm = ChatOllama(
        model="qwen2.5:3b"
    )
 
def summarize_file(document):
    prompt = prompt = f"""
        You are analyzing a source code file.

        Rules:
        - Use ONLY information present in the file.
        - Do NOT invent functions, classes, modules, or behaviors.
        - If something is not present, say "Not found".
        - Mention only functions/classes that actually appear in the code.
        - Be concise.

        File path:
        {document.metadata["file_path"]}

        File content:
        {document.page_content}

        Output format:

        Purpose:
        ...

        Functions/Classes:
        - ...
        - ...

        Responsibilities:
        - ...
        - ...
    """

    response = llm.invoke(prompt)
    return response.content

def generate_file_summaries(documents):
    summaries = []

    for doc in documents:
        print(
            f"Summarizing: {doc.metadata['file_path']}"
        )
        summary = summarize_file(doc)

        summaries.append({
            "file_path": doc.metadata["file_path"],
            "file_name": doc.metadata["file_name"],
            "summary": summary
        })

    return summaries

def save_file_summary(summary, file_path):

    summary_path = (
        Path("data/file_summaries")
        / Path(file_path)
    )

    summary_path = summary_path.with_suffix(".md")

    summary_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    content = f"""# {file_path}

    {summary}
    """

    summary_path.write_text(content)