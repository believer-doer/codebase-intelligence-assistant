# Codebase Intelligence Assistant
Built from scratch as a learning project to understand: 
LangChain, RAG, embeddings, vector databases, retrieval systems, and agent architectures.

An AI-powered assistant that understands software repositories and helps developers explore, analyze, and reason about codebases using Retrieval-Augmented Generation (RAG).

Instead of manually navigating hundreds of files, developers can ask natural language questions such as:

* Where is authentication implemented?
* How does user registration work?
* Which services interact with the database?
* Explain the checkout flow.
* Which files are responsible for payment processing?

The assistant indexes a repository, performs semantic search over the codebase, retrieves relevant context, and uses a local LLM to generate grounded answers.


---

## Motivation

Modern codebases can contain thousands of files spread across multiple services, libraries, and modules.

Finding relevant code often requires:

* Searching through files
* Understanding project structure
* Following call chains
* Reading documentation
* Consulting team members

This project explores how AI systems can help developers understand unfamiliar codebases by combining:

* Semantic search
* Vector databases
* Retrieval-Augmented Generation (RAG)
* Agentic workflows

---

## Current Status

✅ Stage 1 – Complete

Implemented features:

* Repository loading
* File filtering
* LangChain document creation
* Chunking with overlap
* Embeddings generation
* ChromaDB vector storage
* Semantic retrieval
* Metadata filtering
* Local LLM integration (Ollama)
* End-to-end RAG pipeline
* Retrieval debugging mode

---

## Architecture

### Stage 1 – RAG Foundation

```text
Repository
    ↓
File Loader
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
    ↓
Retriever
    ↓
Qwen (Ollama)
    ↓
Answer
```

### Current Retrieval Flow

```text
User Question
       ↓
Query Embedding
       ↓
ChromaDB Search
       ↓
Relevant Chunks
       ↓
Context Builder
       ↓
Prompt Builder
       ↓
Qwen 2.5 (3B)
       ↓
Answer
```

---

## Roadmap

### Stage 2 – Enhanced Retrieval

* Metadata-aware retrieval
* Repository summaries
* Architecture analysis
* Multi-repository support
* Query rewriting
* Retrieval optimization

### Stage 3 – Agentic Capabilities

```text
Question
    ↓
Agent
    ↓
Retrieve Code
    ↓
Analyze Results
    ↓
Search Again (if needed)
    ↓
Generate Answer
```

### Stage 4 – LangGraph Workflows

```text
Question
    ↓
Retrieve
    ↓
Analyze
    ↓
Need More Context?
   ↙          ↘
 Yes          No
  ↓            ↓
Search Again   Answer
```

### Stage 5 – Productionization

* FastAPI backend
* Streamlit UI
* Evaluation framework
* Observability
* Deployment

---

## Technology Stack

### AI Layer

* LangChain
* LangGraph (planned)
* Ollama
* Qwen 2.5 (3B)

### Embeddings Layer

* Sentence Transformers
* all-MiniLM-L6-v2

### Retrieval Layer

* ChromaDB

### Application Layer

* Python
* FastAPI (planned)
* Streamlit (planned)

---

## Project Structure

```text
codebase-intelligence-assistant/

app/
│
├── chains/
├── commands/
├── embeddings/
├── ingestion/
├── retrieval/
├── vectorstore/
│
└── prompts/          (planned)

docs/
├── stage_1.md
└── tasks.md

main.py
requirements.txt
```

---

## Example Usage

Index a repository:

```bash
python main.py index .
```

Ask a question:

```bash
python main.py ask "Where are embeddings generated?"
```

Inspect retrieval results:

```bash
python main.py ask \
"Where are embeddings generated?" \
--show-context
```

---

## Learning Objectives

This project is intentionally being built incrementally to gain a deep understanding of modern AI application architecture.

Topics explored include:

* LangChain fundamentals
* Document ingestion
* Chunking strategies
* Embeddings
* Vector databases
* Semantic search
* Retrieval-Augmented Generation (RAG)
* Agent frameworks
* LangGraph workflows
* AI system design

---

## Development Workflow

The project is managed using:

* GitHub Issues
* GitHub Projects
* Milestones

Each stage is broken down into small engineering tasks and implemented incrementally.

---

## Future Vision

The long-term goal is to build a developer copilot capable of:

* Understanding large repositories
* Performing multi-step code investigations
* Generating architecture explanations
* Assisting onboarding engineers
* Acting as an intelligent codebase knowledge system

---

## License

MIT
