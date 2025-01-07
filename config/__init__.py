"""
config/__init__.py

This module contains configuration classes for the project.

Classes:
    - LLMConfig: Configuration class for the language model.
    - GraphConfig: Configuration class for the graph structure.

Usage:
    from config.llm_config import LLMConfig
    from config.graph_config import GraphConfig

    llm_config = LLMConfig(
        api_key="your_api_key",
        api_base="your_api_base",
        model_name="your_model_name",
        temperature=0.5,
        max_tokens=4096,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    graph_config = GraphConfig(
        allowed_nodes=["Node1", "Node2"],
        allowed_relationships=["Relationship1", "Relationship2"],
    )
"""
