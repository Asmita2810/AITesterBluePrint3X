from typing import Optional, Dict, Any
from datetime import datetime, timedelta
from faker import Faker
from pydantic import BaseModel, Field

faker = Faker()

class BookingDates(BaseModel):
    """Booking dates model"""
    checkin: str
    checkout: str

class BookingPayload(BaseModel):
    """Complete booking payload model"""
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None

class TestDataFactory:
    """Factory for generating test data"""

    @staticmethod
    def create_valid_booking(
        firstname: Optional[str] = None,
        lastname: Optional[str] = None,
        totalprice: Optional[int] = None,
        depositpaid: Optional[bool] = None,
        checkin: Optional[str] = None,
        checkout: Optional[str] = None,
        additionalneeds: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create valid booking payload"""

        today = datetime.now()
        default_checkin = (today + timedelta(days=1)).strftime("%Y-%m-%d")
        default_checkout = (today + timedelta(days=7)).strftime("%Y-%m-%d")

        return {
            "firstname": firstname or faker.first_name(),
            "lastname": lastname or faker.last_name(),
            "totalprice": totalprice if totalprice is not None else faker.random_int(100, 5000),
            "depositpaid": depositpaid if depositpaid is not None else faker.boolean(),
            "bookingdates": {
                "checkin": checkin or default_checkin,
                "checkout": checkout or default_checkout
            },
            "additionalneeds": additionalneeds or faker.random_element(
                [None, "Breakfast", "WiFi", "Parking", "Late checkout"]
            )
        }

    @staticmethod
    def create_booking_with_missing_field(field_to_remove: str) -> Dict[str, Any]:
        """Create booking payload with missing required field"""
        booking = TestDataFactory.create_valid_booking()

        if field_to_remove in booking:
            del booking[field_to_remove]
        elif field_to_remove in ["checkin", "checkout"]:
            del booking["bookingdates"][field_to_remove]

        return booking

    @staticmethod
    def create_booking_with_invalid_dates(
        checkin: Optional[str] = None,
        checkout: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create booking with invalid date range (checkout before checkin)"""
        booking = TestDataFactory.create_valid_booking()

        if checkin and checkout:
            booking["bookingdates"]["checkin"] = checkin
            booking["bookingdates"]["checkout"] = checkout
        else:
            # Default: checkout 5 days before checkin
            today = datetime.now()
            booking["bookingdates"]["checkin"] = (today + timedelta(days=10)).strftime("%Y-%m-%d")
            booking["bookingdates"]["checkout"] = (today + timedelta(days=5)).strftime("%Y-%m-%d")

        return booking

    @staticmethod
    def create_booking_with_invalid_type(
        field_name: str = "totalprice",
        invalid_value: Any = "invalid"
    ) -> Dict[str, Any]:
        """Create booking with invalid field type"""
        booking = TestDataFactory.create_valid_booking()

        if field_name in booking:
            booking[field_name] = invalid_value
        elif field_name in ["checkin", "checkout"]:
            booking["bookingdates"][field_name] = invalid_value

        return booking

    @staticmethod
    def create_bulk_bookings(count: int) -> list:
        """Create multiple valid bookings"""
        return [TestDataFactory.create_valid_booking() for _ in range(count)]

    @staticmethod
    def create_empty_booking() -> Dict[str, Any]:
        """Create empty booking payload"""
        return {}

    @staticmethod
    def create_null_values_booking() -> Dict[str, Any]:
        """Create booking with null values"""
        return {
            "firstname": None,
            "lastname": None,
            "totalprice": None,
            "depositpaid": None,
            "bookingdates": {
                "checkin": None,
                "checkout": None
            }
        }

    @staticmethod
    def create_auth_credentials(
        username: Optional[str] = None,
        password: Optional[str] = None
    ) -> Dict[str, str]:
        """Create authentication credentials"""
        return {
            "username": username or "admin",
            "password": password or "password123"
        }
