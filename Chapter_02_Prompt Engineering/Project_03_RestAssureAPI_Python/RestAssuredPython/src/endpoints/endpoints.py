from src.config.client import APIClient
from src.config.logger import LoggerSetup
from src.assertions.assertions import RestAssertions

logger = LoggerSetup.get_logger(__name__)

class APIEndpoints:
    """Centralized endpoint definitions."""

    # Booking endpoints
    BOOKINGS = "booking"
    BOOKING_BY_ID = "booking/{id}"
    BOOKING_AUTH = "auth/login"
    BOOKING_HEALTH = "ping"
