

from chunk_manager import generate_chunk
from document_manager import load_document
from embedding_manager import embed_documents


if __name__ == "__main__":
    path = "~/Self Study/python/sample-docs/AIAgents.pdf"  # Replace with your PDF file path
    uploaded_docs = load_document(path)
    chunk_docs = generate_chunk(uploaded_docs)
    embed_documents(chunk_docs)
