from fastapi import FastAPI, Depends

from routes.match import match_route
from routes.indexer import index_route
from routes.recommendation import recommendation_route

from security import require_api_key

app = FastAPI(dependencies=[Depends(require_api_key)])


@app.get("/health")
def health_check():
    return {
        "health": "ok"
    }


app.include_router(match_route, prefix="/api/v1")
app.include_router(index_route, prefix="/api/v1")
app.include_router(recommendation_route, prefix="/api/v1")