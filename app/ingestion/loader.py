from pathlib import Path
from langchain_core.documents import Document

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".java",
    ".go",
    ".rs",
    ".md",
}

IGNORED_DIRECTORIES = {
    ".git",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
}


def load_repository(repo_path):
    repo_path = Path(repo_path)

    print(f"Loading repository from: {repo_path}")

    documents = []
    for file_path in repo_path.rglob("*"):

        if any(
            part in IGNORED_DIRECTORIES
            for part in file_path.parts
        ):
            continue

        if (
            file_path.is_file()
            and file_path.suffix in SUPPORTED_EXTENSIONS
        ):
            try:
                content = file_path.read_text(encoding="utf-8")
            except Exception:
                continue

            if not content.strip():
                continue
            
            document = Document(
                page_content = content,
                metadata = {
                    "file_path" : str(file_path),
                    "extension": file_path.suffix
                }
            )

            documents.append(document)
    return documents