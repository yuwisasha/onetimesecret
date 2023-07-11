from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient
from redis.asyncio.client import Pipeline

from app.main import app
from tests.utils import tmp_database


@pytest_asyncio.fixture()
async def db() -> Pipeline:
    async with tmp_database("pytest") as tmp_db:
        async with tmp_db.pipeline(transaction=True) as db:
            yield db


@pytest_asyncio.fixture()
async def client() -> AsyncGenerator:
    async with AsyncClient(app=app, base_url=str("http://pytest")) as client:
        yield client
