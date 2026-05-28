import pytest
from src.config.client import APIClient
from src.config.logger import LoggerSetup

logger = LoggerSetup.get_logger(__name__)

@pytest.fixture(scope="session")
def api_client():
    """Provide API client instance for entire test session."""
    client = APIClient()
    yield client
    client.close()
    logger.info("API client session closed")

@pytest.fixture(scope="function")
def reset_response(api_client):
    """Reset response between tests."""
    api_client.last_response = None
    yield
    logger.info("Response reset for next test")

@pytest.fixture(autouse=True)
def log_test_execution(request):
    """Log test execution start and end."""
    logger.info(f"\n{'='*60}")
    logger.info(f"TEST START: {request.node.name}")
    logger.info(f"{'='*60}")
    yield
    logger.info(f"TEST END: {request.node.name}")
    logger.info(f"{'='*60}\n")
