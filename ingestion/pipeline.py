from .loader import load_documents
from .parser import parse_json
from .transformer import transform_documents
from .chunker import process_documents

path = "data/candidate.json"

def ingestion(path):
    text = load_documents(path)
    documents = parse_json(text)
    transformer = transform_documents(documents)
    chunks = process_documents(transformer)

    return chunks
