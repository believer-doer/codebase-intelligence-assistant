from langchain_text_splitters import RecursiveCharacterTextSplitter
from collections import defaultdict
from pathlib import Path

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )

    chunks = splitter.split_documents(documents)
    file_chunk_counts = defaultdict(int)
    for chunk in chunks:
        file_path = chunk.metadata["file_path"]
        chunk.metadata["file_name"] = Path(file_path).name
        chunk.metadata["chunk_index"] = file_chunk_counts[file_path]
        file_chunk_counts[file_path] += 1

    return chunks