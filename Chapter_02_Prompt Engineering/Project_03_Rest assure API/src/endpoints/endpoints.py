from typing import Optional, Dict, Any
import requests
from ..config.client import APIClient
from ..config.logger import LoggerManager
from ..assertions.assertions import APIAssertions

logger = LoggerManager.get_logger(__name__)

class BookingEndpoint:
    """Endpoint manager for Booking API endpoints"""

    BASE_ENDPOINT = "/booking"

    def __init__(self, client: Optional[APIClient] = None):
        self.client = client or APIClient()
        self.auth_token = None

    def create_booking(self, booking_data: Dict[str, Any]) -> requests.Response:
        """POST /booking - Create new booking"""
        logger.info(f"Creating booking: {booking_data}")
        response = self.client.post(self.BASE_ENDPOINT, json=booking_data)
        logger.info(f"Create booking response: {response.status_code}")
        return response

    def get_booking(self, booking_id: int) -> requests.Response:
        """GET /booking/{id} - Retrieve booking by ID"""
        endpoint = f"{self.BASE_ENDPOINT}/{booking_id}"
        logger.info(f"Getting booking ID: {booking_id}")
        response = self.client.get(endpoint)
        logger.info(f"Get booking response: {response.status_code}")
        return response

    def get_all_bookings(self, filters: Optional[Dict[str, Any]] = None) -> requests.Response:
        """GET /booking - Get all bookings with optional filters"""
        logger.info(f"Getting all bookings with filters: {filters}")
        response = self.client.get(self.BASE_ENDPOINT, params=filters)
        logger.info(f"Get all bookings response: {response.status_code}")
        return response

    def update_booking(
        self,
        booking_id: int,
        booking_data: Dict[str, Any],
        auth_token: Optional[str] = None
    ) -> requests.Response:
        """PUT /booking/{id} - Update booking"""
        endpoint = f"{self.BASE_ENDPOINT}/{booking_id}"
        headers = {}

        if auth_token:
            headers["Cookie"] = f"token={auth_token}"

        logger.info(f"Updating booking ID: {booking_id}")
        response = self.client.put(endpoint, json=booking_data, headers=headers)
        logger.info(f"Update booking response: {response.status_code}")
        return response

    def partial_update_booking(
        self,
        booking_id: int,
        booking_data: Dict[str, Any],
        auth_token: Optional[str] = None
    ) -> requests.Response:
        """PATCH /booking/{id} - Partially update booking"""
        endpoint = f"{self.BASE_ENDPOINT}/{booking_id}"
        headers = {}

        if auth_token:
            headers["Cookie"] = f"token={auth_token}"

        logger.info(f"Partially updating booking ID: {booking_id}")
        response = self.client.patch(endpoint, json=booking_data, headers=headers)
        logger.info(f"Partial update response: {response.status_code}")
        return response

    def delete_booking(
        self,
        booking_id: int,
        auth_token: Optional[str] = None
    ) -> requests.Response:
        """DELETE /booking/{id} - Delete booking"""
        endpoint = f"{self.BASE_ENDPOINT}/{booking_id}"
        headers = {}

        if auth_token:
            headers["Cookie"] = f"token={auth_token}"

        logger.info(f"Deleting booking ID: {booking_id}")
        response = self.client.delete(endpoint, headers=headers)
        logger.info(f"Delete booking response: {response.status_code}")
        return response

class AuthEndpoint:
    """Endpoint manager for Authentication endpoints"""

    BASE_ENDPOINT = "/auth"

    def __init__(self, client: Optional[APIClient] = None):
        self.client = client or APIClient()

    def create_auth_token(self, credentials: Dict[str, str]) -> requests.Response:
        """POST /auth - Create authentication token"""
        logger.info("Creating auth token")
        response = self.client.post(self.BASE_ENDPOINT, json=credentials)
        logger.info(f"Create auth token response: {response.status_code}")
        return response

class HealthEndpoint:
    """Endpoint manager for Health check endpoints"""

    BASE_ENDPOINT = "/ping"

    def __init__(self, client: Optional[APIClient] = None):
        self.client = client or APIClient()

    def health_check(self) -> requests.Response:
        """GET /ping - Health check"""
        logger.info("Running health check")
        response = self.client.get(self.BASE_ENDPOINT)
        logger.info(f"Health check response: {response.status_code}")
        return response
