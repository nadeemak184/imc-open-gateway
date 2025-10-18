
# config.py
# Place to wire different providers and secrets.
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Add real provider API keys as environment variables or .env file.
    OPEN_GATEWAY_API_KEY: str | None = None
    PROVIDER_URL: str = "https://api.mock-opengateway.local"

settings = Settings()
