from typing import AsyncGenerator

from app.db.session import redis


async def get_db() -> AsyncGenerator:
    async with redis.pipeline(transaction=True) as db:
        yield db
