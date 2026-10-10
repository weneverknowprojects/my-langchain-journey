

import asyncio

from chunk_manager import generate_chunk
from document_manager import load_document
from embedding_manager import embed_documents, embed_using_faiss, load_db_faiss
from retrieve_manager import retrieve

async def main():
    path = "~/Self Study/python/sample-docs/AIAgents.pdf"  # Replace with your PDF file path
    uploaded_docs = load_document(path)
    chunk_docs = generate_chunk(uploaded_docs)
    await embed_using_faiss(chunk_docs)
    db = load_db_faiss()
    retrieve("what is architecture of Agents", db)

if __name__ == "__main__":
    asyncio.run(main())
    