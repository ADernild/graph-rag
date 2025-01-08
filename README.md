# Graph RAG Initializer

## Overview
This project provides a structured approach to loading PDF documents, transforming them into a graph using a language model, and storing the graph in a Neo4j database.

## Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/ADernild/graph-rag
   cd graph-rag
   ```
2. Run docker-compose:
   ```sh
   docker-compose up -d
   ```

## Usage
1. Run the main.py file to load PDF documents, transform them into a graph using a language model, and store the graph in a Neo4j database

## File Structure
```
.
├── config
│   ├── __init__.py
│   ├── graph_config.py
│   └── llm_config.py
├── database
│   ├── __init__.py
│   └── neo4j_interface.py
├── loaders
│   ├── __init__.py
│   └── pdf_loader.py
├── main.py
├── README.md
├── requirements.txt
└── transformers
    ├── __init__.py
    └── graph_transformer.py
```
