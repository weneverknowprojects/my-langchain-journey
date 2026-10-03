from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from chunk_manager import generate_chunk

def load_document(path) -> list[Document]:
    """
    Load a document from the specified path.

    Args:
        path (str): The file path to the document.
        """
    # initialize the PyPdfLoader with the given path
    loader = PyPDFLoader(path)

    #load pdf content into a document object [Document] (list of Document objects)
    document = loader.load()
    print(f"Loaded document from {path} with {len(document)} pages.")
    print(f"Document content preview: {document[0].page_content[:500]}")  # Print first 500 characters of the first page
    print(f"Document metadata: {document[0].metadata}")  # Print metadata of the first page
    return document
