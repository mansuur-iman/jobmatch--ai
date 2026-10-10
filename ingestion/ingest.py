from vector_store.store import get_vector_store
from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.transformer import transform_job

vector_store = get_vector_store()
text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
def ingest_job(job:dict)->int:
 
    document = transform_job(job)

    chunks = text_splitter.split_documents([document])
    ids = [f"{job['id']} : {i}" for i in range(len(chunks))]

    vector_store.add_documents(chunks, ids)

    print(f"Successfully chunked and stored {len(chunks)} chunks")

    return len(chunks)

  
