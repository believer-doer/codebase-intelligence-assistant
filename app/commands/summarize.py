from app.ingestion.loader import load_repository
from app.summarization.file_summary import (
    generate_file_summaries,
    save_file_summary
)
from app.summarization.repository_summary import (
    generate_repository_summary,
    save_repository_summary
)

def summarize_repository(repo_path):

    documents = load_repository(repo_path)

    print(f"Loaded {len(documents)} documents")

    file_summaries = generate_file_summaries(documents)

    for item in file_summaries:
        save_file_summary(
            item["summary"],
            item["file_path"]
        )

    repo_summary = generate_repository_summary(
        file_summaries
    )

    save_repository_summary(repo_summary)

    print(repo_summary)