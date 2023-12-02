from typing import Optional, Any

from pydantic_settings import BaseSettings
from pydantic import validator, PostgresDsn


class Settings(BaseSettings):
    WORDS_BASE_URL: str
    WORDS_API_KEY: str
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=values.get('POSTGRES_DB') or '',
        )

    class Config:
        case_sensitive = False
        env_file = ".env"


settings = Settings()
