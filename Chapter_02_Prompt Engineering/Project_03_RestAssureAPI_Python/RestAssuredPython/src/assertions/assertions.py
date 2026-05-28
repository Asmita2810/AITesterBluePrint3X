from src.config.logger import LoggerSetup
import json
from jsonschema import validate, ValidationError

logger = LoggerSetup.get_logger(__name__)

class RestAssertions:
    """Enterprise-grade assertions for REST API responses."""

    def __init__(self, response):
        self.response = response
        self._assertions_count = 0

    def status_code(self, expected):
        """Assert response status code."""
        self._assertions_count += 1
        actual = self.response.status_code
        assert actual == expected, \
            f"[ASSERTION {self._assertions_count}] Status code mismatch. Expected: {expected}, Actual: {actual}"
        logger.info(f"✓ Status code assertion passed: {actual}")
        return self

    def status_ok(self):
        """Assert status is 2xx."""
        self._assertions_count += 1
        assert 200 <= self.response.status_code < 300, \
            f"[ASSERTION {self._assertions_count}] Expected 2xx status, got {self.response.status_code}"
        logger.info(f"✓ Status OK assertion passed: {self.response.status_code}")
        return self

    def content_type(self, expected):
        """Assert response content type."""
        self._assertions_count += 1
        actual = self.response.headers.get("Content-Type", "")
        assert expected in actual, \
            f"[ASSERTION {self._assertions_count}] Content-Type mismatch. Expected: {expected}, Actual: {actual}"
        logger.info(f"✓ Content-Type assertion passed: {actual}")
        return self

    def body_contains(self, *keys):
        """Assert response body contains specific keys."""
        try:
            body = self.response.json()
        except ValueError:
            raise AssertionError("[ASSERTION] Response body is not valid JSON")

        for key in keys:
            self._assertions_count += 1
            assert key in body or self._key_exists_nested(body, key), \
                f"[ASSERTION {self._assertions_count}] Key '{key}' not found in response"
            logger.info(f"✓ Body contains key assertion passed: {key}")
        return self

    def body_equals(self, expected_body):
        """Assert entire response body matches."""
        self._assertions_count += 1
        try:
            actual = self.response.json()
        except ValueError:
            raise AssertionError("[ASSERTION] Response body is not valid JSON")
        assert actual == expected_body, \
            f"[ASSERTION {self._assertions_count}] Body mismatch. Expected: {expected_body}, Actual: {actual}"
        logger.info("✓ Body equals assertion passed")
        return self

    def body_path(self, json_path, expected_value):
        """Assert specific JSON path value."""
        self._assertions_count += 1
        try:
            body = self.response.json()
            actual = self._extract_json_path(body, json_path)
            assert actual == expected_value, \
                f"[ASSERTION {self._assertions_count}] Path '{json_path}' mismatch. Expected: {expected_value}, Actual: {actual}"
            logger.info(f"✓ Body path assertion passed: {json_path} = {actual}")
        except KeyError:
            raise AssertionError(f"[ASSERTION] Path '{json_path}' not found in response")
        return self

    def header(self, header_name, expected_value):
        """Assert response header value."""
        self._assertions_count += 1
        actual = self.response.headers.get(header_name)
        assert actual == expected_value, \
            f"[ASSERTION {self._assertions_count}] Header '{header_name}' mismatch. Expected: {expected_value}, Actual: {actual}"
        logger.info(f"✓ Header assertion passed: {header_name} = {actual}")
        return self

    def header_exists(self, header_name):
        """Assert response header exists."""
        self._assertions_count += 1
        assert header_name in self.response.headers, \
            f"[ASSERTION {self._assertions_count}] Header '{header_name}' not found"
        logger.info(f"✓ Header exists assertion passed: {header_name}")
        return self

    def schema(self, json_schema):
        """Validate response against JSON schema."""
        self._assertions_count += 1
        try:
            body = self.response.json()
            validate(instance=body, schema=json_schema)
            logger.info("✓ Schema validation assertion passed")
        except ValidationError as e:
            raise AssertionError(f"[ASSERTION {self._assertions_count}] Schema validation failed: {e.message}")
        return self

    def response_time(self, max_seconds):
        """Assert response time is within threshold."""
        self._assertions_count += 1
        actual = self.response.elapsed.total_seconds()
        assert actual <= max_seconds, \
            f"[ASSERTION {self._assertions_count}] Response time exceeded. Expected <= {max_seconds}s, Actual: {actual}s"
        logger.info(f"✓ Response time assertion passed: {actual}s")
        return self

    def custom(self, condition, message):
        """Custom assertion with user-defined condition."""
        self._assertions_count += 1
        assert condition, f"[ASSERTION {self._assertions_count}] {message}"
        logger.info(f"✓ Custom assertion passed: {message}")
        return self

    @staticmethod
    def _key_exists_nested(obj, key):
        """Check if key exists in nested dictionary."""
        for k, v in obj.items():
            if k == key:
                return True
            if isinstance(v, dict) and RestAssertions._key_exists_nested(v, key):
                return True
        return False

    @staticmethod
    def _extract_json_path(obj, path):
        """Extract value from JSON path (dot notation)."""
        keys = path.split(".")
        current = obj
        for key in keys:
            if isinstance(current, dict):
                current = current[key]
            else:
                raise KeyError(f"Cannot access '{key}' in {current}")
        return current

    def get_assertion_count(self):
        """Get total assertions executed."""
        return self._assertions_count
