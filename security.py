import os
import secrets
from fastapi import Header, HTTPException, status

def require_api_key(x_api_key: str = Header(default="")):
    expected = os.environ.get("AI_SERVICE_API_KEY")
    if not expected:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, "Server key not configured")
    if not secrets.compare_digest(x_api_key, expected):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid API key")