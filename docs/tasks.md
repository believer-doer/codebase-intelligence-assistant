# Stage 1 Tasks - Codebase Intelligence Assistant

## Goal

Build a CLI-based RAG system that can understand a code repository and answer questions about it.

---

# Progress Tracker

| Task                 | Status |
| -------------------- | ------ |
| Project Setup        | ⬜      |
| Repository Loader    | ⬜      |
| Chunking             | ⬜      |
| Embeddings           | ⬜      |
| ChromaDB Integration | ⬜      |
| Retriever            | ⬜      |
| RAG Pipeline         | ⬜      |
| CLI Commands         | ⬜      |
| Source Attribution   | ⬜      |
| Testing & Cleanup    | ⬜      |

---

# Task 1: Project Setup

## Objective

Create the project structure and install dependencies.

## Learn

* Virtual environments
* LangChain packages
* ChromaDB

## Deliverables

Create:

```text
codebase-intelligence-assistant/

app/
data/

main.py
requirements.txt
.env
```

Install:

```bash
langchain
langchain-openai
langchain-community
chromadb
python-dotenv
typer
```

## Acceptance Criteria

```bash
python main.py
```

runs successfully.

---

# Task 2: Repository Loader

## Objective

Load source files from a repository.

## Learn

* LangChain Documents
* Metadata

## Deliverables

Implement:

```python
load_repository(repo_path)
```

Output:

```python
[
    Document(
        page_content="...",
        metadata={
            "file_path": "...",
            "extension": ".py"
        }
    )
]
```

Supported:

```text
.py
.js
.ts
.tsx
.jsx
.java
.go
.rs
.md
```

Ignore:

```text
node_modules
dist
build
.git
```

## Acceptance Criteria

```bash
python main.py load ./sample-repo
```

prints:

```text
Loaded 127 documents
```

---

# Task 3: Chunking

## Objective

Split files into manageable chunks.

## Learn

* Text splitters
* Chunk overlap
* Context preservation

## Deliverables

Implement:

```python
chunk_documents(documents)
```

Start with:

```python
chunk_size=1000
chunk_overlap=200
```

Each chunk must preserve:

```python
metadata
```

## Acceptance Criteria

Print:

```text
Loaded: 100 files
Generated: 850 chunks
```

---

# Task 4: Embeddings

## Objective

Convert chunks into vectors.

## Learn

* Embeddings
* Semantic similarity

## Deliverables

Create:

```python
create_embeddings()
```

Use:

```python
OpenAIEmbeddings
```

Read API key from:

```text
.env
```

## Acceptance Criteria

Successfully generate embeddings for sample chunks.

---

# Task 5: ChromaDB Integration

## Objective

Store embeddings.

## Learn

* Vector databases
* Persistence

## Deliverables

Implement:

```python
create_vector_store()
```

Store:

* chunk content
* embeddings
* metadata

Persist data locally.

Directory:

```text
data/chroma/
```

## Acceptance Criteria

Restarting application should preserve vectors.

---

# Task 6: Build Repository Indexing Command

## Objective

Create first useful workflow.

## Deliverables

Command:

```bash
python main.py index ./sample-repo
```

Workflow:

```text
Load Files
 ↓
Chunk
 ↓
Embed
 ↓
Store
```

## Acceptance Criteria

Repository indexed successfully.

Output:

```text
Repository indexed.

Files: 143
Chunks: 912
Stored: 912
```

---

# Task 7: Build Retriever

## Objective

Retrieve relevant code chunks.

## Learn

* Similarity search
* Top-K retrieval

## Deliverables

Implement:

```python
retrieve(query)
```

Example:

```python
retrieve(
    "Where is authentication implemented?"
)
```

Returns:

```python
top_chunks
```

## Acceptance Criteria

Can print retrieved chunks.

---

# Task 8: Build RAG Pipeline

## Objective

Generate answers from retrieved context.

## Learn

* Prompt templates
* Retrieval-Augmented Generation

## Deliverables

Prompt:

```text
You are a senior software engineer.

Use ONLY the provided context.

If the answer is not found,
say you do not know.

Context:
{context}

Question:
{question}
```

Pipeline:

```text
Question
 ↓
Retrieve
 ↓
Inject Context
 ↓
LLM
 ↓
Answer
```

## Acceptance Criteria

Question:

```text
Where is authentication implemented?
```

returns meaningful answer.

---

# Task 9: Create Ask Command

## Objective

Expose RAG via CLI.

## Deliverables

Command:

```bash
python main.py ask \
"Where is authentication implemented?"
```

Output:

```text
Authentication is implemented in:

- auth/middleware.py
- auth/token_service.py

JWT validation occurs in middleware.
```

## Acceptance Criteria

End-to-end question answering works.

---

# Task 10: Source Attribution

## Objective

Show evidence used by the model.

## Learn

* Explainability
* RAG debugging

## Deliverables

Output:

```text
Answer:
...

Sources:

auth/middleware.py
auth/token_service.py
```

Use metadata from retrieved chunks.

## Acceptance Criteria

Every answer displays source files.

---

# Task 11: Add Debug Mode

## Objective

Inspect retrieval quality.

## Deliverables

Flag:

```bash
--show-context
```

Example:

```bash
python main.py ask \
"Where is authentication implemented?" \
--show-context
```

Displays:

```text
Retrieved Chunk 1
Retrieved Chunk 2
Retrieved Chunk 3
```

## Acceptance Criteria

Can visually inspect retrieval results.

---

# Task 12: Refactor

## Objective

Clean architecture before Stage 2.

## Deliverables

Separate:

```text
ingestion/
embeddings/
vectorstore/
rag/
cli/
```

Remove duplicate code.

Add:

```python
config.py
```

for shared settings.

## Acceptance Criteria

Project structure matches architecture plan.

---

# Stage 1 Completion Checklist

Before moving to Stage 2:

* [ ] Repository indexing works
* [ ] ChromaDB persists data
* [ ] Retrieval returns relevant chunks
* [ ] RAG answers questions correctly
* [ ] Sources are displayed
* [ ] CLI commands work
* [ ] Code is organized into modules
* [ ] README updated

---

# Stage 2 Preview

After completing Stage 1 we will add:

* Better code-aware chunking
* Metadata filtering
* Multiple repositories
* Repository summaries
* Architecture analysis
* LangChain tools
* Agent-based retrieval

This is where the project starts evolving from a basic RAG system into a true Codebase Intelligence Assistant.
