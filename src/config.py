"""Configuration module using pydantic-settings."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_title: str = "My Analytics Dashboard"
    app_icon: str = "📊"

    data_file: str = "data/processed/sample_data.parquet"

    primary_color: str = "#2563EB"
    secondary_color: str = "#10B981"
    logo_path: str | None = None


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
