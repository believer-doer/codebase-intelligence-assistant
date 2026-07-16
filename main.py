from app.ingestion.loader import load_repository
from app.ingestion.chunker import chunk_documents


documents = load_repository(".")

print(f"Loaded {len(documents)} documents")

chunks = chunk_documents(documents)

print(f"Created {len(chunks)} chunks")

print("\nFirst Chunk:\n")
print(chunks[0].page_content[:500])

print("\nMetadata:")
print(chunks[0].metadata)

print("\nChunk Statistics")
print("=" * 50)

for i, chunk in enumerate(chunks[:5]):
    print(f"\nChunk {i+1}")
    print(f"Length: {len(chunk.page_content)}")