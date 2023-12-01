from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    WORDS_BASE_URL: str
    WORDS_API_KEY: str

    class Config:
        case_sensitive = False
        env_file = ".env"


settings = Settings()
