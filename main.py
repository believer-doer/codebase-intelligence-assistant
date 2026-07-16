from app.ingestion.loader import load_repository
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import embed_text
from dotenv import load_dotenv

load_dotenv()

documents = load_repository(".")

print(f"Loaded {len(documents)} documents")

chunks = chunk_documents(documents)

print(f"Created {len(chunks)} chunks")

vector = embed_text(chunks[0].page_content)

print("\nEmbedding Generated")
print(f"Vector Length: {len(vector)}")

print("\nFirst 10 Values:")
print(vector[:10])
