import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration class"""

    BASE_DIR = Path(__file__).parent.parent.parent
    ENV = os.getenv("ENV", "staging")

    # API Configuration
    API_BASE_URL = os.getenv("API_BASE_URL", "https://restful-booker.herokuapp.com")
    API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))
    API_RETRY_COUNT = int(os.getenv("API_RETRY_COUNT", "3"))
    API_RETRY_BACKOFF = float(os.getenv("API_RETRY_BACKOFF", "1.0"))

    # Auth Configuration
    AUTH_USERNAME = os.getenv("AUTH_USERNAME", "admin")
    AUTH_PASSWORD = os.getenv("AUTH_PASSWORD", "password123")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Report paths
    REPORTS_DIR = BASE_DIR / "reports"
    LOGS_DIR = REPORTS_DIR / "logs"

    @classmethod
    def get_base_url(cls) -> str:
        """Get API base URL based on environment"""
        return cls.API_BASE_URL

    @classmethod
    def get_timeout(cls) -> int:
        """Get request timeout"""
        return cls.API_TIMEOUT

    @classmethod
    def get_retry_config(cls) -> dict:
        """Get retry configuration"""
        return {
            "max_retries": cls.API_RETRY_COUNT,
            "backoff_factor": cls.API_RETRY_BACKOFF,
        }
