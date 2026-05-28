import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Central configuration for API testing framework."""

    # API Endpoints
    BASE_URL = os.getenv("BASE_URL", "https://restful-booker.herokuapp.com")
    API_VERSION = os.getenv("API_VERSION", "v1")

    # Authentication
    AUTH_ENABLED = os.getenv("AUTH_ENABLED", "false").lower() == "true"
    AUTH_TYPE = os.getenv("AUTH_TYPE", "bearer")
    AUTH_TOKEN = os.getenv("AUTH_TOKEN", "")

    # Request Settings
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))
    VERIFY_SSL = os.getenv("VERIFY_SSL", "true").lower() == "true"

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_DIR = os.getenv("LOG_DIR", "logs")

    # Retry Settings
    RETRY_COUNT = int(os.getenv("RETRY_COUNT", "0"))
    RETRY_DELAY = int(os.getenv("RETRY_DELAY", "1"))

    @classmethod
    def get_full_url(cls, endpoint):
        """Build complete URL from base URL and endpoint."""
        return f"{cls.BASE_URL}/{cls.API_VERSION}/{endpoint}".replace("//", "/").replace(":/", "://")
