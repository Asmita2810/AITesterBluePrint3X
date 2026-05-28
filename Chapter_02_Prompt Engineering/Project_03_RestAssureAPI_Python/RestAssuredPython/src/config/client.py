import requests
from src.config.config import Config
from src.config.logger import LoggerSetup
import time

logger = LoggerSetup.get_logger(__name__)

class APIClient:
    """REST API Client with request/response handling."""

    def __init__(self):
        self.session = requests.Session()
        self.last_response = None
        self._setup_session()

    def _setup_session(self):
        """Configure session with headers and auth if needed."""
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

        if Config.AUTH_ENABLED and Config.AUTH_TOKEN:
            if Config.AUTH_TYPE.lower() == "bearer":
                self.session.headers.update({
                    "Authorization": f"Bearer {Config.AUTH_TOKEN}"
                })
            elif Config.AUTH_TYPE.lower() == "basic":
                self.session.auth = (Config.AUTH_TOKEN, "")

    def request(self, method, endpoint, **kwargs):
        """Execute HTTP request with retry logic."""
        url = Config.get_full_url(endpoint)
        kwargs.setdefault("timeout", Config.REQUEST_TIMEOUT)
        kwargs.setdefault("verify", Config.VERIFY_SSL)

        for attempt in range(Config.RETRY_COUNT + 1):
            try:
                logger.info(f"[ATTEMPT {attempt + 1}] {method.upper()} {url}")
                if "json" in kwargs:
                    logger.debug(f"Request body: {kwargs['json']}")

                response = self.session.request(method, url, **kwargs)
                self.last_response = response

                logger.info(f"Response Status: {response.status_code}")
                logger.debug(f"Response body: {response.text[:500]}")

                return response

            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {e}")
                if attempt < Config.RETRY_COUNT:
                    time.sleep(Config.RETRY_DELAY)
                else:
                    raise

    def get(self, endpoint, **kwargs):
        """GET request."""
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        """POST request."""
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        """PUT request."""
        return self.request("PUT", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        """PATCH request."""
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        """DELETE request."""
        return self.request("DELETE", endpoint, **kwargs)

    def close(self):
        """Close session."""
        self.session.close()
