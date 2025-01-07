import asyncio
from typing import List

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.documents import Document

from utils.logger import log_error, log_info


class PDFLoader:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    async def load(self) -> List[Document]:
        documents = []
        loader = PyPDFDirectoryLoader(self.directory_path)
        try:
            async for doc in loader.alazy_load():
                documents.append(doc)
        except Exception as e:
            log_error(f"Error loading PDF: {e}")
        return documents

    def load_sync(self) -> List[Document]:
        documents = asyncio.run(self.load())
        log_info(f"Loaded {len(documents)} documents.")
        return documents
