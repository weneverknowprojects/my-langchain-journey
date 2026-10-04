from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import numpy as np
from langchain_community.vectorstores import FAISS

def embed_using_faiss(docs:list[Document]):
    """
    Embed the provided documents using FAISS embeddings.

    Args:
        docs (list): A list of Document objects to be embedded.
    """
    try:
        # Initialize FAISS embeddings
        embeddings = HuggingFaceEmbeddings(
            model="sentence-transformers/all-mpnet-base-v2"
        )
        
        # initialize FAISS db
        db = FAISS.from_documents(docs, embeddings)

        print(f"Generated embeddings for {len(docs)} documents using FAISS.")
        # db.save_local("faiss_index")

        # try give question
        result = db.similarity_search("What the component of architecture of AI Agents?", k=3)
        print(f"Similarity search results: {result[0].page_content[:500]}")  # Print first 500 characters of the first result
        print(f"Metadata of the first result: {result[0].metadata}")  # Print metadata of the first result
    except Exception as e:
        print(f"Error embedding documents: {e}")
        

def embed_documents(docs:list[Document]) -> list[np.float32]|None:
    """
    Embed the provided documents using HuggingFace embeddings.

    Args:
        docs (list): A list of Document objects to be embedded.
    """
    try:
        # Initialize HuggingFace embeddings
            embeddings = HuggingFaceEmbeddings(
                # model="sentence-transformers/all-MiniLM-L6-v2"
                model="sentence-transformers/all-mpnet-base-v2"
            )
        
            # Generate embeddings for the documents
            embedded_docs = embeddings.embed_documents([doc.page_content for doc in docs])
        
            #conver to float32
            v_result = np.array(embedded_docs, dtype=np.float32)
            print(f"Converted embeddings to float32. shape {v_result.shape} type {v_result.dtype}")
            print(f"Generated embeddings for {len(embedded_docs)} documents. type {type(embedded_docs)}")
            return v_result
    except Exception as e:
        print(f"Error embedding documents: {e}")
        return None