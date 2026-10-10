from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from llm_manager import send_message

def retrieve_documents(query: str, db: FAISS) -> list[Document]|None:
    """
    Retrieve documents from the FAISS database based on the provided query.
    
    Args:
        query (str): The query string to search for relevant documents.
        db: The FAISS database object.
        
    Returns:
        list[Document]: A list of retrieved Document objects.
    """
    if db is None:
        print("FAISS database is not loaded.")
        return None
    
    # Perform the retrieval using the FAISS database
    results = db.similarity_search(query, k=3)  # Adjust 'k' as needed for the number of results to retrieve    
    return results

def retrieve(query:str, db: FAISS) -> str|None:
    try:
        docs = retrieve_documents(query, db)
        context = "\n\n".join([doc.page_content for doc in docs])
        result = send_message(query, context)
        print(f"result {result.content}")
        return result.content
    except Exception as e:
        print(f"retrieve error {e}")
        return None
