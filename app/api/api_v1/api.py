from fastapi import APIRouter

from app.api.api_v1.endpoints import secrets

api_router = APIRouter()

api_router.include_router(secrets.router)
