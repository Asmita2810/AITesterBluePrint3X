# REST Assured Framework - Python

> **Production-grade REST API testing framework using RICE POT principles**

## 📋 RICE-POT Framework Implementation

### **R — Role**
Expert API Automation Test Engineer specializing in enterprise-grade REST API testing frameworks

### **I — Instructions**
1. Build modular, reusable components following REST Assured patterns
2. Implement fluent assertion API for chained assertions
3. Centralize configuration and logging
4. Create comprehensive test data factory
5. Support both positive and negative test scenarios
6. Maintain complete request/response traceability

**Do NOT:**
- Hard-code test data in test methods
- Skip logging for debugging purposes
- Mix concerns (assertions, data, endpoints)
- Assume default behaviors

### **C — Context**
- Restful Booker API (https://restful-booker.herokuapp.com)
- Enterprise API testing requirements
- Support for multiple test scenarios (smoke, regression, negative, performance)

### **E — Example**
```python
response = api_client.post(APIEndpoints.BOOKINGS, json=payload)
assertions = RestAssertions(response)
assertions.status_code(200).body_contains("bookingid").response_time(5)
```

### **P — Parameters**
- Production-grade code quality
- Zero invented test data
- All assertions traceable to requirements
- Deterministic test execution
- Comprehensive logging at each step

### **O — Output**
- Executable Python test suite
- HTML test reports with pytest
- Structured logs for debugging
- Reusable framework components

### **T — Tone**
Technical, precise, production-ready code

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Edit `.env` file:
```env
BASE_URL=https://restful-booker.herokuapp.com
API_VERSION=v1
REQUEST_TIMEOUT=30
```

### 3. Run Tests
```bash
# All tests
pytest

# With HTML report
pytest --html=reports/report.html

# Specific test file
pytest tests/test_booking_api.py

# Specific test
pytest tests/test_booking_api.py::TestBookingAPI::test_tc001_health_check_success

# By marker
pytest -m smoke
pytest -m negative
pytest -m slow
```

---

## 📁 Project Structure

```
RestAssuredPython/
├── src/
│   ├── config/
│   │   ├── config.py         # Central configuration
│   │   ├── client.py         # API client with retry logic
│   │   └── logger.py         # Logging setup
│   ├── assertions/
│   │   └── assertions.py     # Fluent assertions library
│   ├── data/
│   │   └── test_data_factory.py  # Test data generation
│   └── endpoints/
│       └── endpoints.py      # Centralized endpoints
├── tests/
│   ├── conftest.py           # Pytest fixtures
│   └── test_booking_api.py   # Test implementations
├── logs/                     # Test execution logs
├── reports/                  # HTML test reports
├── requirements.txt          # Python dependencies
├── pytest.ini               # Pytest configuration
├── .env                     # Environment variables
└── README.md               # Documentation
```

---

## ✨ Key Features

### Fluent Assertions API
```python
assertions = RestAssertions(response)
assertions \
    .status_code(200) \
    .content_type("application/json") \
    .body_contains("firstname", "lastname") \
    .body_path("totalprice", 100) \
    .response_time(5)
```

### Centralized Configuration
- Load from `.env` file
- Support for auth (Bearer, Basic)
- Configurable retry logic
- SSL verification control

### Test Data Factory
```python
# Valid data
payload = TestDataFactory.create_booking_payload(
    firstname="John",
    totalprice=250
)

# Invalid data (for negative tests)
invalid = TestDataFactory.create_invalid_booking_payload("empty")
```

### Comprehensive Logging
- Separate logs for each test run
- Request/response logging
- Assertion traceability
- Performance metrics

### Pytest Integration
- Fixture-based setup/teardown
- Marker-based test categorization
- HTML report generation
- Automatic session logging

---

## 📝 Test Scenarios

### Positive Tests (Smoke)
- ✓ TC-001: Health check
- ✓ TC-002: Retrieve all bookings
- ✓ TC-003: Create booking with valid data
- ✓ TC-004: Get booking by ID
- ✓ TC-005: Update booking
- ✓ TC-006: Delete booking

### Negative Tests
- ✓ TC-007: Non-existent booking (404)
- ✓ TC-008: Empty payload
- ✓ TC-009: Invalid price
- ✓ TC-010: Invalid dates

### Performance Tests
- ✓ TC-011: Response time SLA compliance

### Regression Tests
- ✓ TC-012: Bulk booking operations

---

## 🔧 Advanced Usage

### Custom Assertions
```python
assertions.custom(
    condition=len(response.json()) > 0,
    message="Bookings list should not be empty"
)
```

### Schema Validation
```python
schema = {
    "type": "object",
    "properties": {
        "bookingid": {"type": "integer"}
    }
}
assertions.schema(schema)
```

### Authentication
```env
AUTH_ENABLED=true
AUTH_TYPE=bearer
AUTH_TOKEN=your_token_here
```

---

## 📊 Test Execution Output

```
TEST START: test_tc001_health_check_success
======================================================
[ATTEMPT 1] GET https://restful-booker.herokuapp.com/v1/ping
Response Status: 201
✓ Status code assertion passed: 201
✓ Header exists assertion passed: Server
TEST END: test_tc001_health_check_success
======================================================
```

---

## 🎯 Best Practices Implemented

✅ **Separation of Concerns** - Config, assertions, data, and tests are separate  
✅ **Fluent API** - Chainable assertions for readability  
✅ **DRY Principle** - Centralized endpoints and test data  
✅ **Logging** - Complete traceability of test execution  
✅ **Modularity** - Easy to extend and reuse components  
✅ **Error Handling** - Retry logic and meaningful error messages  
✅ **Documentation** - Inline comments and docstrings  
✅ **Zero Hallucination** - All data comes from explicit definitions  

---

## 📚 References

- [Restful Booker API Docs](https://restful-booker.herokuapp.com)
- [Pytest Documentation](https://docs.pytest.org/)
- [Requests Library](https://requests.readthedocs.io/)
- [REST Assured Java](https://rest-assured.io/)

---

## 📄 License

Educational use - Part of QA Automation Learning Blueprint 3X
