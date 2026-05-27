# Advanced Selenium Framework - Salesforce Login Testing

## 📁 Framework Structure

```
AdvancedSeleniumFramework/
├── pom.xml
├── testng.xml
├── src/
│   ├── main/java/com/salesforce/
│   │   ├── config/
│   │   │   └── Constants.java                 [URLs, timeouts, test data]
│   │   ├── driver/
│   │   │   └── DriverManager.java             [WebDriver lifecycle]
│   │   ├── pages/
│   │   │   └── LoginPage.java                 [Page Object Model]
│   │   └── listeners/
│   │       └── TestListener.java              [TestNG reporting]
│   └── test/java/com/salesforce/
│       └── tests/
│           ├── LoginTestValid.java            [6 valid test cases]
│           └── LoginTestInvalid.java          [8 invalid test cases]
```

## 🚀 Setup Instructions

### Prerequisites
- Java 11 or higher
- Maven 3.6+
- Chrome/Firefox browser

### Installation Steps

1. **Navigate to project directory:**
```bash
cd AdvancedSeleniumFramework
```

2. **Install dependencies:**
```bash
mvn clean install
```

3. **Update Constants.java with valid credentials:**
```java
public static final String VALID_USERNAME = "your-valid-email@salesforce.com";
public static final String VALID_PASSWORD = "your-valid-password";
```

## 🧪 Test Execution

### Run All Tests
```bash
mvn test
```

### Run Valid Login Tests Only
```bash
mvn test -Dgroups="LoginTestValid"
```

### Run Invalid Login Tests Only
```bash
mvn test -Dgroups="LoginTestInvalid"
```

### Run Specific Test Class
```bash
mvn test -Dtest=com.salesforce.tests.LoginTestValid
```

### Run Specific Test Method
```bash
mvn test -Dtest=com.salesforce.tests.LoginTestValid#testLoginPageLoad
```

## 📊 Test Cases Summary

### Valid Test Cases (LoginTestValid.java)
1. ✓ **testLoginPageLoad** - Verifies login page loads successfully
2. ✓ **testLoginWithValidCredentials** - Login with correct credentials
3. ✓ **testPasswordFieldMasking** - Verifies password field is masked
4. ✓ **testLoginWithRememberMe** - Login with Remember Me checkbox
5. ✓ **testForgotPasswordLinkPresence** - Verifies Forgot Password link exists
6. ✓ **testLoginButtonPresence** - Verifies Login button is enabled

### Invalid Test Cases (LoginTestInvalid.java)
1. ✗ **testLoginWithEmptyCredentials** - Rejects empty username/password
2. ✗ **testLoginWithInvalidPassword** - Rejects wrong password
3. ✗ **testLoginWithInvalidEmailFormat** - Rejects invalid email format
4. ✗ **testLoginWithEmptyPassword** - Rejects empty password
5. ✗ **testLoginWithNonExistentUsername** - Rejects non-existent user
6. ✗ **testErrorMessageDisplay** - Verifies error message appears
7. ✗ **testLoginPageTitleAfterFailedLogin** - Checks page remains on login
8. ✗ **testUsernameFieldAfterFailedLogin** - Verifies field accepts new input

## 🔧 Key Features

### Page Object Model (LoginPage.java)
- **XPath-only locators** - No CSS, ID, or name selectors
- **PageFactory with @FindBy** - Clean initialization pattern
- **Reusable methods**:
  - `navigateToLoginPage(url)`
  - `enterUsername(username)`
  - `enterPassword(password)`
  - `clickLoginButton()`
  - `clickRememberMe()`
  - `getErrorMessage()`
  - `login(username, password)`
  - `loginWithRememberMe(username, password)`

### Robust Exception Handling
- Try-catch blocks in all methods
- Custom exception throwing with descriptive messages
- Logging at every step for debugging
- WebDriverWait with explicit waits (no Thread.sleep)

### TestNG Integration
- `@BeforeTest` - Driver initialization
- `@AfterTest` - Driver cleanup
- `@Test` - Individual test cases
- `@Listeners` - TestListener for reporting
- Dependency management between tests
- Priority-based execution

### Logging (Log4j)
- Comprehensive logging at INFO, WARN, ERROR levels
- Test execution tracking
- Exception stack traces
- Test result summaries

## 📝 Configuration Files

### Constants.java
```java
BASE_URL = "https://login.salesforce.com/?locale=in"
IMPLICIT_WAIT = 10 seconds
EXPLICIT_WAIT = 15 seconds
PAGE_LOAD_TIMEOUT = 30 seconds
```

### testng.xml
- Configures test execution order
- Groups valid and invalid tests separately
- Runs tests sequentially (parallel="false")
- Attaches TestListener for reporting

## 🔍 XPath Locators Used

```java
//input[@id='username']        // Username field
//input[@id='password']         // Password field
//input[@id='Login']            // Login button
//input[@id='rememberUn']       // Remember Me checkbox
//div[@id='error']              // Error message
//a[contains(text(), 'Forgot Your Password?')]  // Forgot Password link
```

## 📋 Best Practices Implemented

✅ **Enterprise-Grade Standards**
✅ **No Thread.sleep() - WebDriverWait only**
✅ **No Comments - Self-documenting code**
✅ **ThreadLocal WebDriver** - Thread-safe execution
✅ **Exception Handling** - Structured try-catch
✅ **Logging** - Every action logged
✅ **Modular Design** - Reusable components
✅ **Data Centralization** - Constants.java
✅ **Page Object Model** - Maintainable locators
✅ **TestNG Annotations** - Proper lifecycle management

## 🛠️ Troubleshooting

### WebDriver Not Found
- Ensure WebDriverManager dependency is in pom.xml
- Check internet connection for driver download

### Tests Hanging
- Increase `EXPLICIT_WAIT` in Constants.java
- Verify URL accessibility
- Check browser compatibility

### Element Not Found
- Verify XPath expressions in LoginPage.java
- Check if page loaded completely
- Increase explicit wait timeout

## 📦 Dependencies

```xml
Selenium 4.15.0
TestNG 7.8.1
WebDriverManager 5.6.2
Log4j 2.21.0
Java 11+
Maven 3.6+
```

## 📄 Next Steps

1. Add credentials to Constants.java
2. Run `mvn clean install`
3. Execute `mvn test`
4. View results in console/testng-report.html

---
**Framework Created:** 2026-05-27
**Status:** Production Ready ✅
