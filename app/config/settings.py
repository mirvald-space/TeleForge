"""
Settings module for the bot
"""
from pathlib import Path
from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for the bot"""
    # Bot settings
    bot_token: str = Field(..., description="Telegram Bot token from BotFather")
    bot_name: str = Field("TelegramBot", description="Bot name")

    # MongoDB settings
    mongodb_uri: str = Field(..., description="MongoDB connection URI")

    # Admin settings
    admin_ids: List[int] = Field(default_factory=list, description="List of admin user IDs")

    # Localization
    default_language: str = Field("en", description="Default language code")
    i18n_domain: str = Field("bot", description="Translation domain")
    i18n_path: Path = Field(Path(__file__).parent.parent.parent / "locales", description="Path to locales directory")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @field_validator("admin_ids", mode="before")
    def parse_admin_ids(cls, v):
        """Parse admin_ids from string to list of ints"""
        if isinstance(v, str):
            if "," in v:
                # Parse comma-separated list
                return [int(x.strip()) for x in v.split(",") if x.strip()]
            elif v.strip():
                # Parse single value
                return [int(v.strip())]
        elif isinstance(v, int):
            # Handle single integer
            return [v]
        return v


# Create settings instance
settings = Settings() 