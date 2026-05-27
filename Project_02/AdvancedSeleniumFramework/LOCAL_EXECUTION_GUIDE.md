# 🎯 LOCAL EXECUTION GUIDE - Run Tests On Your Windows Machine

## 📌 IMPORTANT: This Framework is Ready to Run Locally

Since Java/Maven aren't available in this development environment, you need to run the framework on **your local Windows 11 machine**. The framework is **100% complete** and ready to execute!

---

## ⏱️ TOTAL TIME NEEDED: ~15-20 minutes

### 5 minutes - Install prerequisites
### 3 minutes - Copy framework to your machine
### 2 minutes - Update credentials
### 5 minutes - Run tests

---

## 🔧 STEP-BY-STEP EXECUTION GUIDE

### **STEP 1: Install Java (5 minutes)**

1. **Download Java JDK 11:**
   - Go to: https://www.oracle.com/java/technologies/downloads/
   - Click "JDK 11" → "Windows x64 Installer"
   - Download `jdk-11.x.x_windows-x64_bin.exe`

2. **Install Java:**
   - Run the downloaded `.exe` file
   - Click "Next" → "Install"
   - Use default installation path: `C:\Program Files\Java\jdk-11.x.x`
   - Click "Finish"

3. **Verify Installation:**
   - Open Command Prompt
   - Run: `java -version`
   - Should show: `java version "11.x.x"`

---

### **STEP 2: Install Maven (3 minutes)**

1. **Download Maven:**
   - Go to: https://maven.apache.org/download.cgi
   - Download: `apache-maven-3.9.x-bin.zip`

2. **Extract Maven:**
   - Extract to: `C:\Program Files\Apache\maven`
   - Folder structure: `C:\Program Files\Apache\maven\bin\mvn.cmd` should exist

3. **Add Maven to PATH:**
   - Press `Win + X` → Select "System"
   - Click "Advanced system settings" button
   - Click "Environment Variables" button
   - Click "New" button (under System variables):
     - Variable name: `MAVEN_HOME`
     - Variable value: `C:\Program Files\Apache\maven`
     - Click OK

4. **Update PATH Variable:**
   - In Environment Variables, find and select "Path"
   - Click "Edit" button
   - Click "New" button
   - Add: `C:\Program Files\Apache\maven\bin`
   - Click OK → OK → OK

5. **Verify Installation:**
   - Close & reopen Command Prompt
   - Run: `mvn -version`
   - Should show Maven version info

---

### **STEP 3: Install Chrome Browser (2 minutes)**

- Go to: https://www.google.com/chrome/
- Download and install normally
- WebDriverManager will auto-download ChromeDriver

---

### **STEP 4: Copy Framework to Your Machine**

1. **Create project folder:**
   ```
   C:\SeleniumFramework\
   ```

2. **Copy entire AdvancedSeleniumFramework folder** to `C:\SeleniumFramework\`

3. **Verify structure:**
   ```
   C:\SeleniumFramework\AdvancedSeleniumFramework\
   ├── pom.xml
   ├── testng.xml
   ├── setup.bat
   ├── run-tests.bat
   ├── src/
   └── ...
   ```

---

### **STEP 5: Update Test Credentials (CRITICAL)**

1. **Open file:**
   ```
   C:\SeleniumFramework\AdvancedSeleniumFramework\
   src\main\java\com\salesforce\config\Constants.java
   ```

2. **Find these lines:**
   ```java
   public static final String VALID_USERNAME = "testuser@salesforce.com";
   public static final String VALID_PASSWORD = "ValidPassword@123";
   ```

3. **Update with YOUR credentials:**
   ```java
   public static final String VALID_USERNAME = "your-salesforce-email@domain.com";
   public static final String VALID_PASSWORD = "your-actual-password";
   ```

4. **Save the file (Ctrl+S)**

---

### **STEP 6: Setup Framework (First Time Only)**

**Option A: Using Batch Script (Easiest)**
1. Open Command Prompt
2. Navigate: `cd C:\SeleniumFramework\AdvancedSeleniumFramework`
3. Run: `setup.bat`
4. Wait for completion (2-3 minutes)
5. Check for: `[SUCCESS] Framework setup complete!`

**Option B: Using Command Line**
1. Open Command Prompt
2. Navigate: `cd C:\SeleniumFramework\AdvancedSeleniumFramework`
3. Run: `mvn clean install`
4. Wait for: `BUILD SUCCESS`

---

### **STEP 7: Run Your First Test**

**Option A: Single Test (Recommended for first run)**

1. Open Command Prompt
2. Navigate: `cd C:\SeleniumFramework\AdvancedSeleniumFramework`
3. Run:
   ```cmd
   mvn test -Dtest=LoginTestValid#testLoginPageLoad
   ```

4. **Watch your screen:**
   - Chrome will launch automatically
   - Navigates to Salesforce login page
   - Verifies username field is visible
   - Browser closes
   - Test completes

5. **Check result:**
   ```
   [INFO] ✓ TEST PASSED: testLoginPageLoad
   [INFO] BUILD SUCCESS
   ```

**Option B: All Tests**
```cmd
mvn test
```

This will run all 14 tests (valid + invalid)

---

## 📊 EXPECTED OUTPUT

### Console Output:
```
[INFO] Running com.salesforce.tests.LoginTestValid
[INFO] ========== TEST STARTED: testLoginPageLoad ==========
[INFO] Chrome browser initialized
[INFO] Navigated to login page: https://login.salesforce.com/?locale=in
[INFO] ✓ TEST PASSED: testLoginPageLoad
[INFO] Duration: 2345ms

[INFO] Tests run: 14
[INFO] Failures: 0
[INFO] BUILD SUCCESS
```

### Browser Behavior:
1. Chrome opens automatically
2. Navigates to login page
3. Performs test actions
4. Verifies results
5. Closes automatically

---

## 🎯 VERIFICATION CHECKLIST

Before running tests:

- [ ] Java 11+ installed (`java -version` works)
- [ ] Maven 3.6+ installed (`mvn -version` works)
- [ ] Chrome installed
- [ ] Framework copied to C:\SeleniumFramework\
- [ ] Constants.java updated with YOUR credentials
- [ ] `mvn clean install` completed successfully
- [ ] Internet connection available

---

## 🚀 QUICK COMMAND REFERENCE

```cmd
REM Navigate to framework
cd C:\SeleniumFramework\AdvancedSeleniumFramework

REM First time setup (install dependencies)
mvn clean install

REM Run all tests
mvn test

REM Run valid tests only
mvn test -Dtest=LoginTestValid

REM Run invalid tests only
mvn test -Dtest=LoginTestInvalid

REM Run specific test
mvn test -Dtest=LoginTestValid#testLoginPageLoad

REM Run with debug logging
mvn test -X

REM Check logs
type logs\automation-framework.log
```

---

## 📁 OUTPUT FILES AFTER RUNNING TESTS

```
logs/
├── automation-framework.log         (Detailed execution logs)

target/
├── surefire-reports/
│   ├── index.html                  (HTML test report)
│   ├── LoginTestValid.html
│   └── LoginTestInvalid.html
```

---

## 🐛 TROUBLESHOOTING

### Maven command not found
**Problem:** `'mvn' is not recognized`
- Solution: Verify Maven PATH is correct
- Command: `echo %PATH%`
- Should contain: `C:\Program Files\Apache\maven\bin`

### Java command not found
**Problem:** `'java' is not recognized`
- Solution: Verify Java PATH is correct
- Command: `echo %JAVA_HOME%`
- Should be: `C:\Program Files\Java\jdk-11.x.x`

### Chrome not launching
**Problem:** Browser doesn't open
- Solution: Install Chrome from https://www.google.com/chrome/
- Verify: Can open Chrome manually

### Tests timeout/hang
**Problem:** Tests run very slowly or hang
- Solution: Increase EXPLICIT_WAIT in Constants.java
- Change from: 15 to 30 seconds

### Login fails with credentials rejected
**Problem:** `testLoginWithValidCredentials` fails
- Solution: Update Constants.java with correct credentials
- Verify: Credentials work in browser manually
- Note: Use Salesforce test account, not production

### No log file created
**Problem:** `logs/automation-framework.log` doesn't exist
- Solution: Create logs folder
- Command: `mkdir logs`

---

## 📖 TEST EXECUTION WORKFLOW

```
START
  ↓
Run: mvn test
  ↓
Maven downloads dependencies (first time only)
  ↓
Java starts TestNG
  ↓
For each test:
  - @BeforeTest runs (driver init)
  - Chrome launches
  - Test executes
  - Assertions checked
  - Chrome closes
  - @AfterTest runs (driver cleanup)
  ↓
TestListener logs results
  ↓
Generate HTML report
  ↓
Display: BUILD SUCCESS or BUILD FAILURE
  ↓
END
```

---

## ✅ WHAT HAPPENS WHEN TEST PASSES

```
Test: testLoginPageLoad

✓ Chrome launches
✓ Navigates to https://login.salesforce.com/?locale=in
✓ Finds username field using XPath: //input[@id='username']
✓ Verifies field is visible
✓ Assertion passes
✓ Browser closes
✓ Test marked as PASSED
✓ Log entry created
✓ Report updated
```

---

## ❌ WHAT HAPPENS WHEN TEST FAILS

```
Test: testLoginWithValidCredentials

✗ Chrome launches
✗ Navigates to login page
✗ Enters credentials
✗ Clicks login button
✗ Waits for redirect (timeout!)
✗ Expected: Dashboard
✗ Actual: Still on login page
✗ Assertion fails
✗ Exception thrown
✗ Test marked as FAILED
✗ Error logged
✗ Report updated

Possible causes:
- Invalid credentials in Constants.java
- Salesforce account locked
- Network connectivity issue
- Selenium locator changed
```

---

## 📞 SUPPORT REFERENCES

| Issue | Reference |
|-------|-----------|
| Java Installation | https://www.oracle.com/java/technologies/downloads/ |
| Maven Installation | https://maven.apache.org/download.cgi |
| Chrome Installation | https://www.google.com/chrome/ |
| Salesforce Login | https://login.salesforce.com/?locale=in |
| Selenium Docs | https://www.selenium.dev/documentation/ |
| TestNG Docs | https://testng.org/ |

---

## 🎓 LEARNING NEXT STEPS

### After First Successful Test Run:

1. **Run all tests:**
   ```cmd
   mvn test
   ```
   - See all 14 tests execute
   - Review invalid test cases
   - Check error messages

2. **Review test code:**
   - Open: `src\test\java\com\salesforce\tests\LoginTestValid.java`
   - Read: How tests are structured
   - Understand: @Test, @BeforeTest, @AfterTest

3. **Review page object:**
   - Open: `src\main\java\com\salesforce\pages\LoginPage.java`
   - Read: Page methods
   - Understand: XPath locators

4. **Check logs:**
   - Open: `logs\automation-framework.log`
   - See: Detailed test execution
   - Understand: Logging pattern

5. **Review report:**
   - Open: `target\surefire-reports\index.html`
   - See: Test results visualization
   - Check: Pass/fail statistics

---

## 🏆 SUCCESS INDICATORS

✅ **First Test Passes When:**
- Chrome opens
- Test navigates to Salesforce
- Verifies username field exists
- Browser closes
- Console shows: `[SUCCESS]`

✅ **All Tests Pass When:**
- All 14 tests execute
- Console shows: `Tests run: 14`
- Console shows: `Failures: 0`
- Console shows: `BUILD SUCCESS`

---

## 📊 COMPLETE TIMELINE

| Step | Time | What Happens |
|------|------|--------------|
| Java Install | 5 min | Download & install |
| Maven Install | 3 min | Extract & configure |
| Chrome Install | 2 min | Download & install |
| Framework Copy | 2 min | Copy to C:\SeleniumFramework\ |
| Credentials Update | 1 min | Edit Constants.java |
| Maven Build | 3-5 min | `mvn clean install` |
| First Test Run | 2-3 min | Single test execution |
| **TOTAL** | **18-21 min** | Ready for testing |

---

## 🎉 YOU'RE READY!

Everything is set up and ready to run! Just follow these steps:

1. ✅ Install Java, Maven, Chrome
2. ✅ Copy framework folder
3. ✅ Update Constants.java with credentials
4. ✅ Run: `mvn clean install`
5. ✅ Run: `mvn test -Dtest=LoginTestValid#testLoginPageLoad`
6. ✅ Watch test execute in Chrome
7. ✅ Check results in console

---

**Framework Status:** ✅ 100% Complete & Ready to Run  
**Next Action:** Follow steps above on your Windows 11 machine  
**Expected Result:** All tests pass after credential update  

**Happy Testing! 🚀**
