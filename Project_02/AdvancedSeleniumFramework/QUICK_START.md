# Quick Start Guide - AdvancedSeleniumFramework

## 🎯 Framework Overview

**Enterprise-Grade Selenium Automation Framework** for Salesforce login testing with:
- Page Object Model using PageFactory
- XPath-only locators
- TestNG annotations
- Robust exception handling
- Comprehensive logging
- 14 test cases (6 valid + 8 invalid)

---

## 🚀 Quick Setup (5 minutes)

### 1. Install Dependencies
```bash
mvn clean install
```

### 2. Update Test Data
Edit `src/main/java/com/salesforce/config/Constants.java`:
```java
public static final String VALID_USERNAME = "your-email@salesforce.com";
public static final String VALID_PASSWORD = "your-password";
```

### 3. Run Tests
```bash
mvn test
```

---

## 📋 Test Execution Commands

| Command | Purpose |
|---------|---------|
| `mvn test` | Run all tests |
| `mvn test -Dtest=LoginTestValid` | Run only valid tests |
| `mvn test -Dtest=LoginTestInvalid` | Run only invalid tests |
| `mvn test -Dtest=LoginTestValid#testLoginPageLoad` | Run specific test |
| `mvn clean install -DskipTests` | Build without running tests |

---

## 🔍 XPath Locators Reference

| Element | XPath |
|---------|-------|
| Username | `//input[@id='username']` |
| Password | `//input[@id='password']` |
| Login Button | `//input[@id='Login']` |
| Remember Me | `//input[@id='rememberUn']` |
| Error Message | `//div[@id='error']` |
| Forgot Password | `//a[contains(text(), 'Forgot Your Password?')]` |

---

## 📁 File Structure

```
src/main/java/com/salesforce/
├── config/Constants.java           ← URLs, timeouts, credentials
├── driver/DriverManager.java        ← WebDriver setup/cleanup
├── pages/LoginPage.java             ← Page Object Model
└── listeners/TestListener.java      ← Test reporting

src/test/java/com/salesforce/tests/
├── LoginTestValid.java              ← 6 valid test cases
└── LoginTestInvalid.java            ← 8 invalid test cases
```

---

## ✅ Valid Test Cases

1. **testLoginPageLoad** - Verify login page loads
2. **testLoginWithValidCredentials** - Login success
3. **testPasswordFieldMasking** - Password is masked
4. **testLoginWithRememberMe** - Remember Me functionality
5. **testForgotPasswordLinkPresence** - Link is visible
6. **testLoginButtonPresence** - Button is enabled

---

## ❌ Invalid Test Cases

1. **testLoginWithEmptyCredentials** - Both fields empty
2. **testLoginWithInvalidPassword** - Wrong password
3. **testLoginWithInvalidEmailFormat** - Invalid email
4. **testLoginWithEmptyPassword** - Password empty
5. **testLoginWithNonExistentUsername** - User doesn't exist
6. **testErrorMessageDisplay** - Error appears
7. **testLoginPageTitleAfterFailedLogin** - Stays on login page
8. **testUsernameFieldAfterFailedLogin** - Field accepts input

---

## 🛠️ Key Classes

### LoginPage.java (Page Object Model)
```java
loginPage.navigateToLoginPage(Constants.BASE_URL);
loginPage.enterUsername("test@email.com");
loginPage.enterPassword("password");
loginPage.clickLoginButton();
loginPage.login("email", "pass");
loginPage.loginWithRememberMe("email", "pass");
loginPage.getErrorMessage();
loginPage.isErrorMessageDisplayed();
```

### DriverManager.java
```java
WebDriver driver = DriverManager.initializeDriver("chrome");
WebDriverWait wait = DriverManager.getWait();
DriverManager.closeDriver();
```

### Constants.java
```java
Constants.BASE_URL                    // Login URL
Constants.VALID_USERNAME              // Test email
Constants.VALID_PASSWORD              // Test password
Constants.IMPLICIT_WAIT               // 10 seconds
Constants.EXPLICIT_WAIT               // 15 seconds
```

---

## 📊 Expected Output

```
[INFO] Running com.salesforce.tests.LoginTestValid
[INFO] ========== TEST STARTED: testLoginPageLoad ==========
[INFO] Navigated to login page: https://login.salesforce.com/?locale=in
[INFO] ✓ TEST PASSED: testLoginPageLoad
[INFO] Duration: 2345ms

[INFO] Running com.salesforce.tests.LoginTestInvalid
[INFO] ========== TEST STARTED: testLoginWithEmptyCredentials ==========
[INFO] ✓ TEST PASSED: testLoginWithEmptyCredentials
```

---

## 🔐 Best Practices Applied

✅ No Thread.sleep() - WebDriverWait used  
✅ XPath-only locators - No CSS/ID/name  
✅ PageFactory with @FindBy  
✅ TestNG annotations (@BeforeTest, @AfterTest, @Test)  
✅ Exception handling with try-catch  
✅ Logging at every step  
✅ ThreadLocal WebDriver  
✅ Reusable page methods  
✅ Centralized test data  
✅ Self-documenting code (no comments)  

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Driver not found | Check internet for WebDriverManager download |
| Test hangs | Increase EXPLICIT_WAIT in Constants.java |
| Element not found | Verify XPath in browser DevTools |
| Maven build fails | Run `mvn clean install` |

---

## 📞 Support

- Check `logs/automation-framework.log` for detailed logs
- Review TestNG report in `target/surefire-reports/`
- Verify credentials in Constants.java
- Check browser compatibility (Chrome/Firefox)

---

**Status:** ✅ Production Ready  
**Framework Version:** 1.0.0  
**Last Updated:** 2026-05-27
