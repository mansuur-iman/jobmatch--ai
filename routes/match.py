from fastapi import APIRouter
from controllers.match.controller import match_controller
match_route = APIRouter()

@match_route.post("/match")
def match():
    return match_controller()