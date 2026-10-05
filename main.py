from fastapi import FastAPI

from routes.match import match_route

app = FastAPI()


@app.get("/health")
def health_check():
    return {
        "health": "ok"
    }


app.include_router(match_route)