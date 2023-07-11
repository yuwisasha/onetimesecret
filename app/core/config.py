from typing import Any

from pydantic import RedisDsn, field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    REDIS_DATABASE_URI: RedisDsn | None = None

    @field_validator("REDIS_DATABASE_URI", mode="before")
    def assemble_db_connection(
        cls, v: str | None, values: dict[str, str]
    ) -> Any:
        if isinstance(v, str):
            return v
        return RedisDsn("redis://db")

    class Config:
        case_sensetive = True
        env_file = ".env"


settings = Settings()
