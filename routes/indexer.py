from fastapi import APIRouter
from schemas.jobs import IndexRequest
from ingestion.ingest import ingest_job

index_route = APIRouter()

@index_route.post("/api/v1/jobs/index")
def index_jobs(data:IndexRequest):
    indexed, failed = [], []

    for job in data.jobs:
        try:
            ingest_job(job.model_dump())
            indexed.append(job.id)
        except Exception as e:
            print(f"failed indexing job: {job.id}: {e}")
            failed.append(job.id)
    return {
        "indexed": indexed,
        "failed": failed
    }