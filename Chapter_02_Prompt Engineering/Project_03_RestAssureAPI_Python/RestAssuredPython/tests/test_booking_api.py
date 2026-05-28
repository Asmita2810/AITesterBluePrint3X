import pytest
from src.config.client import APIClient
from src.config.logger import LoggerSetup
from src.assertions.assertions import RestAssertions
from src.data.test_data_factory import TestDataFactory
from src.endpoints.endpoints import APIEndpoints

logger = LoggerSetup.get_logger(__name__)

class TestBookingAPI:
    """Test Suite: Restful Booker API - Booking Management"""

    def test_tc001_health_check_success(self, api_client):
        """
        TC-001: Verify API health check returns success
        Scenario: Health Check | Priority: High | Type: Smoke
        """
        response = api_client.get(APIEndpoints.BOOKING_HEALTH)

        assertions = RestAssertions(response)
        assertions.status_code(201).header_exists("Server")

        logger.info(f"✓ TC-001 passed with {assertions.get_assertion_count()} assertions")

    def test_tc002_get_all_bookings_success(self, api_client):
        """
        TC-002: Retrieve all bookings
        Scenario: GET All Bookings | Priority: High | Type: Smoke
        """
        response = api_client.get(APIEndpoints.BOOKINGS)

        assertions = RestAssertions(response)
        assertions.status_code(200).content_type("application/json")

        body = response.json()
        assert isinstance(body, list), "Response should be list of bookings"

        logger.info(f"✓ TC-002 passed - Retrieved {len(body)} bookings")

    def test_tc003_create_booking_valid_data(self, api_client):
        """
        TC-003: Create booking with valid data
        Scenario: POST Create Booking | Priority: High | Type: Smoke
        """
        payload = TestDataFactory.create_booking_payload(
            firstname="Alice",
            lastname="Johnson",
            totalprice=250,
            depositpaid=False
        )

        response = api_client.post(APIEndpoints.BOOKINGS, json=payload)

        assertions = RestAssertions(response)
        assertions.status_code(200)
        assertions.body_contains("bookingid")

        booking_id = response.json().get("bookingid")
        logger.info(f"✓ TC-003 passed - Created booking ID: {booking_id}")

    def test_tc004_get_booking_by_id_success(self, api_client):
        """
        TC-004: Retrieve specific booking by ID
        Scenario: GET Booking by ID | Priority: High | Type: Smoke
        """
        payload = TestDataFactory.create_booking_payload()
        create_response = api_client.post(APIEndpoints.BOOKINGS, json=payload)
        booking_id = create_response.json()["bookingid"]

        response = api_client.get(APIEndpoints.BOOKING_BY_ID.format(id=booking_id))

        assertions = RestAssertions(response)
        assertions.status_code(200)
        assertions.body_contains("firstname", "lastname", "totalprice")
        assertions.body_path("firstname", payload["firstname"])

        logger.info(f"✓ TC-004 passed - Retrieved booking {booking_id}")

    def test_tc005_update_booking_valid_data(self, api_client):
        """
        TC-005: Update booking with valid data
        Scenario: PUT Update Booking | Priority: High | Type: Regression
        """
        original_payload = TestDataFactory.create_booking_payload()
        create_response = api_client.post(APIEndpoints.BOOKINGS, json=original_payload)
        booking_id = create_response.json()["bookingid"]

        updated_payload = TestDataFactory.create_booking_payload(
            firstname="Updated",
            totalprice=500
        )

        response = api_client.put(
            APIEndpoints.BOOKING_BY_ID.format(id=booking_id),
            json=updated_payload,
            headers={"Cookie": "token=test"}
        )

        assertions = RestAssertions(response)
        assertions.status_code(200)
        assertions.body_path("firstname", "Updated")
        assertions.body_path("totalprice", 500)

        logger.info(f"✓ TC-005 passed - Updated booking {booking_id}")

    def test_tc006_delete_booking_success(self, api_client):
        """
        TC-006: Delete booking successfully
        Scenario: DELETE Booking | Priority: High | Type: Regression
        """
        payload = TestDataFactory.create_booking_payload()
        create_response = api_client.post(APIEndpoints.BOOKINGS, json=payload)
        booking_id = create_response.json()["bookingid"]

        response = api_client.delete(
            APIEndpoints.BOOKING_BY_ID.format(id=booking_id),
            headers={"Cookie": "token=test"}
        )

        assertions = RestAssertions(response)
        assertions.status_code(201)

        logger.info(f"✓ TC-006 passed - Deleted booking {booking_id}")

    @pytest.mark.negative
    def test_tc007_get_nonexistent_booking(self, api_client):
        """
        TC-007: Attempt to retrieve non-existent booking (Negative Test)
        Scenario: GET Non-existent Booking | Priority: Medium | Type: Negative
        """
        response = api_client.get(APIEndpoints.BOOKING_BY_ID.format(id=99999))

        assertions = RestAssertions(response)
        assertions.status_code(404)

        logger.info("✓ TC-007 passed - Non-existent booking returns 404")

    @pytest.mark.negative
    def test_tc008_create_booking_invalid_data_empty_payload(self, api_client):
        """
        TC-008: Create booking with empty payload (Negative Test)
        Scenario: POST Booking Empty Data | Priority: Medium | Type: Negative
        """
        payload = TestDataFactory.create_invalid_booking_payload("empty")

        response = api_client.post(APIEndpoints.BOOKINGS, json=payload)

        assert response.status_code in [400, 500], \
            "Empty payload should result in 4xx or 5xx error"

        logger.info("✓ TC-008 passed - Empty payload correctly rejected")

    @pytest.mark.negative
    def test_tc009_create_booking_invalid_price(self, api_client):
        """
        TC-009: Create booking with negative price (Negative Test)
        Scenario: POST Booking Negative Price | Priority: Medium | Type: Negative
        """
        payload = TestDataFactory.create_invalid_booking_payload("invalid_price")

        response = api_client.post(APIEndpoints.BOOKINGS, json=payload)

        assert response.status_code in [400, 500], \
            "Negative price should be rejected"

        logger.info("✓ TC-009 passed - Negative price correctly rejected")

    @pytest.mark.negative
    def test_tc010_create_booking_invalid_dates(self, api_client):
        """
        TC-010: Create booking with checkout before checkin (Negative Test)
        Scenario: POST Booking Invalid Dates | Priority: Medium | Type: Negative
        """
        payload = TestDataFactory.create_invalid_booking_payload("invalid_dates")

        response = api_client.post(APIEndpoints.BOOKINGS, json=payload)

        assert response.status_code in [400, 500], \
            "Invalid date range should be rejected"

        logger.info("✓ TC-010 passed - Invalid dates correctly rejected")

    @pytest.mark.slow
    def test_tc011_response_time_compliance(self, api_client):
        """
        TC-011: Verify API response time is within SLA
        Scenario: Response Time SLA | Priority: Medium | Type: Performance
        """
        response = api_client.get(APIEndpoints.BOOKINGS)

        assertions = RestAssertions(response)
        assertions.status_ok()
        assertions.response_time(max_seconds=5)

        logger.info("✓ TC-011 passed - Response time within SLA")

    def test_tc012_create_multiple_bookings_and_verify(self, api_client):
        """
        TC-012: Create multiple bookings and verify retrieval
        Scenario: Bulk Booking Creation | Priority: Medium | Type: Regression
        """
        created_ids = []

        for i in range(3):
            payload = TestDataFactory.create_booking_payload(
                firstname=f"User{i}",
                lastname=f"Test{i}",
                totalprice=100 + (i * 50)
            )
            response = api_client.post(APIEndpoints.BOOKINGS, json=payload)
            created_ids.append(response.json()["bookingid"])

        all_bookings = api_client.get(APIEndpoints.BOOKINGS).json()

        for booking_id in created_ids:
            assert any(b.get("bookingid") == booking_id for b in all_bookings), \
                f"Booking {booking_id} not found in all bookings"

        logger.info(f"✓ TC-012 passed - Verified {len(created_ids)} bookings")
