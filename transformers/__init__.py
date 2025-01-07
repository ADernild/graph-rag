"""
transformers/__init__.py

This module contains classes for transforming documents into graphs.

Classes:
    - PDFGraphTransformer: Class for transforming PDF documents into graph structures.

Usage:
    from transformers.graph_transformer import PDFGraphTransformer
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

    pdf_graph_transformer = PDFGraphTransformer(llm_config, graph_config)
    documents = pdf_graph_transformer.load_pdf("path/to/your/pdf_file.pdf")
    graph_documents_filtered = pdf_graph_transformer.convert_to_graph(documents)
"""
