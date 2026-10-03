from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def generate_chunk(docs:list[Document]) -> list[Document]:
    """
    Generate chunks from the provided documents.

    Args:
        docs (list[Document]): A list of Document objects to be chunked.
        """
    # Initialite recursive character text splitter with specified parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Maximum size of each chunk
        chunk_overlap=200,  # Overlap between chunks
        length_function=len  # Function to determine the length of text        
    )
    splits = text_splitter.split_documents(docs)
    # print("\n\n=======================\n\n")
    # print(f"Generated {len(splits)} chunks from the provided documents.\n")
    # print(f"Preview of the first chunk: {splits[0].page_content[:500]}\n")  # Print first 500 characters of the first chunk
    # print(f"Metadata of the first chunk: {splits[0].metadata}")  # Print metadata of the first chunk
    return splits