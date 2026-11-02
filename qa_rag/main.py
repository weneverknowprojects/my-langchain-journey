

import asyncio

from chunk_manager import generate_chunk, generate_semantic_chunk
from document_manager import load_document
from embedding_manager import embed_documents, embed_using_faiss, load_db_faiss, embed_using_chroma, load_chroma_db
from retrieve_manager import retrieve, retrieve_from_chroma

async def main():
    path = "~/Self Study/python/sample-docs/Markdown to PDF.pdf"  # Replace with your PDF file path
    uploaded_docs = load_document(path)
    semantic_chunk_docs = generate_semantic_chunk(uploaded_docs)
    # chunk_docs = generate_chunk(uploaded_docs)
    embed_using_chroma(docs=semantic_chunk_docs)
    db = load_chroma_db()
    result = retrieve_from_chroma("what function in Telematics Service", db=db)
    print(f"result {result}")
    # db = load_db_faiss()
    # retrieve("what is architecture of Agents", db)

if __name__ == "__main__":
    asyncio.run(main())
    