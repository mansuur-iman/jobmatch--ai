
from .transformer import transform_documents
from .chunker import process_documents

def ingestion(profile:dict):
   
    documents = transform_documents(profile)
    chunks = process_documents(documents)

    return chunks
