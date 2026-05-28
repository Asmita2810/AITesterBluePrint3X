# Quick Start Guide - REST Assured Python Framework

## 1️⃣ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
```bash
# Clone/navigate to project
cd RestAssuredPython

# Install dependencies
pip install -r requirements.txt
```

**Installed Packages:**
- `requests==2.31.0` - HTTP client
- `pytest==7.4.3` - Test framework
- `pytest-html==4.1.1` - HTML reporting
- `python-dotenv==1.0.0` - Environment management
- `pyyaml==6.0.1` - Config file support
- `jsonschema==4.20.0` - JSON schema validation

---

## 2️⃣ Configuration

### Basic Setup (.env)
```env
# API Configuration
BASE_URL=https://restful-booker.herokuapp.com
API_VERSION=v1

# Request Settings
REQUEST_TIMEOUT=30
VERIFY_SSL=true

# Logging
LOG_LEVEL=INFO
LOG_DIR=logs

# Authentication (if needed)
AUTH_ENABLED=false
AUTH_TYPE=bearer
AUTH_TOKEN=
```

### For Different Environments
```bash
# Local testing
BASE_URL=http://localhost:3000

# Staging
BASE_URL=https://staging-api.example.com

# Production
BASE_URL=https://api.example.com
VERIFY_SSL=true
```

---

## 3️⃣ Running Tests

### All Tests
```bash
pytest
```

### With HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Specific Test File
```bash
pytest tests/test_booking_api.py -v
```

### Specific Test Case
```bash
pytest tests/test_booking_api.py::TestBookingAPI::test_tc003_create_booking_valid_data
```

### By Test Marker
```bash
# Smoke tests only
pytest -m smoke

# Negative tests only
pytest -m negative

# Performance tests
pytest -m slow

# All except slow
pytest -m "not slow"
```

### With Different Log Levels
```bash
pytest -v -s              # Show print statements
pytest -v -x              # Stop on first failure
pytest -v -k "create"     # Run tests matching keyword
```

---

## 4️⃣ Project Structure

```
RestAssuredPython/
│
├── src/
│   ├── config/
│   │   ├── config.py          # Configuration class
│   │   ├── client.py          # API client
│   │   └── logger.py          # Logging setup
│   │
│   ├── assertions/
│   │   └── assertions.py      # Assertion library (main magic!)
│   │
│   ├── data/
│   │   └── test_data_factory.py  # Generate test data
│   │
│   └── endpoints/
│       └── endpoints.py       # Centralized endpoints
│
├── tests/
│   ├── conftest.py            # Pytest fixtures
│   └── test_booking_api.py    # Test implementations
│
├── logs/                      # Auto-created, test logs
├── reports/                   # Auto-created, HTML reports
│
├── .env                       # Configuration
├── pytest.ini                # Pytest settings
├── requirements.txt          # Python dependencies
├── RICE-POT-Prompt.md        # Framework documentation
└── README.md                 # Overview & usage
```

---

## 5️⃣ Writing Your First Test

### Test Template
```python
def test_tc999_description(api_client):
    """
    TC-999: Test description
    Scenario: Scenario Name | Priority: High | Type: Smoke
    """
    # Arrange: Create test data
    payload = TestDataFactory.create_booking_payload(
        firstname="TestUser",
        totalprice=150
    )

    # Act: Make API call
    response = api_client.post(APIEndpoints.BOOKINGS, json=payload)

    # Assert: Verify response
    assertions = RestAssertions(response)
    assertions.status_code(200).body_contains("bookingid")

    logger.info("✓ Test passed")
```

### Common Patterns

#### Create → Read
```python
# Create
payload = TestDataFactory.create_booking_payload()
create_resp = api_client.post(APIEndpoints.BOOKINGS, json=payload)
booking_id = create_resp.json()["bookingid"]

# Read
response = api_client.get(APIEndpoints.BOOKING_BY_ID.format(id=booking_id))
RestAssertions(response).status_code(200)
```

#### Verify Field Values
```python
response = api_client.get(endpoint)
RestAssertions(response) \
    .body_path("firstname", "John") \
    .body_path("totalprice", 100) \
    .body_path("bookingdates.checkin", "2024-01-01")
```

#### Error Handling
```python
response = api_client.get(APIEndpoints.BOOKING_BY_ID.format(id=99999))
RestAssertions(response).status_code(404)

# Or without assertions
assert response.status_code == 400
```

---

## 6️⃣ Understanding Assertions

### Fluent Chain (Recommended)
```python
RestAssertions(response) \
    .status_code(200) \
    .content_type("application/json") \
    .body_contains("firstname", "lastname") \
    .response_time(5)
```

### Available Assertions

| Method | Example | Purpose |
|--------|---------|---------|
| `status_code()` | `.status_code(200)` | Assert exact status |
| `status_ok()` | `.status_ok()` | Assert 2xx status |
| `content_type()` | `.content_type("json")` | Assert content type |
| `body_contains()` | `.body_contains("id")` | Assert keys exist |
| `body_equals()` | `.body_equals({...})` | Assert entire body |
| `body_path()` | `.body_path("user.name", "John")` | Assert JSON path |
| `header()` | `.header("X-Custom", "value")` | Assert header value |
| `header_exists()` | `.header_exists("Server")` | Assert header exists |
| `schema()` | `.schema(schema_def)` | Validate JSON schema |
| `response_time()` | `.response_time(5)` | Assert response time |
| `custom()` | `.custom(len(x) > 0, "msg")` | Custom condition |

---

## 7️⃣ Debugging Failed Tests

### Check Logs
```bash
# View latest log
tail -f logs/api_test_*.log

# Search for errors
grep ERROR logs/api_test_*.log
```

### Run Single Test with Output
```bash
pytest tests/test_booking_api.py::TestBookingAPI::test_tc003_create_booking_valid_data -v -s
```

### Print Response Details
```python
response = api_client.post(endpoint, json=payload)
print(f"Status: {response.status_code}")
print(f"Body: {response.json()}")
print(f"Headers: {dict(response.headers)}")
```

### Test Report
```bash
# Open HTML report in browser
open reports/report.html  # macOS
start reports/report.html  # Windows
```

---

## 8️⃣ Best Practices

### ✅ DO
- Use test data factory for all data
- Centralize endpoints in `APIEndpoints`
- Chain assertions for readability
- Log important values
- Use descriptive test names
- Mark tests appropriately (smoke, negative, etc.)

### ❌ DON'T
- Hard-code test data in tests
- Make assumptions about API behavior
- Skip error cases
- Ignore logging
- Create multiple API client instances
- Mixed concerns (data + assertions)

### Example: ✅ Good
```python
def test_create_booking_valid(api_client):
    payload = TestDataFactory.create_booking_payload()
    response = api_client.post(APIEndpoints.BOOKINGS, json=payload)
    RestAssertions(response).status_code(200).body_contains("bookingid")
```

### Example: ❌ Avoid
```python
def test_create_booking(api_client):
    response = api_client.post(
        "https://restful-booker.herokuapp.com/v1/booking",
        json={"firstname": "John"}  # Hard-coded!
    )
    assert response.status_code == 200  # No structure
```

---

## 9️⃣ Common Issues

### Issue: Tests hang
```
Solution: Increase REQUEST_TIMEOUT in .env
REQUEST_TIMEOUT=60
```

### Issue: SSL certificate error
```
Solution: Disable SSL verification for testing
VERIFY_SSL=false
```

### Issue: ImportError for src modules
```
Solution: Run pytest from project root
cd RestAssuredPython
pytest
```

### Issue: Logs not appearing
```
Solution: Check LOG_LEVEL and ensure logs/ directory exists
LOG_LEVEL=INFO
mkdir -p logs
```

---

## 🔟 Next Steps

1. ✅ Install dependencies
2. ✅ Configure `.env`
3. ✅ Run `pytest` to verify setup
4. ✅ Check `logs/` and `reports/` directories
5. ✅ Examine existing test cases
6. ✅ Write your first custom test
7. ✅ Run tests with markers
8. ✅ Review HTML report

---

## 📞 Quick Reference

```bash
# Install
pip install -r requirements.txt

# Run all tests
pytest -v

# Run with report
pytest --html=reports/report.html

# Run smoke tests
pytest -m smoke -v

# Run single test
pytest tests/test_booking_api.py::TestBookingAPI::test_tc001_health_check_success -v

# View logs
tail logs/api_test_*.log

# Run with debugging
pytest -v -s --tb=short
```

---

Happy Testing! 🚀
