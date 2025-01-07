import logging
import os

from config.graph_config import GraphConfig
from config.llm_config import LLMConfig
from database.neo4j_interface import Neo4jInterface
from transformers.graph_transformer import PDFGraphTransformer

logging.basicConfig(level=logging.INFO)

# Initialize LLM configuration
llm_config = LLMConfig(
    api_base="http://host.docker.internal:1234/v1",
    model_name="mlx-community/mistral-nemo-instruct-2407",
    temperature=0.5,
    max_tokens=4096,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

# Initialize Graph configuration
graph_config = GraphConfig(
    allowed_nodes=[
        "Organisation",
        "Project",
        "Work Package (WP)",
        "Task (T)",
        "Deliverable (D)",
        "Milestone (M)",
        "Due Date (M)",
    ],
    allowed_relationships=[
        "LEAD",
        "CONTRIBUTOR",
        "PRINCIPAL_INVESTIGATOR",
        "COORDINATOR",
        "PARTNER",
        "HAS_PERSON_MONTH",
        "DEPENDS_ON",
        "INCLUDES",
        "IS_PART_OF",
        "HAS_PART",
        "HAS_MILESTONE",
    ],
)
directory_path = "data/"

# Initialize PDFGraphTransformer with the LLM and Graph configurations
pdf_graph_transformer = PDFGraphTransformer(
    llm_config=llm_config, graph_config=graph_config, directory_path=directory_path
)

# Load PDFs from directory and convert to graph
graph_documents_filtered = pdf_graph_transformer.create_graph(num_documents=20)

# Print graph details
pdf_graph_transformer.print_graph_details(graph_documents_filtered)

# # Initialize Neo4j interface
neo4j_interface = Neo4jInterface(
    uri=os.environ.get("NEO4J_URI", ""),
    username=os.environ.get("NEO4J_USERNAME", ""),
    password=os.environ.get("NEO4J_PASSWORD", ""),
)

# # Add graph documents to Neo4j
neo4j_interface.add_graph_documents(graph_documents_filtered)
