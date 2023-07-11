import pytest
from httpx import AsyncClient
from redis.asyncio.client import Pipeline

from app.core.config import settings


@pytest.mark.asyncio
async def test_create_secret(client: AsyncClient, db: Pipeline) -> None:
    secret = "123"
    secret_phrase = "12345"
    data = {"content": secret, "secret_phrase": secret_phrase}
    r = await client.post(
        f"{settings.API_V1_STR}/generate",
        json=data,
    )
    assert r.status_code == 200
    assert r.json()["secret_key"]


@pytest.mark.asyncio
async def test_read_secret(client: AsyncClient, db: Pipeline) -> None:
    secret = "string"
    secret_phrase = "string"
    data = {"content": secret, "secret_phrase": secret_phrase}
    r_1 = await client.post(
        f"{settings.API_V1_STR}/generate",
        json=data,
    )
    assert r_1.status_code == 200
    assert r_1.json()["secret_key"]
    data = {"secret_phrase": secret_phrase}
    r_2 = await client.post(
        f'{settings.API_V1_STR}/secrets/{r_1.json()["secret_key"]}',
        json=data,
    )
    assert r_2.status_code == 200
    assert r_2.json()["content"]
    assert r_2.json()["content"] == secret
