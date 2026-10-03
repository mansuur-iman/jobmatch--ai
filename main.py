
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def healthCheck():
    return {
        "health": "ok"
    }