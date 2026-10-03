from schemas import MatchRequest
from agent import match_agent
def match_controller(data:MatchRequest):
  profile = data.profile
  job = data.job

  return match_agent(profile, job)