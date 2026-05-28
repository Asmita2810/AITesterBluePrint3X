# Test Plan: RESTful Booker API

**Document Version:** 1.0  
**Last Updated:** 2026-05-28  
**API URL:** https://restful-booker.herokuapp.com/apidoc/index.html

---

## Table of Contents
1. [Objective](#objective)
2. [Scope](#scope)
3. [Test Environments](#test-environments)
4. [Test Strategy](#test-strategy)
5. [Test Schedule](#test-schedule)
6. [Entry and Exit Criteria](#entry-and-exit-criteria)
7. [Test Deliverables](#test-deliverables)
8. [Defect Reporting Procedure](#defect-reporting-procedure)
9. [Tools and Resources](#tools-and-resources)
10. [Risks and Mitigations](#risks-and-mitigations)

---

## Objective

The objective of this test plan is to verify the **RESTful Booker API**, covering:
- Booking creation, modification, and deletion operations
- Authentication and authorization mechanisms
- Identification and documentation of all existing bugs
- Manual testing via Postman
- Automated testing using REST Assured framework

---

## Scope

### In-Scope Testing

#### 1. **Functional Testing**
- Verify correctness and functionality of all API endpoints per documentation
- Test booking creation, modification, and cancellation scenarios
- Validate user authentication and authorization for protected endpoints

#### 2. **Data Validation Testing**
- Validate proper rejection of invalid input data
- Test boundary values for input fields
- Verify accuracy of data returned in responses

#### 3. **Error Handling Testing**
- Verify appropriate error codes and messages for invalid requests
- Check for sensitive information disclosure in error responses
- Validate graceful error handling for unexpected scenarios

#### 4. **Performance Testing**
- Assess response time under normal and peak loads
- Measure API throughput and scalability
- Identify performance bottlenecks

#### 5. **Security Testing**
- Conduct security assessments (SQL injection, XSS, etc.)
- Validate HTTPS compliance
- Verify proper access controls and authorization

#### 6. **Integration Testing**
- Verify interactions between different API endpoints
- Test data consistency across related endpoints

#### 7. **Compatibility Testing**
- Test API on different OS, browsers, and devices

#### 8. **Load & Concurrency Testing**
- Evaluate API behavior under high concurrent user loads
- Test concurrent CRUD operations

#### 9. **Edge Case Testing**
- Test extreme and boundary scenarios

#### 10. **Regression Testing**
- Ensure existing functionality remains intact after bug fixes

### CRUD Operations Coverage

#### **Create (POST) Operations**
- [ ] Create new bookings with valid input data
- [ ] Return appropriate error responses for invalid/missing data
- [ ] Verify correct storage of newly created bookings

#### **Read (GET) Operations**
- [ ] Retrieve booking information by various criteria (ID, date range, guest name)
- [ ] Return correct data in response
- [ ] Handle non-existent or invalid booking IDs

#### **Update (PUT) Operations**
- [ ] Update existing bookings with valid data
- [ ] Reject invalid update requests with appropriate errors
- [ ] Verify correct modification of booking data

#### **Delete (DELETE) Operations**
- [ ] Delete bookings by valid booking IDs
- [ ] Return appropriate responses after successful deletion
- [ ] Verify removal of deleted bookings

---

## Test Environments

### Operating Systems
- Windows 10 (Chrome, Firefox, Edge)
- macOS (Safari)
- Android (Chrome)
- iPhone (Safari)

### API Test Environments
| Environment | URL |
|-------------|-----|
| QA | https://restful-booker.herokuapp.com/apidoc/index.html |
| Pre-Prod | https://restful-booker.herokuapp.com/apidoc/index.html |

### Hardware & Software Requirements
- Processor: 2GHz or higher
- Memory: 4GB RAM minimum
- Storage: 100MB available space
- Network: Wi-Fi, cellular, or wired connection

### Authentication & Access
- API uses token-based authentication
- Tokens required for PUT and DELETE operations
- Username: `admin`
- Password: `password123`

---

## Test Strategy

### Test Design Techniques
- **Equivalence Class Partition** - Group inputs into classes
- **Boundary Value Analysis** - Test boundary conditions
- **Decision Table Testing** - Test decision logic
- **State Transition Testing** - Test state changes
- **Use Case Testing** - Test real-world scenarios
- **Error Guessing** - Anticipate potential errors
- **Exploratory Testing** - Ad-hoc testing based on expertise

### Test Execution Phases

#### **Phase 1: Smoke Testing**
- Verify critical functionalities are working
- Reject build if smoke testing fails
- Wait for stable build before proceeding

#### **Phase 2: In-Depth Testing**
- Execute comprehensive test cases
- Test on multiple supported environments simultaneously
- Perform all testing types (functional, data validation, error handling, etc.)

#### **Phase 3: Reporting & Iteration**
- Report bugs in JIRA with reproduction steps
- Send daily status reports
- Repeat test cycles until quality product is achieved

### Testing Types to Perform
- Smoke and Sanity Testing
- Regression Testing and Retesting
- Usability and Functionality Testing
- UI Testing
- End-to-End Flow Testing

### Best Practices
- **Context-Driven Testing** - Perform testing per application context
- **Shift Left Testing** - Start testing from early development stages
- **Exploratory Testing** - Beyond standard test case execution
- **End-to-End Testing** - Multi-functionality user flow simulation

---

## Test Schedule

| Task | Duration | Status |
|------|----------|--------|
| Creating Test Plan | - | |
| Test Case Creation | - | |
| Test Case Execution | - | |
| Summary Reports Submission | - | |

**Total Timeline:** 2 Sprints

---

## Entry and Exit Criteria

### Requirement Analysis Phase

**Entry Criteria:**
- Testing team receives Requirements Documents

**Exit Criteria:**
- Requirements explored and understood
- All doubts clarified

### Test Execution Phase

**Entry Criteria:**
- Test Scenarios and Test Cases signed-off by Client
- Application ready for testing

**Exit Criteria:**
- Test Case Reports and Defect Reports ready

### Test Closure Phase

**Entry Criteria:**
- Test Case Reports and Defect Reports completed

**Exit Criteria:**
- Test Summary Reports finalized

---

## Test Deliverables

| Deliverable | Description | Target Date |
|-------------|-------------|-------------|
| **Test Plan** | Scope, strategy, schedule, resources, deliverables | TBD |
| **Functional Test Cases** | Test cases for defined scope | TBD |
| **Defect Reports** | Detailed description of defects with screenshots and reproduction steps (daily basis) | Ongoing |
| **Summary Reports** | Bugs by ID, Functional Area, and Priority | TBD |

---

## Defect Reporting Procedure

### Defect Identification Criteria
- Deviation from requirements
- User experience issues
- Technical errors
- Unexpected behavior

### Defect Reporting Steps
1. Use designated defect template
2. Provide detailed reproduction steps
3. Attach screenshots or logs
4. Document expected vs. actual behavior

### Defect Triage & Prioritization
- Assign severity levels (Critical, High, Medium, Low)
- Assign priority levels (P0, P1, P2, P3)
- Route to appropriate team members

### Defect Tracking Tool
- **Tool Used:** JIRA

### Defect Process Points of Contact (POC)

| Area | POC |
|------|-----|
| New Frontend | Devesh |
| Backend | Sonal |
| DevOps | Prajeeth |

### Metrics
- Number of defects found
- Time to resolve defects
- Percentage of successfully fixed defects

---

## Tools and Resources

### Testing Tools
- **JIRA** - Bug tracking and defect management
- **Mind Map Tool** - Test planning and organization
- **Postman** - Manual API testing
- **REST Assured Framework** - Automated API testing
- **Snipping Tool** - Screenshot capture for bug reports
- **Excel/Word** - Documentation and reporting

### Team Roles & Responsibilities
- **QA Lead** - Test planning, coordination, reporting
- **QA Testers** - Test case creation and execution
- **Developers** - Bug investigation and fixes
- **DevOps** - Environment setup and maintenance

---

## Risks and Mitigations

| Risk | Mitigation Strategy |
|------|-------------------|
| **Non-Availability of Resource** | Maintain backup resource planning |
| **Build URL Not Working** | Resources pivot to other tasks; escalate to DevOps |
| **Less Time for Testing** | Dynamically ramp up resources based on client needs |
| **Test Environment Issues** | Maintain pre-configured environments; have fallback environments |
| **Scope Creep** | Maintain strict scope control; document all change requests |
| **External API Dependency** | Mock external dependencies if needed; plan contingencies |

---

## Approvals

The following documents require client approval before proceeding to next phase:
- [ ] Test Plan
- [ ] Test Scenarios
- [ ] Test Cases
- [ ] Defect Reports
- [ ] Summary Reports

**Testing will only proceed to the next phase once approvals are obtained.**

---

## Appendix: API Endpoints Summary

### Authentication
- **POST /auth** - Create authentication token
- Credentials: `admin` / `password123`

### Booking Management
- **POST /booking** - Create new booking
- **GET /booking** - Get all bookings (with optional filters)
- **GET /booking/{id}** - Get specific booking details
- **PUT /booking/{id}** - Update booking (requires auth token)
- **DELETE /booking/{id}** - Delete booking (requires auth token)

### Health Check
- **GET /ping** - API health check

---

**Document Sign-off:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Lead | | | |
| Project Manager | | | |
| Client Approver | | | |

