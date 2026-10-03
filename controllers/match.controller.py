from schemas.match.schema import MatchRequest
def match_controller(data:MatchRequest):
  profile = data.profile
  job = data.job

  return match_agent(profile, job)