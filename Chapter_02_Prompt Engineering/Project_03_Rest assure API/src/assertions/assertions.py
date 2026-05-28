from typing import Any, Dict, Optional, Union
import requests
from requests.models import Response

class APIAssertionError(AssertionError):
    """Custom assertion error for API testing"""
    pass

class APIAssertions:
    """Custom assertions for REST API testing"""

    @staticmethod
    def assert_status_code(response: Response, expected_status: Union[int, list]) -> None:
        """Assert response status code"""
        if isinstance(expected_status, list):
            if response.status_code not in expected_status:
                raise APIAssertionError(
                    f"Expected status code {expected_status}, "
                    f"got {response.status_code}. Response: {response.text}"
                )
        else:
            if response.status_code != expected_status:
                raise APIAssertionError(
                    f"Expected status code {expected_status}, "
                    f"got {response.status_code}. Response: {response.text}"
                )

    @staticmethod
    def assert_successful_response(response: Response) -> None:
        """Assert 2xx status code"""
        if not response.ok:
            raise APIAssertionError(
                f"Expected successful response (2xx), "
                f"got {response.status_code}. Response: {response.text}"
            )

    @staticmethod
    def assert_json_response(response: Response) -> Dict[str, Any]:
        """Assert response is valid JSON and return parsed data"""
        try:
            return response.json()
        except ValueError as e:
            raise APIAssertionError(
                f"Response is not valid JSON: {response.text}"
            ) from e

    @staticmethod
    def assert_key_exists(data: Dict[str, Any], key: str, path: str = "root") -> Any:
        """Assert key exists in dictionary"""
        if key not in data:
            raise APIAssertionError(
                f"Key '{key}' not found in {path}. Available keys: {list(data.keys())}"
            )
        return data[key]

    @staticmethod
    def assert_key_value(data: Dict[str, Any], key: str, expected_value: Any,
                        path: str = "root") -> None:
        """Assert key has expected value"""
        actual_value = APIAssertions.assert_key_exists(data, key, path)
        if actual_value != expected_value:
            raise APIAssertionError(
                f"At {path}.{key}: expected '{expected_value}', got '{actual_value}'"
            )

    @staticmethod
    def assert_response_contains(response: Response, text: str) -> None:
        """Assert response text contains substring"""
        if text not in response.text:
            raise APIAssertionError(
                f"Expected substring '{text}' not found in response. "
                f"Response: {response.text[:200]}"
            )

    @staticmethod
    def assert_response_time_less_than(response: Response, max_time_ms: float) -> None:
        """Assert response time is within threshold"""
        elapsed_ms = response.elapsed.total_seconds() * 1000
        if elapsed_ms > max_time_ms:
            raise APIAssertionError(
                f"Response took {elapsed_ms:.2f}ms, exceeds threshold {max_time_ms}ms"
            )

    @staticmethod
    def assert_header_exists(response: Response, header_name: str) -> str:
        """Assert header exists in response"""
        if header_name not in response.headers:
            raise APIAssertionError(
                f"Header '{header_name}' not found. Available headers: {list(response.headers.keys())}"
            )
        return response.headers[header_name]

    @staticmethod
    def assert_header_value(response: Response, header_name: str, expected_value: str) -> None:
        """Assert header has expected value"""
        actual_value = APIAssertions.assert_header_exists(response, header_name)
        if actual_value != expected_value:
            raise APIAssertionError(
                f"Header '{header_name}': expected '{expected_value}', got '{actual_value}'"
            )

    @staticmethod
    def assert_not_empty(value: Any, field_name: str = "value") -> None:
        """Assert value is not empty"""
        if not value:
            raise APIAssertionError(f"Field '{field_name}' is empty or None: {value}")

    @staticmethod
    def assert_array_length(data: list, expected_length: int, field_name: str = "array") -> None:
        """Assert array has expected length"""
        if len(data) != expected_length:
            raise APIAssertionError(
                f"Array '{field_name}' expected length {expected_length}, got {len(data)}"
            )

    @staticmethod
    def assert_array_not_empty(data: list, field_name: str = "array") -> None:
        """Assert array is not empty"""
        if not data:
            raise APIAssertionError(f"Array '{field_name}' is empty")

    @staticmethod
    def assert_content_type(response: Response, expected_type: str) -> None:
        """Assert response content type"""
        content_type = response.headers.get("Content-Type", "")
        if expected_type not in content_type:
            raise APIAssertionError(
                f"Expected content type '{expected_type}', got '{content_type}'"
            )
