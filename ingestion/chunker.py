from vector_store.store import get_vector_store
from langchain_text_splitters import RecursiveCharacterTextSplitter
from services.job import get_unindexed_jobs
from ingestion.transformer import transform_job

vector_store = get_vector_store()
async def process_documents()->list:
    try:
        jobs = await get_unindexed_jobs()

        langchain_documents = []

        for job in jobs:
            document = transform_job(job)
            langchain_documents.append(document)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = text_splitter.split_documents(langchain_documents)

        vector_store.add_documents(chunks)

        print(f"Successfully chunked and stored {len(chunks)} chunks")

        return chunks

    except Exception as e:
        print(f"Failed to process and store chunks: {e}")
        return []
