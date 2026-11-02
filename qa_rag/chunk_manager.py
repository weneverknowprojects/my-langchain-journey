from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker

embeddings = HuggingFaceEmbeddings(
            model="sentence-transformers/all-mpnet-base-v2"
        )
     

def generate_semantic_chunk(docs: list[Document]) -> list[Document]:
    """
    ## Pre-Retrieval Improvement
    Generate semantic chunk of docs
    separate each (small) sentence -> embed (vectorize) -> compare each embedded sentence, if distance too far then cut as chunk
    RULE:
        - embedding model to semantic chunk should be same  to embed and store to vectorize db
    """
    chunker = SemanticChunker(
        embeddings=embeddings,
        breakpoint_threshold_type='percentile',
        # breakpoint_threshold_amount=70,
    )
    print(f"[GenerateSemanticChunk] before {len(docs)} pages")
    result = chunker.split_documents(docs)
    print(f"[GenerateSemanticChunk] after {len(result)} pages")
        
    return result

def generate_chunk(docs:list[Document]) -> list[Document]:
    """
    Generate chunks from the provided documents.

    Args:
        docs (list[Document]): A list of Document objects to be chunked.
        """
    # Initialite recursive character text splitter with specified parameters
    """
    split based on \n\n(pharagraph), if token lower than chunk_size then keep/cut as chunk
    if more then chunk_size, split using \n(row)
    if split by \n(row) still more than chunk_size then split by space
    if split by space still more than chunk_size then split by character

    """
    
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