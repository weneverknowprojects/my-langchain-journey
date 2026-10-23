from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import numpy as np
from langchain_community.vectorstores import FAISS
from langchain_chroma import Chroma
import uuid

 # Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(
            model="sentence-transformers/all-mpnet-base-v2"
        )
# Initialize chroma and save into disk (default save to memory)
my_chroma = Chroma(
    collection_name='qna',
    embedding_function=embeddings,
    persist_directory='./qna_vector_db'
)
def load_chroma_db() -> Chroma:
    return my_chroma

def embed_using_chroma(docs: list[Document]):
    """
    embed and store to chromadb
    """
    # embed and save vector    
    my_chroma.add_documents(documents=docs, ids=[str(uuid.uuid4()) if doc.id==None else doc.id for doc in docs])

def load_db_faiss() -> FAISS|None:
    """
    Load the FAISS database from the local file system.

    Returns:
        FAISS: The loaded FAISS database object.
    """
    try:
        db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        print("FAISS database loaded successfully.")
        return db
    except Exception as e:
        print(f"Error loading FAISS database: {e}")
        return None

async def embed_using_faiss(docs:list[Document]):
    """
    Embed the provided documents using FAISS embeddings.

    Args:
        docs (list): A list of Document objects to be embedded.
    """
    try:
       
        
        # initialize FAISS db
        db = FAISS.from_documents(docs, embeddings)

        print(f"Generated embeddings for {len(docs)} documents using FAISS.")
        # db.save_local("faiss_index")

        db.save_local("faiss_index")
        
        
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