from typing import Optional
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .config import Config
from .logger import LoggerManager

logger = LoggerManager.get_logger(__name__)

class APIClient:
    """REST API client with built-in retry and error handling"""

    def __init__(self, base_url: Optional[str] = None, timeout: Optional[int] = None):
        self.base_url = base_url or Config.get_base_url()
        self.timeout = timeout or Config.get_timeout()
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """Create requests session with retry strategy"""
        session = requests.Session()

        retry_config = Config.get_retry_config()
        retry_strategy = Retry(
            total=retry_config["max_retries"],
            backoff_factor=retry_config["backoff_factor"],
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH"]
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        """GET request"""
        url = self._build_url(endpoint)
        logger.info(f"GET {url}")
        return self.session.get(url, timeout=self.timeout, **kwargs)

    def post(self, endpoint: str, json=None, **kwargs) -> requests.Response:
        """POST request"""
        url = self._build_url(endpoint)
        logger.info(f"POST {url} - Body: {json}")
        return self.session.post(url, json=json, timeout=self.timeout, **kwargs)

    def put(self, endpoint: str, json=None, **kwargs) -> requests.Response:
        """PUT request"""
        url = self._build_url(endpoint)
        logger.info(f"PUT {url} - Body: {json}")
        return self.session.put(url, json=json, timeout=self.timeout, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """DELETE request"""
        url = self._build_url(endpoint)
        logger.info(f"DELETE {url}")
        return self.session.delete(url, timeout=self.timeout, **kwargs)

    def patch(self, endpoint: str, json=None, **kwargs) -> requests.Response:
        """PATCH request"""
        url = self._build_url(endpoint)
        logger.info(f"PATCH {url} - Body: {json}")
        return self.session.patch(url, json=json, timeout=self.timeout, **kwargs)

    def _build_url(self, endpoint: str) -> str:
        """Build full URL from endpoint"""
        if endpoint.startswith("http"):
            return endpoint
        return f"{self.base_url}{endpoint}"

    def close(self):
        """Close session"""
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
