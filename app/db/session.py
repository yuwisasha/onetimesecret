from redis.asyncio import Redis

from app.core.config import settings

redis = Redis.from_url(str(settings.REDIS_DATABASE_URI), decode_responses=True)
