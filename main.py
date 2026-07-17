from app.ingestion.loader import load_repository
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import get_embedding_model
from app.vectorstore.chroma_store import (reset_collection, index_chunks)
from dotenv import load_dotenv

load_dotenv()

documents = load_repository(".")

print(f"Loaded {len(documents)} documents")

chunks = chunk_documents(documents)

print(f"Created {len(chunks)} chunks")


embedding_model = get_embedding_model()

reset_collection()

index_chunks(chunks, embedding_model)

for chunk in chunks[:10]:
    print(chunk.metadata)