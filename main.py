# from app.config import OPENAI_API_KEY
from app.ingestion.loader import load_repository


documents = load_repository("./")
print(f"Loaded {len(documents)} documents")

print(documents[0])