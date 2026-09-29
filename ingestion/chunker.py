from vector_store.store import get_vector_store
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

vector_store = get_vector_store()

def process_documents(path):
    try:
        documents = TextLoader(path)
        loaded_documents = documents.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = text_splitter.split_documents(loaded_documents)

        vector_store.add_documents(chunks)
        print(f"successfully chunked and stored {len(chunks)}")
    except Exception as e:
        print(f"failed to process and store chunks: {e}")

