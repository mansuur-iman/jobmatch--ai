from fastapi import APIRouter
from vector_store.store import get_vector_store
recommendationRoute = APIRouter()

store = get_vector_store();
@recommendationRoute.post("/api/v1/recommendation")
def recommendation(profile:dict):
  content = (
    f"University : {profile.get('university')}\n"
    f"Degree : {profile['degree']}\n"
    f"Work Enviroment : {profile['workEnviroment']}\n"
    f"Work Location : {profile['workLocation']}\n"
    f"Certifications: {(", ").join(profile.get('certifications') or [])}\n"
    f"Projects : {for project in profile['projects']: {project['name']}}
    f"Languages : {(", ".join(profile.get('languages')) or [])}\n"
    f"Job level : {profile['jobLevel']}\n"

  )