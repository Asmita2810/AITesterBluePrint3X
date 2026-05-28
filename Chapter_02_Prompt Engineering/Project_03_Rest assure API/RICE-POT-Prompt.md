## 🤖 RICE-POT Prompt Framework: REST Assured API Testing Framework in Python

---

### **R — Role**
Expert QA Automation Engineer with 15+ years of experience in API testing, REST protocol expertise, and Python-based test automation framework design. Should demonstrate proficiency in pytest, requests library, and enterprise-grade testing patterns.

---

### **I — Instructions**

#### **MUST DO:**
1. Create a production-ready REST API testing framework using Python 3.9+
2. Use pytest as the test runner and requests library for HTTP calls
3. Implement Page Object Model (POM) equivalent called "Endpoint Manager" pattern for API endpoints
4. Create reusable request/response builders with fluent API design
5. Implement comprehensive assertion library for API testing
6. Create test data factories for generating consistent test payloads
7. Implement comprehensive logging and reporting mechanisms
8. Support both positive and negative test scenarios
9. Include request/response interceptors for debugging
10. Add retry mechanisms for flaky API calls (with exponential backoff)

#### **Do NOT:**
- Use hardcoded credentials or API keys in code (use environment variables)
- Create monolithic test files; separate by endpoint/feature
- Skip exception handling in API calls
- Use generic assertions; implement specific API assertions
- Mix test data with test logic
- Ignore response time metrics
- Create brittle tests dependent on specific ordering
- Use global variables for test state

---

### **C — Context**

**System Under Test:** Restful Booker API (https://restful-booker.herokuapp.com)

**Key Endpoints:**
- `POST /booking` - Create booking
- `GET /booking/{id}` - Retrieve booking
- `PUT /booking/{id}` - Update booking
- `DELETE /booking/{id}` - Delete booking
- `GET /auth` - Token-based authentication
- `GET /ping` - Health check

**API Authentication:** Cookie-based token authentication
**Base URL:** https://restful-booker.herokuapp.com

---

### **E — Example Output Structure**

```python
# Example test using the framework
def test_create_booking_happy_path():
    """Verify POST /booking creates booking successfully with valid payload"""
    
    booking_payload = TestDataFactory.create_valid_booking(
        firstname="John",
        lastname="Doe",
        checkin="2026-06-01",
        checkout="2026-06-07"
    )
    
    response = BookingEndpoint.create_booking(booking_payload)
    
    BookingAssertions.assert_successful_creation(response)
    BookingAssertions.assert_booking_id_exists(response)
    BookingAssertions.assert_booking_details_match(response, booking_payload)
```

---

### **P — Parameters**

#### **Quality Constraints:**
- **Deterministic:** Same test input → Same test output (no randomness in test logic)
- **No Hallucination:** All assertions based on actual API responses, no invented fields
- **Traceability:** Every test must be traceable to a specific API requirement
- **Response Validation:** Every assertion validates against documented API spec
- **Error Handling:** All HTTP errors handled with specific exception classes
- **Timeout Management:** All requests have configurable timeouts (default 30s)
- **Type Safety:** Use type hints throughout the codebase
- **Performance Tracking:** Log response times for all API calls

#### **Code Standards:**
- PEP 8 compliant
- Docstrings for all classes and public methods
- No magic numbers; use named constants
- All dependencies in requirements.txt with pinned versions
- CI/CD compatible (no UI dependencies)

---

### **O — Output**

**Format:** Python package with modular structure

**Deliverables:**
1. `/config/` - Configuration management (environments, credentials)
2. `/data/` - Test data factories and fixtures
3. `/endpoints/` - Endpoint managers (API abstraction layer)
4. `/assertions/` - Custom assertion library
5. `/tests/` - Test cases organized by feature
6. `/reports/` - HTML reports and logs
7. `/utils/` - Helper utilities (logging, retry logic, etc.)
8. `requirements.txt` - Python dependencies
9. `pytest.ini` - Pytest configuration
10. `JIRA_ISSUES.md` - Test cases in JIRA format
11. `README.md` - Complete documentation with RICE-POT breakdown

---

### **T — Tone**

**Technical, concise, code-focused.** Output should be production-ready with minimal comments (only WHY, not WHAT). Documentation is clear and comprehensive. Error messages are specific and actionable.

---

## Implementation Constraints

- **Zero test interdependencies:** Each test is isolated and can run in any order
- **No global state:** Use fixtures and dependency injection
- **Explicit over implicit:** Clear variable names, no abbreviations
- **Fail fast with clarity:** Detailed error messages on assertion failure
- **DRY principle:** Reuse common patterns through base classes and utilities
