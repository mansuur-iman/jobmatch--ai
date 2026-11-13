import logging

from fastapi import APIRouter, HTTPException

from agent.agent import match_profile_to_job
from schemas.match import JobMatchOutput, MatchRequest

logger = logging.getLogger(__name__)

match_route = APIRouter()


@match_route.post("/match", response_model=JobMatchOutput)
async def match_profile(data: MatchRequest):
    try:
        return await match_profile_to_job(data.profile, data.job)
    except Exception:
        logger.exception("Job match failed")
        raise HTTPException(status_code=502, detail="Matching service failed")