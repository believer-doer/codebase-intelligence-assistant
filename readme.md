# Codebase Intelligence Assistant

An AI-powered assistant that understands software repositories and helps developers explore, analyze, and reason about codebases using Retrieval-Augmented Generation (RAG).

Instead of manually navigating hundreds of files, developers can ask natural language questions such as:

* Where is authentication implemented?
* How does user registration work?
* Which services interact with the database?
* Explain the checkout flow.
* Which files are responsible for payment processing?

The assistant indexes a repository, performs semantic search over the codebase, retrieves relevant context, and uses an LLM to generate grounded answers.

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

🚧 Stage 1 – In Progress

Current functionality:

* Repository loading
* File filtering
* LangChain Document creation

Upcoming:

* Chunking
* Embeddings
* ChromaDB integration
* Retrieval
* RAG question answering

---

## Architecture Roadmap

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
OpenAI
    ↓
Answer
```

### Stage 2 – Enhanced Retrieval

* Metadata-aware retrieval
* Repository summaries
* Architecture analysis
* Multi-repository support

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

* OpenAI
* LangChain
* LangGraph

### Retrieval Layer

* ChromaDB
* OpenAI Embeddings

### Application Layer

* Python
* FastAPI
* Streamlit

---

## Project Structure

```text
codebase-intelligence-assistant/

app/
│
├── ingestion/
├── embeddings/
├── vectorstore/
├── rag/
├── cli/
│
├── config.py
│
└── main.py

data/

docs/
├── STAGE_1.md
└── TASKS.md
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
