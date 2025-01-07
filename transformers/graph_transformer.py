from typing import List, Optional

from langchain_community.graphs.graph_document import GraphDocument
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer
from tqdm_loggable.auto import tqdm

from config.graph_config import GraphConfig
from config.llm_config import LLMConfig
from loaders.pdf_loader import PDFLoader
from utils.logger import log_info


class PDFGraphTransformer:
    def __init__(
        self,
        llm_config: LLMConfig,
        graph_config: GraphConfig,
        directory_path: str = "data/",
    ):
        self.llm_config = llm_config
        self.graph_config = graph_config
        self.directory_path = directory_path
        self.llm_transformer_filtered = LLMGraphTransformer(
            llm=llm_config.llm,
            allowed_nodes=graph_config.allowed_nodes,
            allowed_relationships=graph_config.allowed_relationships,
        )
        self.documents = self.load_pdfs()

    def load_pdfs(self) -> List[Document]:
        loader = PDFLoader(self.directory_path)
        documents = loader.load_sync()
        return documents

    def create_graph(self, num_documents: Optional[int] = None) -> List[GraphDocument]:
        documents_to_process = (
            self.documents[:num_documents] if num_documents else self.documents
        )

        graph_documents_filtered = []
        for document in tqdm(
            documents_to_process,
            desc="Converting documents to graph",
            ncols=100,
            ascii=True,
        ):
            graph_documents_filtered.extend(
                self.llm_transformer_filtered.convert_to_graph_documents([document])
            )

        return graph_documents_filtered

    @staticmethod
    def print_graph_details(graph_documents_filtered):
        log_info(f"Nodes: {graph_documents_filtered[0].nodes}")
        log_info(f"Relationships: {graph_documents_filtered[0].relationships}")
