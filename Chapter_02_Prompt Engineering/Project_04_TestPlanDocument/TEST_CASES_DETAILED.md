# Test Cases: RESTful Booker API

## Test Case Template

| **Field** | **Value** |
|-----------|----------|
| **Test Case ID** | TC_001 |
| **Test Case Name** | Create Booking with Valid Data |
| **Module** | Booking Management |
| **Priority** | P1 (High) |
| **Severity** | Critical |
| **Pre-conditions** | API is accessible; test data available |
| **Test Steps** | 1. Send POST request to /booking with valid booking data 2. Verify response status code |
| **Expected Result** | HTTP 200; Booking created successfully; Valid booking ID returned |
| **Actual Result** | |
| **Status** | Pass/Fail |
| **Executed By** | |
| **Execution Date** | |
| **Remarks** | |

---

## Functional Test Cases

### Authentication Tests

#### TC_001: Create Authentication Token - Valid Credentials
| Item | Details |
|------|---------|
| **Objective** | Verify auth token creation with valid credentials |
| **Pre-conditions** | API endpoint is accessible |
| **Test Data** | Username: admin, Password: password123 |
| **Steps** | 1. POST to /auth with valid credentials 2. Capture response |
| **Expected** | HTTP 200; Token generated in response |
| **Pass/Fail** | |

#### TC_002: Create Authentication Token - Invalid Credentials
| Item | Details |
|------|---------|
| **Objective** | Verify error handling for invalid credentials |
| **Test Data** | Invalid username/password combination |
| **Expected** | HTTP 200 with reason: "Bad credentials" |
| **Pass/Fail** | |

---

### Booking Creation Tests (POST /booking)

#### TC_003: Create Booking - All Valid Fields
| Item | Details |
|------|---------|
| **Objective** | Create booking with complete valid data |
| **Test Data** | First Name: John, Last Name: Doe, Total Price: 500, Deposit Paid: true, Check-in: 2026-06-01, Check-out: 2026-06-05, Breakfast: true |
| **Expected** | HTTP 200; Booking ID returned; Data stored correctly |
| **Pass/Fail** | |

#### TC_004: Create Booking - Missing Required Field
| Item | Details |
|------|---------|
| **Objective** | Verify error handling for missing required fields |
| **Test Data** | Missing "lastname" field |
| **Expected** | HTTP 400; Error message indicating missing field |
| **Pass/Fail** | |

#### TC_005: Create Booking - Invalid Date Format
| Item | Details |
|------|---------|
| **Objective** | Verify validation of date fields |
| **Test Data** | Check-in: "invalid-date" |
| **Expected** | HTTP 400; Error message for invalid date format |
| **Pass/Fail** | |

#### TC_006: Create Booking - Negative Price
| Item | Details |
|------|---------|
| **Objective** | Verify price validation (boundary test) |
| **Test Data** | Total Price: -100 |
| **Expected** | HTTP 400; Error rejecting negative price OR HTTP 200 accepting it (document behavior) |
| **Pass/Fail** | |

#### TC_007: Create Booking - Zero Price
| Item | Details |
|------|---------|
| **Objective** | Test boundary value for price field |
| **Test Data** | Total Price: 0 |
| **Expected** | HTTP 200 (system should accept) OR HTTP 400 (system should reject) |
| **Pass/Fail** | |

#### TC_008: Create Booking - Maximum Price
| Item | Details |
|------|---------|
| **Objective** | Test upper boundary for price |
| **Test Data** | Total Price: 999999.99 |
| **Expected** | HTTP 200; Booking created |
| **Pass/Fail** | |

#### TC_009: Create Booking - Empty Strings
| Item | Details |
|------|---------|
| **Objective** | Verify validation of empty string fields |
| **Test Data** | First Name: "", Last Name: "" |
| **Expected** | HTTP 400; Error indicating empty values not allowed |
| **Pass/Fail** | |

#### TC_010: Create Booking - Special Characters in Name
| Item | Details |
|------|---------|
| **Objective** | Test handling of special characters |
| **Test Data** | First Name: "John@#$%", Last Name: "Doe<script>" |
| **Expected** | HTTP 200 (accept as-is) OR HTTP 400 (reject special chars) |
| **Pass/Fail** | |

---

### Booking Retrieval Tests (GET /booking)

#### TC_011: Get All Bookings
| Item | Details |
|------|---------|
| **Objective** | Retrieve list of all bookings |
| **Pre-conditions** | At least one booking exists |
| **Expected** | HTTP 200; Array of booking IDs returned |
| **Pass/Fail** | |

#### TC_012: Get Booking by ID - Valid ID
| Item | Details |
|------|---------|
| **Objective** | Retrieve specific booking details |
| **Test Data** | Valid booking ID (e.g., 1) |
| **Expected** | HTTP 200; Complete booking details returned |
| **Pass/Fail** | |

#### TC_013: Get Booking by ID - Invalid ID
| Item | Details |
|------|---------|
| **Objective** | Verify error handling for non-existent booking |
| **Test Data** | Invalid booking ID: 999999 |
| **Expected** | HTTP 404; Error message or empty response |
| **Pass/Fail** | |

#### TC_014: Get Booking by ID - Non-Numeric ID
| Item | Details |
|------|---------|
| **Objective** | Verify handling of invalid ID format |
| **Test Data** | ID: "abc" or special characters |
| **Expected** | HTTP 400 or appropriate error |
| **Pass/Fail** | |

#### TC_015: Get Bookings with Filters - Valid Date Range
| Item | Details |
|------|---------|
| **Objective** | Test filtering by checkin/checkout dates |
| **Test Data** | checkin: 2026-05-01, checkout: 2026-06-30 |
| **Expected** | HTTP 200; Filtered booking results |
| **Pass/Fail** | |

#### TC_016: Get Bookings with Filters - Invalid Date Range
| Item | Details |
|------|---------|
| **Objective** | Test with checkout before checkin |
| **Test Data** | checkin: 2026-06-30, checkout: 2026-05-01 |
| **Expected** | HTTP 400 or empty results or specific error |
| **Pass/Fail** | |

---

### Booking Update Tests (PUT /booking/{id})

#### TC_017: Update Booking - Valid Data with Auth Token
| Item | Details |
|------|---------|
| **Objective** | Update booking with valid authentication |
| **Pre-conditions** | Valid booking ID exists; Auth token generated |
| **Test Data** | New First Name: "Jane" |
| **Expected** | HTTP 200; Booking updated successfully |
| **Pass/Fail** | |

#### TC_018: Update Booking - Without Auth Token
| Item | Details |
|------|---------|
| **Objective** | Verify authorization requirement |
| **Test Data** | No token provided |
| **Expected** | HTTP 403; Forbidden or auth required error |
| **Pass/Fail** | |

#### TC_019: Update Booking - Invalid Token
| Item | Details |
|------|---------|
| **Objective** | Test with expired/invalid token |
| **Test Data** | Token: "invalid-token-12345" |
| **Expected** | HTTP 401; Unauthorized error |
| **Pass/Fail** | |

#### TC_020: Update Booking - Non-Existent ID
| Item | Details |
|------|---------|
| **Objective** | Verify error handling for non-existent booking |
| **Test Data** | Booking ID: 999999 |
| **Expected** | HTTP 404; Not found error |
| **Pass/Fail** | |

#### TC_021: Update Booking - Invalid Data in Update
| Item | Details |
|------|---------|
| **Objective** | Verify validation during update |
| **Test Data** | Total Price: -50 |
| **Expected** | HTTP 400; Validation error |
| **Pass/Fail** | |

---

### Booking Deletion Tests (DELETE /booking/{id})

#### TC_022: Delete Booking - Valid ID with Auth Token
| Item | Details |
|------|---------|
| **Objective** | Successfully delete a booking |
| **Pre-conditions** | Valid booking ID; Auth token available |
| **Expected** | HTTP 201; Booking deleted |
| **Pass/Fail** | |

#### TC_023: Delete Booking - Without Auth Token
| Item | Details |
|------|---------|
| **Objective** | Verify authorization for delete |
| **Test Data** | No token |
| **Expected** | HTTP 403; Forbidden |
| **Pass/Fail** | |

#### TC_024: Delete Booking - Non-Existent ID
| Item | Details |
|------|---------|
| **Objective** | Test delete on non-existent booking |
| **Test Data** | ID: 999999 |
| **Expected** | HTTP 404; Not found |
| **Pass/Fail** | |

#### TC_025: Delete Booking - Already Deleted
| Item | Details |
|------|---------|
| **Objective** | Verify idempotency or error handling |
| **Pre-conditions** | Booking already deleted |
| **Expected** | HTTP 404 or HTTP 201 (API behavior) |
| **Pass/Fail** | |

---

### Security Tests

#### TC_026: SQL Injection - POST /booking
| Item | Details |
|------|---------|
| **Objective** | Test API resilience to SQL injection |
| **Test Data** | First Name: "'; DROP TABLE bookings; --" |
| **Expected** | HTTP 400; Input validated/sanitized |
| **Pass/Fail** | |

#### TC_027: XSS Attack - POST /booking
| Item | Details |
|------|---------|
| **Objective** | Verify protection against XSS |
| **Test Data** | First Name: "<script>alert('xss')</script>" |
| **Expected** | Input escaped/sanitized; HTTP 200 or 400 |
| **Pass/Fail** | |

#### TC_028: HTTPS Compliance
| Item | Details |
|------|---------|
| **Objective** | Verify secure data transmission |
| **Test Steps** | Verify endpoint uses HTTPS |
| **Expected** | All endpoints use HTTPS; No HTTP fallback |
| **Pass/Fail** | |

---

### Performance Tests

#### TC_029: Response Time - Create Booking
| Item | Details |
|------|---------|
| **Objective** | Verify response time for booking creation |
| **Expected** | < 500ms under normal load |
| **Actual Time** | |
| **Pass/Fail** | |

#### TC_030: Response Time - Get All Bookings
| Item | Details |
|------|---------|
| **Objective** | Measure retrieval performance |
| **Expected** | < 1000ms for retrieving all bookings |
| **Actual Time** | |
| **Pass/Fail** | |

#### TC_031: Concurrent Requests - 100 simultaneous creates
| Item | Details |
|------|---------|
| **Objective** | Test API under concurrent load |
| **Expected** | API remains stable; No errors; Response time < 2s |
| **Pass/Fail** | |

---

### Integration Tests

#### TC_032: Create → Read → Update Flow
| Item | Details |
|------|---------|
| **Objective** | Test end-to-end booking workflow |
| **Steps** | 1. Create booking 2. Read booking 3. Verify data integrity 4. Update booking 5. Verify update |
| **Expected** | All operations successful; Data consistent |
| **Pass/Fail** | |

#### TC_033: Create → Delete → Verify Removed
| Item | Details |
|------|---------|
| **Objective** | Verify booking is completely removed after deletion |
| **Steps** | 1. Create booking 2. Delete booking 3. Attempt to retrieve |
| **Expected** | GET returns 404 after deletion |
| **Pass/Fail** | |

---

### Regression Tests

#### TC_034: Verify Previous Bookings Unaffected
| Item | Details |
|------|---------|
| **Objective** | After new operations, existing bookings intact |
| **Expected** | All existing bookings retrievable; Data unchanged |
| **Pass/Fail** | |

---

## Test Execution Summary Template

| Test Case ID | Test Name | Status | Executed Date | Defects Found | Remarks |
|------|-----------|--------|---------------|---------------|---------|
| TC_001 | Create Token - Valid Credentials | Pass/Fail | | | |
| TC_002 | Create Token - Invalid Credentials | Pass/Fail | | | |
| TC_003 | Create Booking - Valid Data | Pass/Fail | | | |
| TC_004 | Create Booking - Missing Field | Pass/Fail | | | |
| ... | ... | ... | ... | ... | ... |

---

## Defect Log Template

| Defect ID | Test Case | Severity | Priority | Description | Steps to Reproduce | Expected vs Actual | Status | Assigned To | Date |
|-----------|-----------|----------|----------|-------------|-------------------|-------------------|--------|------------|------|
| DEF_001 | TC_003 | High | P1 | Booking price accepts negative values | Set price to -50 | Should reject negative, but accepts | Open | Dev Team | |
| | | | | | | | | | |

