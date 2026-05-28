import pytest
from src.config.config import Config
from src.config.logger import LoggerManager
from src.config.client import APIClient
from src.endpoints.endpoints import BookingEndpoint, AuthEndpoint, HealthEndpoint

LoggerManager.setup_logging()

@pytest.fixture(scope="session")
def api_client():
    """Create API client for the session"""
    client = APIClient()
    yield client
    client.close()

@pytest.fixture
def booking_endpoint(api_client):
    """Create booking endpoint manager"""
    return BookingEndpoint(api_client)

@pytest.fixture
def auth_endpoint(api_client):
    """Create auth endpoint manager"""
    return AuthEndpoint(api_client)

@pytest.fixture
def health_endpoint(api_client):
    """Create health endpoint manager"""
    return HealthEndpoint(api_client)

@pytest.fixture
def auth_token(auth_endpoint):
    """Get valid authentication token"""
    credentials = {
        "username": Config.AUTH_USERNAME,
        "password": Config.AUTH_PASSWORD
    }

    response = auth_endpoint.create_auth_token(credentials)

    if response.status_code == 200:
        token_data = response.json()
        return token_data.get("token")

    return None

@pytest.fixture(autouse=True)
def health_check(health_endpoint):
    """Verify API is healthy before each test"""
    response = health_endpoint.health_check()
    assert response.status_code == 201, "API health check failed"
    yield
