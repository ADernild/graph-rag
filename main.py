import json
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
        ("Project", "INCLUDES", "Work Package (WP)"),
        ("Organisation", "PRINCIPAL_INVESTIGATOR", "Project"),
        ("Organisation", "COORDINATOR", "Project"),
        ("Organisation", "PARTNER", "Project"),
        ("Organisation", "LEAD", "Work Package (WP)"),
        ("Organisation", "CONTRIBUTOR", "Work Package (WP)"),
        ("Organisation", "HAS_PERSON_MONTH", "Work Package (WP)"),
        ("Organisation", "LEAD", "Task (T)"),
        ("Organisation", "CONTRIBUTOR", "Task (T)"),
        ("Work Package (WP)", "HAS_MILESTONE", "Milestone (M)"),
        ("Work Package (WP)", "HAS_DUE_DATE", "Due Date (M)"),
        ("Milestone (M)", "HAS_DUE_DATE", "Due Date (M)"),
        ("Task (T)", "IS_PART_OF", "Work Package (WP)"),
        ("Task (T)", "INCLUDES", "Deliverable (D)"),
        ("Task (T)", "HAS_MILESTONE", "Milestone (M)"),
        ("Task (T)", "HAS_DUE_DATE", "Due Date (M)"),
        ("Deliverable (D)", "HAS_MILESTONE", "Milestone (M)"),
        ("Deliverable (D)", "HAS_DUE_DATE", "Due Date (M)"),
        ("Deliverable (D)", "DEPENDS_ON", "Task (T)"),
    ],
)

directory_path = "data/"

# Initialize PDFGraphTransformer with the LLM and Graph configurations
pdf_graph_transformer = PDFGraphTransformer(
    llm_config=llm_config, graph_config=graph_config, directory_path=directory_path
)

# Load PDFs from directory and convert to graph
graph_documents_filtered = pdf_graph_transformer.create_graph(num_documents=30)

with open("data.json", "w") as f:
    json.dump(graph_documents_filtered, f)
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
