from contextlib import asynccontextmanager

from pydantic import RedisDsn
from redis.asyncio import Redis


@asynccontextmanager
async def tmp_database(suffix: str = '') -> Redis:
    tmp_db_url = RedisDsn(f"redis://{suffix}")
    tmp_redis = Redis.from_url(str(tmp_db_url))

    try:
        yield tmp_redis
    finally:
        await tmp_redis.close()
