from fastapi import APIRouter
from schemas.match import MatchRequest
from agent.agent import match_agent

match_route = APIRouter()

@match_route.post("/api/v1/match")
async def match(data:MatchRequest):
    profile = data.profile
    job = data.job

    result =  await match_agent(profile, job)
    return result