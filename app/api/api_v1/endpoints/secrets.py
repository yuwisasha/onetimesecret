from typing import Any
from secrets import token_urlsafe

from fastapi import APIRouter, HTTPException, Depends, Body
from redis.asyncio import Redis

from app.api import deps

router = APIRouter()


@router.post("/generate")
async def generate_secret_key(
    db: Redis = Depends(deps.get_db),
    content: str = Body(...),
    secret_phrase: str = Body(...),
) -> Any:
    """Create secret key for accessing secret"""
    secret_key = token_urlsafe(16)
    await db.hmset(
        secret_key,
        mapping={
            "secret_phrase": secret_phrase,
            "content": content,
        },
    ).execute()
    return {"secret_key": secret_key}


@router.post("/secrets/{secret_key}")
async def read_secret(
    secret_key: str,
    secret_phrase: str = Body(...),
    db: Redis = Depends(deps.get_db),
) -> Any:
    """Read secret with secret phrase and secret key given on create"""
    db_secret = await db.hgetall(secret_key).execute()
    if secret_phrase != db_secret[0]["secret_phrase"]:
        raise HTTPException(
            status_code=404,
            detail="Wrong catchphrase."
        )
    await db.delete(secret_key)
    return {"content": db_secret[0]["content"]}
