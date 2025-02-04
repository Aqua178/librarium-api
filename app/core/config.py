from pydantic_settings import BaseSettings
from typing import Optional
import secrets


class Settings(BaseSettings):
    # Основные настройки приложения
    PROJECT_NAME: str = "Library API"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "API для управления библиотечным каталогом"
    API_V1_STR: str = "/api/v1"

    # Настройки базы данных
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "library_db"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Настройки безопасности
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 дней

    # CORS настройки
    BACKEND_CORS_ORIGINS: list = ["*"]

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "allow"  # Разрешаем дополнительные поля


settings = Settings()
