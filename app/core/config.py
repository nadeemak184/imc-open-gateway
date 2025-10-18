from pydantic import BaseSettings, HttpUrl

class Settings(BaseSettings):
    OPEN_GATEWAY_API_KEY: str
    OPEN_GATEWAY_BASE_URL: HttpUrl
    # option for sandbox vs production
    USE_SANDBOX: bool = True

    # timeouts, retry config
    REQUEST_TIMEOUT: float = 10.0
    MAX_RETRIES: int = 3

settings = Settings()
