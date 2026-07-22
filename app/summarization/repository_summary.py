from pathlib import Path
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen2.5:3b"
)

def generate_repository_summary(file_summaries):

    context_sections = []

    for file_summary in file_summaries:

        context_sections.append(
            f"""
            FILE: {file_summary["file_path"]}

            {file_summary["summary"]}
            """
        )

    context = "\n\n".join(context_sections)

    prompt = f"""
        You are analyzing a software repository.

        Using the file summaries below, provide:

        1. Repository purpose
        2. Main technologies
        3. Important modules
        4. Overall architecture
        5. Key capabilities

        Rules:
        - Use ONLY information from the file summaries.
        - Do NOT invent files, modules, functions, classes, or technologies.
        - If information is missing or unclear, explicitly say so.
        - Mention file paths when discussing important modules.
        - Be concise but informative.

        Give your output in the following format:

            Repository Purpose:
            ...

            Main Technologies:
            - ...

            Important Modules:
            - ...

            Architecture:
            ...

            Key Capabilities:
            - ...

        File Summaries:

        {context}
    """

    response = llm.invoke(prompt)

    return response.content


def save_repository_summary(summary):

    Path("data").mkdir(
        exist_ok=True
    )

    Path(
    "data/repository_summary.md"
    ).write_text(
        "# Repository Summary\n\n" + summary
    )