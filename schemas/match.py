from pydantic import BaseModel

class MatchRequest(BaseModel):
   profile:dict
   job:dict