from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    DATABASE_URL: str
    API_PREFIX: str = "/api"
    DEBUG: bool = False

    ALLOWED_ORIGINS: List[str] = Field(default_factory=list)

    AZURE_KEYVAULT_NAME: str = "open-ai-keys-rob"
    AZURE_OPENAI_SECRET_NAME: str = "open-ai-key-rob"

    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_DEPLOYMENT: str
    AZURE_OPENAI_API_VERSION: str = "preview"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()