from app.ingestion.loader import load_repository
from app.ingestion.chunker import chunk_documents
from app.embeddings.embedder import get_embedding_model
from app.vectorstore.chroma_store import (reset_collection, index_chunks)
from app.retrieval.retriever import retrieve
from dotenv import load_dotenv

load_dotenv()

# load repo into Documents
documents = load_repository(".")

print(f"Loaded {len(documents)} documents")

#chunking
chunks = chunk_documents(documents)

print(f"Created {len(chunks)} chunks")


# embeding
embedding_model = get_embedding_model()

reset_collection()

index_chunks(chunks, embedding_model)

# retrieve
queries = ["generate embeddings"]
for query in queries:
    retrieved_results = retrieve(query, 5, ".py")

    for i, doc in enumerate(
        retrieved_results["documents"][0]
    ):

        print("\n" + "=" * 80)

        print(f"Result #{i+1}")

        print(
            retrieved_results["metadatas"][0][i]
        )

        print()

        print(doc[:500])