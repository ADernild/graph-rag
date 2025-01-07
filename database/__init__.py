"""
database/__init__.py

This module contains classes for interfacing with the Neo4j database.

Classes:
    - Neo4jInterface: Class for interacting with the Neo4j database.

Usage:
    from database.neo4j_interface import Neo4jInterface

    neo4j_interface = Neo4jInterface(
        uri="bolt://localhost:7687",
        username="neo4j",
        password="password"
    )

    neo4j_interface.add_graph_documents(documents)
"""
