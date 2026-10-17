from pydantic import BaseModel

class RecommendationRequest(BaseModel):
    profile: dict
    excludeJobIds: list[str] = []