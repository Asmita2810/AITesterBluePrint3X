# REST Assured Python Framework - Execution Guide

> Step-by-step guide to execute, debug, and extend the REST API testing framework

---

## 🎬 Getting Started - First Run

### Step 1: Verify Installation
```bash
cd RestAssuredPython
python --version              # Verify Python 3.8+
pip list | grep pytest        # Verify pytest installed
```

### Step 2: Run Health Check
```bash
pytest tests/test_booking_api.py::TestBookingAPI::test_tc001_health_check_success -v
```

Expected Output:
```
test_tc001_health_check_success PASSED
[ASSERTION 2] Status code assertion passed: 201
[ASSERTION 3] Header exists assertion passed: Server
```

### Step 3: Full Test Run
```bash
pytest -v
```

This will:
- Execute all 12 test cases
- Generate log file in `logs/`
- Generate HTML report in `reports/`

---

## 📋 Test Execution Scenarios

### Scenario 1: Smoke Testing (Quick Verification)
```bash
# Run only smoke tests
pytest -m smoke -v

# Expected: 6 tests pass (TC-001 through TC-006)
# Duration: ~5 seconds
```

### Scenario 2: Full Regression Suite
```bash
# Run all tests except slow tests
pytest -m "not slow" -v

# Expected: 11 tests pass
# Duration: ~15 seconds
```

### Scenario 3: Negative Testing (Error Handling)
```bash
# Run only negative tests
pytest -m negative -v

# Expected: 4 tests pass (TC-007 through TC-010)
# Verify error handling works correctly
```

### Scenario 4: Performance Testing
```bash
# Run performance tests
pytest -m slow -v

# Expected: 1 test (TC-011)
# Verifies API response time meets SLA
```

### Scenario 5: Single Feature Testing
```bash
# Test booking creation feature
pytest -k "create_booking" -v

# Matches: TC-003, TC-008, TC-009, TC-010
```

### Scenario 6: Continuous Integration
```bash
# Full run with HTML report
pytest --html=reports/report.html --self-contained-html -v

# Generates: reports/report.html
# Can be published to CI/CD pipeline
```

---

## 🔍 Debugging Failed Tests

### Debug Scenario 1: Test Fails - Check Why
```bash
# Run with verbose output and print statements
pytest tests/test_booking_api.py::TestBookingAPI::test_tc003_create_booking_valid_data -v -s

# This shows:
# - Printed output from test
# - Request/response details
# - Assertion messages
```

### Debug Scenario 2: Connection Issues
```bash
# Enable debug logging
LOG_LEVEL=DEBUG pytest -v -s

# Check logs for request details
tail -100 logs/api_test_*.log
```

### Debug Scenario 3: Test Takes Too Long
```bash
# Run with timeout and show execution time
pytest -v --durations=10

# Shows slowest 10 tests
# Check REQUEST_TIMEOUT in .env if hanging
```

### Debug Scenario 4: Assertion Mismatch
```bash
# Run with full traceback
pytest -v --tb=long tests/test_booking_api.py::TestBookingAPI::test_tc005_update_booking_valid_data

# Shows full assertion error with context
```

---

## 📊 Reporting & Analysis

### Generate HTML Report
```bash
# Standard report
pytest --html=reports/report.html

# Self-contained HTML (can be emailed)
pytest --html=reports/report.html --self-contained-html

# With self-contained images
pytest --html=reports/report.html --self-contained-html --html-report=reports/
```

### Analyze Test Results
```bash
# Show test summary
pytest -v --tb=no

# Count passes and failures
pytest -v | grep -c PASSED
pytest -v | grep -c FAILED

# Show only failed tests
pytest -v -lf

# Rerun only failed tests
pytest -v --lf
```

### Review Execution Logs
```bash
# View latest log file
tail -f logs/api_test_*.log

# Search for errors
grep ERROR logs/api_test_*.log

# Count assertions per test
grep "ASSERTION" logs/api_test_*.log | wc -l

# View specific test execution
grep "TEST START: test_tc003" -A 50 logs/api_test_*.log
```

---

## 🛠️ Custom Test Execution

### Execute Custom Test Case
```bash
# Create new test in tests/test_custom.py
# (See template below)

# Run it
pytest tests/test_custom.py -v
```

### Custom Test Template
```python
import pytest
from src.config.client import APIClient
from src.assertions.assertions import RestAssertions
from src.data.test_data_factory import TestDataFactory
from src.endpoints.endpoints import APIEndpoints
from src.config.logger import LoggerSetup

logger = LoggerSetup.get_logger(__name__)

class TestCustomScenarios:
    
    @pytest.mark.smoke
    def test_tc999_my_custom_test(self, api_client):
        """
        TC-999: My custom test scenario
        Scenario: Custom Test | Priority: High | Type: Smoke
        """
        # Arrange
        payload = TestDataFactory.create_booking_payload()
        
        # Act
        response = api_client.post(APIEndpoints.BOOKINGS, json=payload)
        
        # Assert
        assertions = RestAssertions(response)
        assertions.status_code(200).body_contains("bookingid")
        
        logger.info(f"✓ TC-999 passed")
```

### Run Custom Test
```bash
pytest tests/test_custom.py::TestCustomScenarios::test_tc999_my_custom_test -v
```

---

## 🔗 Test Chaining & Workflows

### Scenario: Create → Read → Update → Delete

```python
def test_workflow_complete_booking_lifecycle(api_client):
    """Full booking lifecycle workflow"""
    
    # Step 1: Create
    create_payload = TestDataFactory.create_booking_payload()
    create_resp = api_client.post(APIEndpoints.BOOKINGS, json=create_payload)
    booking_id = create_resp.json()["bookingid"]
    
    # Step 2: Read
    read_resp = api_client.get(APIEndpoints.BOOKING_BY_ID.format(id=booking_id))
    RestAssertions(read_resp).status_code(200)
    
    # Step 3: Update
    update_payload = TestDataFactory.create_booking_payload(firstname="Updated")
    update_resp = api_client.put(
        APIEndpoints.BOOKING_BY_ID.format(id=booking_id),
        json=update_payload,
        headers={"Cookie": "token=test"}
    )
    RestAssertions(update_resp).body_path("firstname", "Updated")
    
    # Step 4: Delete
    delete_resp = api_client.delete(
        APIEndpoints.BOOKING_BY_ID.format(id=booking_id),
        headers={"Cookie": "token=test"}
    )
    RestAssertions(delete_resp).status_code(201)
    
    logger.info("✓ Complete workflow passed")
```

---

## 📈 Parallel Execution

### Install Pytest-xdist
```bash
pip install pytest-xdist
```

### Run Tests in Parallel
```bash
# Run with 4 workers
pytest -n 4 -v

# Auto-detect worker count
pytest -n auto -v

# Distribute by test class
pytest -n auto --dist=loadgroup -v
```

### Expected Performance
```
Sequential: ~18 seconds
Parallel (4 workers): ~8 seconds
Speedup: ~2.25x
```

---

## 🔐 Running with Different Configurations

### Configuration 1: Local Development
```bash
# .env
BASE_URL=http://localhost:3000
VERIFY_SSL=false
LOG_LEVEL=DEBUG
REQUEST_TIMEOUT=60
```

### Configuration 2: Staging Environment
```bash
# .env
BASE_URL=https://staging-api.example.com
VERIFY_SSL=true
LOG_LEVEL=INFO
REQUEST_TIMEOUT=30
AUTH_ENABLED=true
AUTH_TYPE=bearer
AUTH_TOKEN=staging_token_xyz
```

### Configuration 3: Production Monitoring
```bash
# .env
BASE_URL=https://api.example.com
VERIFY_SSL=true
LOG_LEVEL=WARNING
REQUEST_TIMEOUT=20
RETRY_COUNT=3
RETRY_DELAY=2
```

### Switch Configurations
```bash
# Local
cp .env.local .env
pytest -v

# Staging
cp .env.staging .env
pytest -v

# Production
cp .env.prod .env
pytest -v
```

---

## 🎯 Continuous Integration Setup

### GitHub Actions Example
```yaml
name: API Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - run: pip install -r RestAssuredPython/requirements.txt
      - run: |
          cd RestAssuredPython
          pytest -v --html=reports/report.html
      - uses: actions/upload-artifact@v3
        if: always()
        with:
          name: test-report
          path: RestAssuredPython/reports/
```

### GitLab CI Example
```yaml
api_tests:
  image: python:3.10
  script:
    - cd RestAssuredPython
    - pip install -r requirements.txt
    - pytest -v --html=reports/report.html
  artifacts:
    paths:
      - RestAssuredPython/reports/
    when: always
```

### Jenkins Example
```groovy
pipeline {
    agent any
    stages {
        stage('Setup') {
            steps {
                sh 'pip install -r RestAssuredPython/requirements.txt'
            }
        }
        stage('Test') {
            steps {
                dir('RestAssuredPython') {
                    sh 'pytest -v --html=reports/report.html'
                }
            }
        }
    }
    post {
        always {
            publishHTML([
                reportDir: 'RestAssuredPython/reports',
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ])
        }
    }
}
```

---

## 📊 Test Metrics & KPIs

### Key Metrics
```bash
# Test execution time
pytest -v --durations=0

# Test coverage (if implemented)
pytest --cov=src

# Test failure rate
pytest -v | awk '/FAILED/ {print}'

# Average response time (from logs)
grep "Response time" logs/api_test_*.log | awk '{sum+=$NF; count++} END {print sum/count}'
```

### Generate Report Summary
```bash
# Create metrics report
pytest -v --tb=no > test_results.txt
echo "Tests run: $(grep -c '::test_' test_results.txt)"
echo "Passed: $(grep -c PASSED test_results.txt)"
echo "Failed: $(grep -c FAILED test_results.txt)"
```

---

## ✅ Pre-Commit Checklist

Before committing test changes:

```bash
# 1. Run full test suite
pytest -v

# 2. Check for lint issues
pip install pylint
pylint src/ tests/

# 3. Verify no hard-coded secrets
grep -r "password\|token\|secret" tests/ src/ | grep -v ".pyc"

# 4. Ensure logs are in .gitignore
grep "logs/" .gitignore

# 5. Verify test count
pytest --collect-only | grep "test session" 
```

---

## 🚀 Quick Command Reference

```bash
# Setup
pip install -r requirements.txt

# Run all tests
pytest -v

# Run with report
pytest --html=reports/report.html

# Smoke tests only
pytest -m smoke -v

# Negative tests
pytest -m negative -v

# Single test
pytest tests/test_booking_api.py::TestBookingAPI::test_tc001_health_check_success -v

# Debug mode
pytest -v -s --tb=long

# Stop on failure
pytest -x

# Show slowest tests
pytest --durations=5

# Parallel execution
pytest -n 4 -v

# View latest logs
tail -100 logs/api_test_*.log
```

---

**Ready to execute tests! 🚀**
