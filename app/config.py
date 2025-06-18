# app/config.py

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # JWT
    JWT_SIGNING_KEY: str = Field(alias="JWT_SIGNING_KEY")
    JWT_ALG: str = Field(alias="JWT_ALG")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(alias="REFRESH_TOKEN_EXPIRE_DAYS")

    # General
    DEBUG: bool = Field(alias="DEBUG")

    # Service URLs
    FARM_CALENDAR_API: str = Field(alias="GATEKEEPER_FARM_CALENDAR_API")
    FARM_CALENDAR_POST_AUTH: str = Field(alias="GATEKEEPER_FARM_CALENDAR_POST_AUTH")
    INTERNAL_GK_URL: str = Field(alias="INTERNAL_GK_URL")

    # DB
    DB_NAME: str = Field(alias="GATEKEEPER_DB_NAME")
    DB_USER: str = Field(alias="GATEKEEPER_DB_USER")
    DB_PASS: str = Field(alias="GATEKEEPER_DB_PASS")
    DB_HOST: str = Field(default="localhost", alias="GATEKEEPER_DB_HOST")
    DB_PORT: int = Field(default=3310, alias="GATEKEEPER_DB_PORT")

    # App host/port
    APP_HOST: str = Field(alias="GATEKEEPER_APP_HOST")
    APP_PORT: int = Field(alias="GATEKEEPER_APP_PORT")

    class Config:
        env_file = ".env"
        extra = "forbid"  # ensures undeclared keys in .env raise errors


settings = Settings()
