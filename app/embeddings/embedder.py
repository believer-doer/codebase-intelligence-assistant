# embedder.py

from sentence_transformers import SentenceTransformer

_embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def get_embedding_model():
    return _embedding_model

def embed_text(text: str):
    model = get_embedding_model()
    return model.encode(text)