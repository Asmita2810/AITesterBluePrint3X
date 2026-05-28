# Test Scenarios: RESTful Booker API

## Overview
Test scenarios outline the various business workflows and user journeys that need to be validated through the RESTful Booker API.

---

## Scenario 1: Basic Booking Workflow

### Description
A user creates, views, and modifies a hotel booking through the API.

### Pre-conditions
- API service is operational
- Database is accessible

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Get authentication token with valid credentials | HTTP 200; Token received |
| 2 | Create a new booking with valid data | HTTP 200; Booking ID generated |
| 3 | Retrieve the created booking using booking ID | HTTP 200; All booking details returned correctly |
| 4 | Update the booking details (e.g., check-out date) | HTTP 200; Booking updated |
| 5 | Retrieve booking again to verify update | HTTP 200; Updated details reflected |

### Expected Outcome
✅ Complete booking workflow executes without errors; All data persists correctly

---

## Scenario 2: Error Handling - Invalid Input

### Description
Testing API's behavior when invalid data is submitted.

### Pre-conditions
- API service is operational

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt to create booking with missing lastname | HTTP 400; Error message specifying missing field |
| 2 | Attempt to create booking with invalid date format | HTTP 400; Date validation error |
| 3 | Attempt to create booking with negative price | HTTP 400; Price validation error |
| 4 | Attempt to retrieve booking with invalid ID format | HTTP 400; ID format error OR HTTP 404 |

### Expected Outcome
✅ API validates all input and returns appropriate error codes

---

## Scenario 3: Authentication & Authorization

### Description
Verify that protected endpoints enforce authentication requirements.

### Pre-conditions
- API service is operational

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt to update booking without token | HTTP 403; Forbidden error |
| 2 | Attempt to delete booking without token | HTTP 403; Forbidden error |
| 3 | Generate valid token | HTTP 200; Token received |
| 4 | Update booking with valid token | HTTP 200; Booking updated |
| 5 | Delete booking with valid token | HTTP 201; Booking deleted |
| 6 | Attempt to update booking with expired/invalid token | HTTP 401; Unauthorized error |

### Expected Outcome
✅ Authentication properly enforced; Only authorized operations allowed

---

## Scenario 4: Concurrent Operations

### Description
Multiple users perform booking operations simultaneously.

### Pre-conditions
- API service is operational
- Test load generation tool available (JMeter, LoadRunner, etc.)

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Generate 50 concurrent create booking requests | All requests processed; HTTP 200 for all |
| 2 | Generate 50 concurrent read requests | All requests return correct data; HTTP 200 |
| 3 | Generate 50 concurrent update requests on same booking | Last update wins; Data consistency maintained |
| 4 | Monitor response times during concurrent load | Average response time < 1s |
| 5 | Monitor server resource utilization | CPU, Memory, DB connections within limits |

### Expected Outcome
✅ API handles concurrent requests without errors or data corruption

---

## Scenario 5: Data Boundary Testing

### Description
Test API behavior with boundary values for numeric and string fields.

### Pre-conditions
- API service is operational
- Test data prepared

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create booking with minimum price (0 or 1) | HTTP 200 or appropriate validation |
| 2 | Create booking with maximum price (999,999.99) | HTTP 200; Booking created |
| 3 | Create booking with very long firstname (1000+ chars) | HTTP 400 OR HTTP 200 with truncation |
| 4 | Create booking with single character firstname | HTTP 200; Booking created |
| 5 | Create booking with check-in date = check-out date | HTTP 200 OR HTTP 400 (document behavior) |

### Expected Outcome
✅ API handles boundary conditions gracefully per specification

---

## Scenario 6: Complete CRUD Lifecycle

### Description
Full lifecycle of a booking from creation to deletion.

### Pre-conditions
- API service is operational

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | **CREATE**: Generate token and create booking | HTTP 200; Booking ID returned (e.g., ID=123) |
| 2 | **READ**: Retrieve booking by ID | HTTP 200; Booking data matches input |
| 3 | **READ**: Get all bookings (verify ID 123 in list) | HTTP 200; ID 123 present in list |
| 4 | **UPDATE**: Modify booking details with token | HTTP 200; Specific fields updated |
| 5 | **READ**: Verify updates persisted | HTTP 200; Updated values reflected |
| 6 | **DELETE**: Delete booking with token | HTTP 201; Deletion confirmed |
| 7 | **READ**: Attempt to retrieve deleted booking | HTTP 404; Booking not found |

### Expected Outcome
✅ Complete lifecycle executes; Data persists through operations; Deletion successful

---

## Scenario 7: Performance Under Load

### Description
Evaluate API performance characteristics under sustained load.

### Pre-conditions
- Load generation tool available
- Performance monitoring tools active

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Establish baseline: 10 requests/second | Response time < 100ms; Success rate 100% |
| 2 | Increase to 50 requests/second | Response time < 500ms; Success rate 99%+ |
| 3 | Increase to 100 requests/second | Response time < 1000ms; Success rate 95%+ |
| 4 | Maintain 100 req/sec for 5 minutes | No degradation; Memory stable |
| 5 | Gradually decrease load to baseline | API returns to normal performance |

### Expected Outcome
✅ API maintains performance within acceptable thresholds under sustained load

---

## Scenario 8: Security Validation

### Description
Test API resilience to common security threats.

### Pre-conditions
- API service is operational
- Security testing tools available

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt SQL injection in firstname field | Input sanitized; HTTP 400 or HTTP 200 with escaped content |
| 2 | Attempt XSS attack in lastname field | Payload escaped/sanitized; No execution |
| 3 | Verify HTTPS is enforced | All endpoints use HTTPS; HTTP redirects to HTTPS |
| 4 | Test auth token isolation | Token from user A cannot access/modify user B's bookings |
| 5 | Verify sensitive data not logged | Check logs for exposed passwords/tokens |

### Expected Outcome
✅ API properly protects against common security threats

---

## Scenario 9: Data Consistency Across Operations

### Description
Verify data integrity when performing multiple operations.

### Pre-conditions
- API service is operational

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create booking (Booking A) | HTTP 200; ID = A1 |
| 2 | Create booking (Booking B) | HTTP 200; ID = B1 |
| 3 | Update Booking A | HTTP 200; A1 updated |
| 4 | Retrieve Booking A | Data shows updates from step 3 |
| 5 | Retrieve Booking B | Data unchanged from step 2 |
| 6 | Delete Booking A | HTTP 201; A1 deleted |
| 7 | Get all bookings | Returns B1 but not A1 |

### Expected Outcome
✅ Operations are isolated; Data consistency maintained; No cross-contamination

---

## Scenario 10: Error Recovery

### Description
Test API's ability to recover from errors and maintain data integrity.

### Pre-conditions
- API service is operational

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Send invalid request (malformed JSON) | HTTP 400; Error response; API still operational |
| 2 | Send another valid request after error | HTTP 200; Request processes normally |
| 3 | Simulate timeout scenario | Request times out; Booking not created or marked pending |
| 4 | Retry same operation | Idempotent behavior OR appropriate error handling |
| 5 | Verify booking status | Consistent state; No duplicate bookings |

### Expected Outcome
✅ API recovers gracefully; No data corruption; Maintains consistency

---

## Scenario 11: Filter & Search Operations

### Description
Test API's ability to filter and search bookings by various criteria.

### Pre-conditions
- Multiple bookings exist in system
- Test data covers different date ranges and guest names

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Get all bookings without filters | HTTP 200; All booking IDs returned |
| 2 | Get bookings with checkin date filter | HTTP 200; Only matching bookings returned |
| 3 | Get bookings with checkout date filter | HTTP 200; Only matching bookings returned |
| 4 | Get bookings with date range filter | HTTP 200; Bookings within range returned |
| 5 | Get bookings with invalid date range | HTTP 400 OR empty results (document behavior) |

### Expected Outcome
✅ Filter operations work correctly; Return accurate subsets of data

---

## Scenario 12: API Documentation Accuracy

### Description
Verify that actual API behavior matches documented behavior.

### Pre-conditions
- API documentation available
- Test cases prepared

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Review API documentation for endpoint specifications | Document should list all endpoints |
| 2 | Test each documented endpoint | All endpoints operational per documentation |
| 3 | Verify request/response format matches docs | Schema aligns with documented structure |
| 4 | Test error codes match documentation | Errors align with documented error responses |
| 5 | Verify auth requirements per docs | Authentication enforced as documented |

### Expected Outcome
✅ API behavior matches documentation; No discrepancies found

---

## Scenario 13: Regression Testing - After Bug Fix

### Description
Ensure that bug fixes don't introduce regressions.

### Pre-conditions
- Bug fix deployed
- Original passing test cases identified

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Execute all original PASSING test cases | All tests still pass; No regressions |
| 2 | Execute test case for fixed bug | Now passes (bug is fixed) |
| 3 | Verify related functionality | No collateral damage to related features |
| 4 | Run performance tests | No degradation in response times |

### Expected Outcome
✅ Bug is fixed; No regressions introduced; System stable

---

## Scenario 14: Edge Case - Boundary Dates

### Description
Test API behavior with extreme and boundary date values.

### Pre-conditions
- API service is operational

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create booking with checkin = today | HTTP 200; Booking created |
| 2 | Create booking with checkin = past date (e.g., 2020-01-01) | HTTP 200 OR HTTP 400 (depending on business rules) |
| 3 | Create booking with checkin = far future (e.g., 2099-12-31) | HTTP 200; Booking created |
| 4 | Create booking with same checkin/checkout date | HTTP 200 OR HTTP 400 (depending on business rules) |
| 5 | Create booking with checkout before checkin | HTTP 400; Invalid date range error |

### Expected Outcome
✅ Date validation works correctly per business requirements

---

## Scenario 15: Stress Test - High Volume

### Description
Push API to its limits with maximum concurrent users and requests.

### Pre-conditions
- Load testing tool available
- Performance monitoring active
- Database backup in place

### Test Flow

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Simulate 500 concurrent users | API remains responsive; Errors < 1% |
| 2 | Simulate 1000 concurrent users | API remains stable; Acceptable degradation |
| 3 | Simulate 5000 concurrent requests/minute | System doesn't crash; Graceful degradation |
| 4 | Monitor resource utilization | CPU, Memory, I/O within limits |
| 5 | Gradually reduce load and monitor recovery | API returns to normal state |

### Expected Outcome
✅ API withstands high load; Fails gracefully under extreme stress

---

## Test Scenario Execution Checklist

- [ ] Scenario 1: Basic Booking Workflow
- [ ] Scenario 2: Error Handling
- [ ] Scenario 3: Authentication & Authorization
- [ ] Scenario 4: Concurrent Operations
- [ ] Scenario 5: Boundary Testing
- [ ] Scenario 6: Complete CRUD Lifecycle
- [ ] Scenario 7: Performance Under Load
- [ ] Scenario 8: Security Validation
- [ ] Scenario 9: Data Consistency
- [ ] Scenario 10: Error Recovery
- [ ] Scenario 11: Filter & Search
- [ ] Scenario 12: API Documentation
- [ ] Scenario 13: Regression Testing
- [ ] Scenario 14: Edge Case - Dates
- [ ] Scenario 15: Stress Test

---

## Notes
- Scenarios should be executed in order when possible to maintain test data consistency
- Failed scenarios should be investigated before proceeding to dependent scenarios
- Performance baselines from Scenario 7 should be used as reference for Scenario 15
- All defects found should be logged with scenario ID and step number

