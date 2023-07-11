import pytest
from httpx import AsyncClient
from redis.asyncio.client import Pipeline


@pytest.mark.asyncio
async def test_create_secret(client: AsyncClient, db: Pipeline) -> None:
    secret = 123
    secret_phrase = 12345
    data = {"secret": secret, "secret_phrase": secret_phrase}
    r = await client.post(
        "/generate",
        json=data,
    )
    assert r
