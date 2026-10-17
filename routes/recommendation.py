from fastapi import APIRouter
from vector_store.store import get_vector_store
from vector_store.scoring import distance_to_score
from ingestion.profile_transformer import transform_profile
from schemas.recommendation import RecommendationRequest
recommendationRoute = APIRouter()

store = get_vector_store();
@recommendationRoute.post("/api/v1/recommendations")
def recommendation(data:RecommendationRequest):
 query = transform_profile(data.profile);

 results = store.similarity_search_with_score(query, k=10 + len(data.excludeJobIds))

 exclude = set(data.excludeJobIds)
 recommendations = []

 for doc, distance in results:
  job_id = doc.metadata["job_id"]
  if job_id in exclude:
   continue
  recommendations.append({"job_id":job_id, "score": distance_to_score(distance)})
  if len(recommendations) == 10:
   break

 return {"recommendations": recommendations}
