import chromadb

def get_chroma_client():
    client = chromadb.PersistentClient("./chroma_db")
    return client

def get_collection(): 
    client = get_chroma_client()
    collection = client.get_or_create_collection("codebase_chunks")
    return collection

def reset_collection():
    client = get_chroma_client()

    try:
        client.delete_collection(
            "codebase_chunks"
        )
    except:
        pass

    
def index_chunks(chunks, embedding_model):
    collection = get_collection()

    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for chunk in chunks:
        ids.append(f"{chunk.metadata['file_path']}_chunk_{chunk.metadata['chunk_index']}")

        documents.append(chunk.page_content)

        embeddings.append(embedding_model.encode(chunk.page_content).tolist())

        metadatas.append(chunk.metadata)

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Indexed {len(chunks)} chunks")