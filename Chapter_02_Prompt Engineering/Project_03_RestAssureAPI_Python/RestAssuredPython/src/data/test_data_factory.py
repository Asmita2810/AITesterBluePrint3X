from src.config.logger import LoggerSetup

logger = LoggerSetup.get_logger(__name__)

class TestDataFactory:
    """Generate test data for API testing."""

    @staticmethod
    def create_booking_payload(
        firstname="John",
        lastname="Doe",
        totalprice=100,
        depositpaid=True,
        checkin="2024-01-01",
        checkout="2024-01-07",
        additionalneeds="Breakfast"
    ):
        """Create booking payload for Restful Booker API."""
        payload = {
            "firstname": firstname,
            "lastname": lastname,
            "totalprice": totalprice,
            "depositpaid": depositpaid,
            "bookingdates": {
                "checkin": checkin,
                "checkout": checkout
            },
            "additionalneeds": additionalneeds
        }
        logger.info(f"Generated booking payload: {payload}")
        return payload

    @staticmethod
    def create_auth_payload(username="admin", password="password123"):
        """Create authentication payload."""
        payload = {
            "username": username,
            "password": password
        }
        logger.info(f"Generated auth payload for user: {username}")
        return payload

    @staticmethod
    def create_invalid_booking_payload(error_type="empty"):
        """Create invalid booking payloads for negative testing."""
        invalid_payloads = {
            "empty": {},
            "missing_firstname": {
                "lastname": "Doe",
                "totalprice": 100,
                "depositpaid": True,
                "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-07"}
            },
            "invalid_price": {
                "firstname": "John",
                "lastname": "Doe",
                "totalprice": -100,
                "depositpaid": True,
                "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-07"}
            },
            "invalid_dates": {
                "firstname": "John",
                "lastname": "Doe",
                "totalprice": 100,
                "depositpaid": True,
                "bookingdates": {"checkin": "2024-01-07", "checkout": "2024-01-01"}
            }
        }
        payload = invalid_payloads.get(error_type, {})
        logger.info(f"Generated invalid booking payload (type: {error_type})")
        return payload
