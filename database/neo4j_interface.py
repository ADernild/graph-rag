import os
from typing import List

from langchain_neo4j import Neo4jGraph
from langchain_neo4j.graphs.graph_document import GraphDocument


class Neo4jInterface:
    def __init__(self, uri: str, username: str, password: str):
        os.environ["NEO4J_URI"] = uri
        os.environ["NEO4J_USERNAME"] = username
        os.environ["NEO4J_PASSWORD"] = password
        self.graph = Neo4jGraph()

    def add_graph_documents(self, documents: List[GraphDocument]):
        self.graph.add_graph_documents(
            documents, include_source=True, baseEntityLabel=True
        )
