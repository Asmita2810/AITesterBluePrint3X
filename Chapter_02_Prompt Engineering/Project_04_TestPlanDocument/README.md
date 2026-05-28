# RESTful Booker API - Test Planning Documentation Index

**Project:** RESTful Booker API Testing  
**Date Created:** 2026-05-28  
**API URL:** https://restful-booker.herokuapp.com/apidoc/index.html

---

## 📋 Documentation Overview

This folder contains comprehensive test planning documentation for the RESTful Booker API project.

### 📁 Files in This Package

| Document | Purpose | Key Contents |
|----------|---------|--------------|
| **TEST_PLAN_RESTFUL_BOOKER_API.md** | Master test plan document | Objectives, scope, strategy, schedule, entry/exit criteria, risks, tools |
| **TEST_CASES_DETAILED.md** | Comprehensive test case library | 34+ detailed test cases covering all CRUD operations, security, performance |
| **TEST_SCENARIOS.md** | Business workflow scenarios | 15 complete end-to-end test scenarios with step-by-step flows |
| **README.md** | This file | Documentation index and quick reference guide |

---

## 🎯 Quick Start

### For QA Lead/Manager
1. Start with **TEST_PLAN_RESTFUL_BOOKER_API.md**
2. Review test strategy and schedule
3. Use risks & mitigations section for stakeholder communication

### For Test Engineers
1. Review **TEST_SCENARIOS.md** for business context
2. Use **TEST_CASES_DETAILED.md** for specific test execution
3. Reference test strategy in main plan for design techniques

### For Automation Engineers
1. Review **TEST_CASES_DETAILED.md** for test case specifications
2. Use REST Assured framework details from main plan
3. Create automated test scripts based on test case steps

### For Developers/DevOps
1. Check **TEST_PLAN_RESTFUL_BOOKER_API.md** for environment setup
2. Review defect reporting procedure
3. Check Risks & Mitigations section for infrastructure concerns

---

## 📊 Test Coverage Summary

### Testing Types Included
- ✅ Functional Testing
- ✅ Data Validation Testing
- ✅ Error Handling Testing
- ✅ Security Testing
- ✅ Performance Testing
- ✅ Integration Testing
- ✅ Concurrency Testing
- ✅ Boundary Testing
- ✅ Regression Testing
- ✅ Ad-hoc/Exploratory Testing

### API Endpoints Covered
- ✅ Authentication (POST /auth)
- ✅ Create Booking (POST /booking)
- ✅ Retrieve Bookings (GET /booking)
- ✅ Retrieve Booking Details (GET /booking/{id})
- ✅ Update Booking (PUT /booking/{id})
- ✅ Delete Booking (DELETE /booking/{id})
- ✅ Health Check (GET /ping)

### Test Cases by Category

| Category | Count | Reference |
|----------|-------|-----------|
| Authentication | 2 | TC_001, TC_002 |
| Booking Creation | 8 | TC_003 - TC_010 |
| Booking Retrieval | 6 | TC_011 - TC_016 |
| Booking Update | 5 | TC_017 - TC_021 |
| Booking Deletion | 4 | TC_022 - TC_025 |
| Security | 3 | TC_026 - TC_028 |
| Performance | 3 | TC_029 - TC_031 |
| Integration | 2 | TC_032 - TC_033 |
| Regression | 1 | TC_034 |
| **Total** | **34+** | |

### Test Scenarios by Type

| Scenario | Focus Area |
|----------|-----------|
| Scenario 1 | Basic booking workflow |
| Scenario 2 | Error handling |
| Scenario 3 | Authentication & authorization |
| Scenario 4 | Concurrent operations |
| Scenario 5 | Data boundary testing |
| Scenario 6 | Complete CRUD lifecycle |
| Scenario 7 | Performance under load |
| Scenario 8 | Security validation |
| Scenario 9 | Data consistency |
| Scenario 10 | Error recovery |
| Scenario 11 | Filter & search operations |
| Scenario 12 | API documentation accuracy |
| Scenario 13 | Regression testing |
| Scenario 14 | Edge case - boundary dates |
| Scenario 15 | Stress testing |

---

## 🔑 Key Information

### Test Timeline
- **Total Duration:** 2 Sprints
- **Test Environment:** QA and Pre-Prod
- **Test Deliverables:** Test Plan, Test Cases, Defect Reports, Summary Reports

### Tools Required
| Tool | Purpose |
|------|---------|
| JIRA | Bug tracking and defect management |
| Postman | Manual API testing |
| REST Assured | Automated API testing (Java framework) |
| JMeter/LoadRunner | Performance and load testing |
| Mind Map Tool | Test planning and organization |

### Team Roles

| Role | Responsibility | POC |
|------|-----------------|-----|
| QA Lead | Test planning, coordination, reporting | - |
| QA Engineers | Test case creation and execution | - |
| Developers | Bug investigation and fixes | Sonal (Backend) |
| DevOps | Environment setup | Prajeeth |
| Frontend | Frontend component issues | Devesh |

### Authentication Credentials
- **Username:** admin
- **Password:** password123
- **Note:** Required for PUT and DELETE operations

### Test Environments
| Environment | URL |
|-------------|-----|
| QA | https://restful-booker.herokuapp.com/apidoc/index.html |
| Pre-Prod | https://restful-booker.herokuapp.com/apidoc/index.html |

---

## 📝 Test Case ID Reference

### Quick Lookup
- **TC_001-002:** Authentication
- **TC_003-010:** Create operations
- **TC_011-016:** Read operations
- **TC_017-021:** Update operations
- **TC_022-025:** Delete operations
- **TC_026-028:** Security tests
- **TC_029-031:** Performance tests
- **TC_032-033:** Integration tests
- **TC_034+:** Regression tests

---

## ✅ Execution Checklist

### Pre-Testing
- [ ] Review test plan with team
- [ ] Confirm test environment access
- [ ] Generate API authentication tokens
- [ ] Prepare test data
- [ ] Set up test reporting tools

### During Testing
- [ ] Execute smoke tests first (Scenario 1)
- [ ] Log all defects with reproduction steps
- [ ] Update test execution tracking
- [ ] Send daily status reports
- [ ] Monitor performance metrics

### Post-Testing
- [ ] Compile test summary report
- [ ] Document lessons learned
- [ ] Archive all test artifacts
- [ ] Update test plan for next iteration

---

## 📈 Defect Management

### Severity Levels
- **Critical:** Complete feature failure, data loss, security issue
- **High:** Major functionality broken, significant impact
- **Medium:** Minor feature issue, workaround available
- **Low:** Cosmetic issue, minimal impact

### Priority Levels
- **P0:** Fix immediately
- **P1:** Fix before release
- **P2:** Fix in next sprint
- **P3:** Fix when resources available

### Defect Process
1. Identify defect during testing
2. Create detailed reproduction steps
3. Capture screenshots/logs
4. File JIRA ticket with assigned POC
5. Track resolution status
6. Retest after fix applied
7. Close defect ticket

### Defect Contacts
| Area | Contact |
|------|---------|
| Backend Issues | Sonal |
| Frontend Issues | Devesh |
| Infrastructure Issues | Prajeeth |

---

## 🔍 Test Design Techniques Used

The following industry-standard test design techniques are employed:

1. **Equivalence Class Partitioning** - Group inputs into valid/invalid classes
2. **Boundary Value Analysis** - Test minimum, maximum, and edge values
3. **Decision Table Testing** - Test logical decision paths
4. **State Transition Testing** - Test state changes and transitions
5. **Use Case Testing** - Real-world user scenarios
6. **Error Guessing** - Anticipate likely errors
7. **Exploratory Testing** - Ad-hoc testing based on expertise

---

## 📱 Test Environments Coverage

### Operating Systems
- Windows 10 (Chrome, Firefox, Edge)
- macOS (Safari)
- Android (Chrome)
- iOS (Safari)

### Network Conditions
- Wi-Fi (broadband)
- Cellular (LTE/4G)
- Wired (enterprise network)

---

## 🚨 Key Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Resource unavailability | Backup resource planning |
| Build/API not accessible | Alternative test tasks; infrastructure escalation |
| Time constraints | Resource scaling per requirements |
| Environment issues | Pre-configured test environments |
| Scope creep | Strict scope control and documentation |

---

## 📊 Metrics to Track

1. **Test Execution Rate**
   - Test cases executed per day
   - Target: 5-10 test cases per resource per day

2. **Defect Discovery Rate**
   - Defects found per test case
   - Defects by severity level

3. **Defect Resolution Rate**
   - Defects resolved vs. open
   - Average time to fix

4. **Test Effectiveness**
   - Defects found during testing vs. production
   - Test case pass/fail ratio

5. **Coverage Metrics**
   - API endpoints covered
   - Business scenarios covered
   - Code coverage (for automated tests)

---

## 🔗 Dependencies & Prerequisites

### Pre-Testing Setup
- [ ] API endpoint must be accessible
- [ ] Authentication service must be operational
- [ ] Database must be available and initialized
- [ ] Test data must be prepared
- [ ] All team members must have access credentials

### Tools Installation
- [ ] Postman installed (for manual testing)
- [ ] Java 8+ installed (for REST Assured)
- [ ] JIRA access configured
- [ ] Performance testing tools available (optional but recommended)

---

## 📞 Escalation Contacts

| Issue | Contact | Phone/Email |
|-------|---------|------------|
| Backend API Issues | Sonal | - |
| Frontend Issues | Devesh | - |
| Infrastructure/DevOps | Prajeeth | - |
| Test Plan Questions | QA Lead | - |

---

## 📚 Additional Resources

### External References
- API Documentation: https://restful-booker.herokuapp.com/apidoc/index.html
- REST Assured Framework: http://rest-assured.io/
- TestNG Documentation: https://testng.org/
- Postman Documentation: https://learning.postman.com/

### Internal References
- Project folder: `Chapter_02_Prompt Engineering\Project_04_TestPlanDocument`
- JIRA Project: [Configure as needed]

---

## 📝 Document Management

### Version Control
- **Current Version:** 1.0
- **Last Updated:** 2026-05-28
- **Created By:** QA Team
- **Status:** Ready for Execution

### Change Log
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-05-28 | Initial document creation | QA Team |

### Approval Status
| Role | Status | Signature | Date |
|------|--------|-----------|------|
| QA Lead | ⏳ Pending | | |
| Project Manager | ⏳ Pending | | |
| Client | ⏳ Pending | | |

---

## ❓ FAQ

**Q: How long will testing take?**  
A: 2 sprints total (plan + case creation, then execution and reporting)

**Q: What if we find many bugs?**  
A: Defects are logged and prioritized. Testing repeats in cycles per the strategy.

**Q: Can tests be automated?**  
A: Yes, REST Assured framework is planned for automation (Phase 2)

**Q: What if the API is down?**  
A: Testers will work on alternate tasks; escalate to DevOps immediately

**Q: How are defects prioritized?**  
A: By severity (Critical/High/Medium/Low) and priority (P0-P3) per JIRA standards

---

## 🚀 Next Steps

1. **Review** all documentation with team
2. **Approve** test plan and strategy
3. **Prepare** test environment and data
4. **Execute** Phase 1: Smoke testing
5. **Report** initial findings
6. **Proceed** with Phase 2: In-depth testing per cycle

---

**For questions or clarifications, contact the QA Lead**

