# 📚 Advanced Selenium Framework - Documentation Index

## 🎯 Start Here Based on Your Role

### **If You're New to This Framework**
1. Read: `QUICK_START.md` (5 minutes)
2. Read: `SETUP_EXECUTION_GUIDE.md` (10 minutes)
3. Run: `mvn clean install`
4. Update credentials
5. Run: `mvn test -Dtest=LoginTestValid#testLoginPageLoad`

### **If You Want Complete Details**
1. Read: `README.md` (framework overview)
2. Read: `EXECUTION_SUMMARY.md` (everything you need)
3. Check: Source code in `src/`
4. Review: `testng.xml` (test configuration)

### **If You Want to Run Tests Immediately**
1. Double-click: `setup.bat` (Windows)
2. Update: `src/main/java/com/salesforce/config/Constants.java`
3. Double-click: `run-tests.bat`
4. Check: `logs/automation-framework.log`

### **If You're a Developer**
1. Review: `src/main/java/com/salesforce/` (source code)
2. Review: `src/test/java/com/salesforce/tests/` (test cases)
3. Read: `pom.xml` (dependencies)
4. Check: `testng.xml` (execution config)

---

## 📄 Documentation Files

### **Quick References**
| File | Purpose | Read Time | Audience |
|------|---------|-----------|----------|
| `QUICK_START.md` | Command reference & test matrix | 5 min | Everyone |
| `EXECUTION_SUMMARY.md` | Complete overview & next steps | 15 min | Project leads |
| `README.md` | Framework features & capabilities | 20 min | Developers |

### **Setup & Installation**
| File | Purpose | Read Time | Audience |
|------|---------|-----------|----------|
| `SETUP_EXECUTION_GUIDE.md` | Step-by-step installation | 30 min | First-time users |
| `setup.bat` | Automated setup (Windows) | - | Windows users |
| `setup.ps1` | Automated setup (PowerShell) | - | Modern Windows |

### **Test Execution**
| File | Purpose | Use When | Audience |
|------|---------|----------|----------|
| `run-tests.bat` | Execute all tests | Windows | QA Engineers |
| `run-tests.ps1` | Execute all tests | PowerShell | QA Engineers |
| `run-single-test.bat` | Single test execution | Windows | Debugging |
| `run-single-test.ps1` | Single test execution | PowerShell | Debugging |

### **Configuration**
| File | Purpose | Edit? | Audience |
|------|---------|-------|----------|
| `pom.xml` | Maven dependencies | Only if adding libs | Developers |
| `testng.xml` | Test execution config | Only if changing tests | QA Engineers |
| `Constants.java` | URLs, credentials, timeouts | **YES - Update this** | Everyone |
| `log4j2.properties` | Logging configuration | Optional | Developers |

---

## 📂 Source Code Structure

### **Main Source Code** (`src/main/java/com/salesforce/`)

```
config/
└── Constants.java          Central configuration
    ├── BASE_URL
    ├── VALID_USERNAME / PASSWORD
    ├── IMPLICIT_WAIT = 10 seconds
    ├── EXPLICIT_WAIT = 15 seconds
    └── All test data

driver/
└── DriverManager.java      WebDriver lifecycle
    ├── initializeDriver()
    ├── getDriver()
    ├── getWait()
    └── closeDriver()

pages/
└── LoginPage.java          Page Object Model
    ├── 6 @FindBy locators (XPath only)
    ├── 11 action methods
    ├── Exception handling
    └── WebDriverWait implementation

listeners/
└── TestListener.java       TestNG reporting
    ├── onTestStart()
    ├── onTestSuccess()
    ├── onTestFailure()
    └── onFinish()
```

### **Test Code** (`src/test/java/com/salesforce/tests/`)

```
LoginTestValid.java        6 Valid Test Cases
├── testLoginPageLoad      Page loads successfully
├── testLoginWithValidCredentials
├── testPasswordFieldMasking
├── testLoginWithRememberMe
├── testForgotPasswordLinkPresence
└── testLoginButtonPresence

LoginTestInvalid.java      8 Invalid Test Cases
├── testLoginWithEmptyCredentials
├── testLoginWithInvalidPassword
├── testLoginWithInvalidEmailFormat
├── testLoginWithEmptyPassword
├── testLoginWithNonExistentUsername
├── testErrorMessageDisplay
├── testLoginPageTitleAfterFailedLogin
└── testUsernameFieldAfterFailedLogin
```

---

## 🚀 Common Commands Quick Reference

### **Setup & Build**
```bash
mvn clean install                    # Build & install (first time)
mvn clean verify                     # Build & verify
mvn dependency:tree                  # View dependency tree
```

### **Run Tests**
```bash
mvn test                             # Run all tests
mvn test -Dtest=LoginTestValid       # Run one test class
mvn test -Dtest=LoginTestValid#testLoginPageLoad  # Run one method
mvn test -X                          # Run with debug logging
mvn test -DskipTests                 # Build without testing
```

### **Reporting & Logs**
```bash
cat logs/automation-framework.log    # View latest logs
mvn clean test                       # Generate fresh report
open target/surefire-reports/index.html  # View HTML report
```

### **Debugging**
```bash
mvn test -Dtest=LoginTestValid#testLoginPageLoad -X  # Debug mode
mvn test -Dgroups=LoginTestValid                    # By group
mvn clean install -U                                # Update deps
```

---

## 🔍 File Navigation Guide

### **To Find...**
| What | Where | File |
|------|-------|------|
| Login page locators | XPath selectors | `LoginPage.java:21-35` |
| Test credentials | Username/password | `Constants.java:11-12` |
| Login methods | Page actions | `LoginPage.java:42-130` |
| Valid test cases | 6 scenarios | `LoginTestValid.java:entire file` |
| Invalid test cases | 8 scenarios | `LoginTestInvalid.java:entire file` |
| Timeouts | Wait configurations | `Constants.java:7-9` |
| TestNG config | Test execution | `testng.xml` |
| Dependencies | Maven libraries | `pom.xml:27-66` |
| Logging config | Log4j settings | `log4j2.properties` |

---

## ✅ Pre-Execution Checklist

- [ ] Java 11+ installed (`java -version`)
- [ ] Maven 3.6+ installed (`mvn -version`)
- [ ] Chrome/Firefox installed
- [ ] Framework folder accessible
- [ ] Internet connection available
- [ ] Constants.java updated with credentials
- [ ] `mvn clean install` completed successfully
- [ ] No firewall blocking browser

---

## 🎓 Learning Path

### Beginner
1. Run setup.bat
2. Read QUICK_START.md
3. Run: `mvn test -Dtest=LoginTestValid#testLoginPageLoad`
4. Review: LoginPage.java
5. Review: LoginTestValid.java

### Intermediate
1. Review entire README.md
2. Review all test cases
3. Review DriverManager.java
4. Modify a test case
5. Add a new test case

### Advanced
1. Review Constants.java
2. Review TestListener.java
3. Review log4j2.properties
4. Review pom.xml
5. Integrate with CI/CD pipeline

---

## 🐛 Debugging Guide

### Test hangs?
- File: `Constants.java:9`
- Increase: `EXPLICIT_WAIT` from 15 to 30

### Element not found?
- File: `LoginPage.java:21-35`
- Verify: XPath in browser DevTools
- Update: @FindBy annotations

### Login fails?
- File: `Constants.java:11-12`
- Update: VALID_USERNAME & VALID_PASSWORD
- Verify: Credentials work in browser

### Tests don't run?
- Check: `mvn clean install` completed
- Check: Constants.java has valid credentials
- Check: Browser installed
- Check: Internet connection

### No logs generated?
- Check: `logs/` folder exists
- Check: File permissions
- Create manually: `mkdir logs`
- Check: log4j2.properties path

---

## 📞 Quick Help

### Maven not found?
```bash
# Add to PATH: C:\Program Files\Apache\maven\bin
# Then verify: mvn -version
```

### Java not found?
```bash
# Install from: https://www.oracle.com/java/technologies/downloads/
# Verify: java -version
```

### Browser not launching?
```bash
# Install Chrome: https://www.google.com/chrome/
# Or Firefox: https://www.mozilla.org/firefox/
```

### Tests fail with "Invalid Username/Password"?
```java
// Update in Constants.java
public static final String VALID_USERNAME = "your-real-salesforce-email@domain.com";
public static final String VALID_PASSWORD = "your-real-password";
```

---

## 📊 File Statistics

| Category | Count | Details |
|----------|-------|---------|
| Total Files | 22 | Documentation + Code + Config |
| Java Classes | 7 | 4 main + 2 test + 1 listener |
| Test Cases | 14 | 6 valid + 8 invalid |
| XPath Locators | 6 | In LoginPage.java |
| Documentation | 7 | Guides + README + Examples |
| Scripts | 6 | Batch + PowerShell + Docker |
| Total Lines | 1200+ | All code combined |

---

## 🏆 Quality Standards Met

- ✅ Enterprise-grade architecture
- ✅ No Thread.sleep() usage
- ✅ XPath-only locators
- ✅ Page Object Model
- ✅ Robust exception handling
- ✅ Comprehensive logging
- ✅ TestNG annotations
- ✅ ThreadLocal WebDriver
- ✅ Documented & ready
- ✅ Cross-platform compatible

---

## 📅 Last Updated

- Created: 2026-05-27
- Framework Version: 1.0.0-RELEASE
- Status: ✅ Production Ready

---

**Questions? Check the relevant doc above! 👆**
