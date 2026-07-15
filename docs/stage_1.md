# Stage 1 - Codebase Intelligence Assistant (CLI RAG)

## Objective

Build a command-line application that can understand a software repository and answer questions about it using Retrieval-Augmented Generation (RAG).

The goal of Stage 1 is to learn and implement the foundations of modern AI applications:

* Document ingestion
* Chunking
* Embeddings
* Vector databases
* Retrieval
* RAG pipelines
* Prompt engineering

At the end of this stage, the application should be able to answer questions about a codebase such as:

* Where is authentication implemented?
* How does user registration work?
* Which files interact with the database?
* Explain the checkout flow.
* What services are responsible for payment processing?

---

# High-Level Architecture

```text
Repository
    ↓
File Loader
    ↓
Code Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Retriever
    ↓
OpenAI LLM
    ↓
Answer
```

---

# Learning Goals

## LangChain Concepts

* Document Loaders
* Text Splitters
* Embeddings
* Vector Stores
* Retrievers
* Prompt Templates
* RAG Pipelines

## AI Concepts

* Semantic Search
* Embedding Similarity
* Context Injection
* Hallucination Reduction
* Retrieval-Augmented Generation

---

# Scope

## Included

### Repository Indexing

The system should:

* Scan a local repository
* Read supported source files
* Convert files into LangChain Documents
* Store metadata

Example metadata:

```json
{
  "file_path": "auth/token_service.py",
  "language": "python"
}
```

---

### Chunking

Large files should be split into smaller chunks.

Example:

```text
auth/token_service.py
        ↓
Chunk 1
Chunk 2
Chunk 3
...
```

Recommended starting values:

```python
chunk_size = 1000
chunk_overlap = 200
```

These values can be tuned later.

---

### Embeddings

Generate embeddings for each chunk using OpenAI embeddings.

Example:

```text
Code Chunk
      ↓
Embedding Model
      ↓
Vector
```

---

### ChromaDB Storage

Store:

* Chunk content
* Embeddings
* Metadata

ChromaDB acts as the searchable memory of the system.

---

### Retrieval

Given a question:

```text
Where is JWT authentication implemented?
```

The retriever should:

1. Convert question into embedding
2. Search ChromaDB
3. Return relevant code chunks

---

### RAG Answer Generation

The retrieved chunks should be passed to the LLM.

Example:

```text
Question
      +
Retrieved Code
      ↓
OpenAI
      ↓
Answer
```

The model should answer only using retrieved context.

---

### CLI Interface

Example usage:

```bash
python main.py index ./sample-repo
```

Indexes the repository.

Example:

```bash
python main.py ask "Where is authentication implemented?"
```

Returns an answer.

---

# Out of Scope (Stage 1)

The following features will be implemented in later stages:

* Streamlit UI
* FastAPI backend
* Agents
* Tool calling
* LangGraph workflows
* Multi-repository support
* GitHub integration
* Architecture diagrams
* Code dependency analysis
* Evaluation pipelines
* Observability and tracing

---

# Supported File Types

Initial support:

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

Additional file types can be added later.

---

# Recommended Project Structure

```text
codebase-intelligence-assistant/

app/
│
├── ingestion/
│   ├── loader.py
│   ├── parser.py
│   └── chunker.py
│
├── embeddings/
│   └── embedding_service.py
│
├── vectorstore/
│   └── chroma_store.py
│
├── rag/
│   ├── retriever.py
│   └── qa_chain.py
│
├── cli/
│   └── commands.py
│
├── config.py
│
└── main.py

data/
│
├── repositories/
│
└── chroma/

requirements.txt

README.md

STAGE_1.md
```

---

# Acceptance Criteria

Stage 1 is complete when:

## Repository Indexing Works

```bash
python main.py index ./sample-repo
```

successfully:

* Loads files
* Chunks files
* Creates embeddings
* Stores vectors in ChromaDB

---

## Question Answering Works

```bash
python main.py ask "Where is authentication implemented?"
```

returns:

* Relevant answer
* References to source files

Example:

```text
Authentication appears to be implemented in:

1. auth/middleware.py
2. auth/token_service.py

The middleware validates JWT tokens and forwards
authenticated users to downstream services.
```

---

## Retrieval Quality Is Reasonable

Questions about:

* Authentication
* Database access
* Services
* Controllers

should retrieve relevant chunks from the repository.

---

# Stretch Goals

If time permits:

## Show Source Files

Display file paths used in the answer.

Example:

```text
Sources:

auth/middleware.py
auth/token_service.py
```

---

## Show Retrieved Chunks

Useful for debugging retrieval quality.

Example:

```bash
python main.py ask \
"Where is authentication implemented?" \
--show-context
```

---

## Configurable Retrieval

Allow:

```bash
--top-k 5
```

to control the number of retrieved chunks.

---

# Success Definition

By the end of Stage 1, you should understand:

* How RAG systems work
* How embeddings are generated
* How vector databases perform semantic search
* How LangChain connects retrieval and generation
* Why retrieval quality directly impacts answer quality

Most importantly, you should have a working AI system that can answer questions about an arbitrary codebase using semantic search and LLM reasoning.
