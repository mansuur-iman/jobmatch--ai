from fastapi import APIRouter
from vector_store.store import get_vector_store
from ingestion.profile_transformer import transform_profile
recommendationRoute = APIRouter()

store = get_vector_store();
@recommendationRoute.post("/api/v1/recommendation")
def recommendation(profile:dict):
 query = transform_profile(profile);

 results = store.similarity_search(query, k=10);

 job_ids = [
  document.metadata["job_id"]
  for document in results
 ]
 return {
  "job_ids" : job_ids
 }