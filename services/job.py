import httpx
import os
from dotenv import load_dotenv

load_dotenv()

APPLICATION_URL = os.environ.get("APPLICATION_URL")

async def get_unindexed_jobs():
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(f"{APPLICATION_URL}/internal/ai/jobs")

        response.raise_for_status()
        return response.json()