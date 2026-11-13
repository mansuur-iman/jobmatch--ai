import logging
from functools import lru_cache

from fastapi import APIRouter, HTTPException

from ingestion.profile_transformer import transform_profile
from schemas.recommendation import RecommendationRequest
from vector_store.scoring import distance_to_score
from vector_store.store import get_vector_store

logger = logging.getLogger(__name__)

recommendation_route = APIRouter()

MAX_RESULTS = 10
OVERFETCH = 5  


@lru_cache
def _store():
    return get_vector_store()


@recommendation_route.post("/recommendation")
def recommend(data: RecommendationRequest):
    query = transform_profile(data.profile)
    if not query.strip():
        raise HTTPException(status_code=422, detail="Profile has no searchable content")

    exclude = set(data.excludeJobIds)
    k = (MAX_RESULTS + len(exclude)) * OVERFETCH

    try:
        results = _store().similarity_search_with_score(query, k=k)
    except Exception:
        logger.exception("Recommendation search failed")
        raise HTTPException(status_code=502, detail="Recommendation service failed")

    seen = set(exclude)
    recommendations = []
    for doc, distance in results:
        job_id = doc.metadata["job_id"]
        if job_id in seen:
            continue
        seen.add(job_id)
        recommendations.append({"job_id": job_id, "score": distance_to_score(distance)})
        if len(recommendations) == MAX_RESULTS:
            break

    return {"recommendations": recommendations}