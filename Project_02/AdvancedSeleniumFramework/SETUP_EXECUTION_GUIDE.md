# Complete Setup & Execution Guide

## 🔧 Prerequisites Installation (Windows 11)

### Step 1: Install Java 11+

1. **Download Java:**
   - Visit: https://www.oracle.com/java/technologies/downloads/
   - Select JDK 11 or later (Windows x64)
   - Click "Download"

2. **Install Java:**
   - Run the downloaded `.exe` file
   - Follow installation wizard (default path is fine)
   - Click "Next" → "Install" → "Finish"

3. **Verify Installation:**
   ```bash
   java -version
   ```
   Should show: `java version "11.0.x" or higher`

---

### Step 2: Install Maven

#### Option A: Manual Installation
1. **Download Maven:**
   - Visit: https://maven.apache.org/download.cgi
   - Download: `apache-maven-3.9.x-bin.zip`

2. **Extract:**
   - Extract to: `C:\Program Files\Apache\maven` (create folder if needed)
   - Folder structure should be: `C:\Program Files\Apache\maven\bin\mvn.cmd`

3. **Set Environment Variables:**
   - Press `Win + X` → Select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables" button
   - Click "New" (under System variables)
   - Variable name: `MAVEN_HOME`
   - Variable value: `C:\Program Files\Apache\maven`
   - Click OK

4. **Update PATH:**
   - In Environment Variables, select "Path" → Click "Edit"
   - Click "New" → Add: `C:\Program Files\Apache\maven\bin`
   - Click OK → OK → OK

5. **Verify Installation:**
   ```bash
   mvn -version
   ```
   Should show Maven version info

#### Option B: Quick Install (Chocolatey)
If you have Chocolatey installed:
```bash
choco install maven
```

---

### Step 3: Install Chrome/Firefox Browser

**For Chrome (Recommended):**
1. Download from: https://www.google.com/chrome/
2. Install normally
3. WebDriverManager will auto-download ChromeDriver

**For Firefox:**
1. Download from: https://www.mozilla.org/en-US/firefox/
2. Install normally
3. WebDriverManager will auto-download GeckoDriver

---

## 📦 Framework Setup

### Step 1: Navigate to Project
```bash
cd C:\Users\Asmita\OneDrive\Documents\AiTesterBluePrint3X\Project_02\AdvancedSeleniumFramework
```

### Step 2: Configure Test Credentials
**Open file:** `src\main\java\com\salesforce\config\Constants.java`

**Find and update:**
```java
public static final String VALID_USERNAME = "your-salesforce-email@domain.com";
public static final String VALID_PASSWORD = "your-salesforce-password";
```

**Example:**
```java
public static final String VALID_USERNAME = "testuser@salesforce.com";
public static final String VALID_PASSWORD = "MyPassword@123";
```

⚠️ **IMPORTANT:** Use actual Salesforce credentials or test account

---

## 🚀 Running Tests

### Option 1: Using Setup Script (Easiest)

#### First Time Setup:
1. Double-click: `setup.bat`
2. Wait for completion
3. Check console for success/errors

#### Run Tests:
1. Double-click: `run-tests.bat`
2. Wait for browser to launch
3. Tests will execute automatically
4. Check results when complete

### Option 2: Command Line

#### Build Project:
```bash
mvn clean install
```

#### Run All Tests:
```bash
mvn test
```

#### Run Valid Tests Only:
```bash
mvn test -Dtest=LoginTestValid
```

#### Run Invalid Tests Only:
```bash
mvn test -Dtest=LoginTestInvalid
```

#### Run Single Test:
```bash
mvn test -Dtest=LoginTestValid#testLoginPageLoad
```

---

## ✅ Test Execution Checklist

Before running tests:

- [ ] Java 11+ installed and verified
- [ ] Maven 3.6+ installed and verified
- [ ] Chrome or Firefox installed
- [ ] Salesforce credentials updated in Constants.java
- [ ] Internet connection available
- [ ] No firewall blocking browser/network

---

## 📊 What Happens When You Run Tests

1. **Browser Launch:** Chrome/Firefox opens automatically
2. **Navigation:** Test navigates to https://login.salesforce.com/?locale=in
3. **Action Execution:** Test performs login actions
4. **Verification:** Test verifies expected results
5. **Cleanup:** Browser closes automatically
6. **Report Generation:** TestNG report created

---

## 📋 Expected Output Examples

### Successful Test Run:
```
[INFO] Running com.salesforce.tests.LoginTestValid
[INFO] ========== TEST STARTED: testLoginPageLoad ==========
[INFO] Navigated to login page: https://login.salesforce.com/?locale=in
[INFO] ✓ TEST PASSED: testLoginPageLoad
[INFO] Duration: 2345ms

[INFO] Tests run: 14, Failures: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

### Failed Test Run:
```
[ERROR] ✗ TEST FAILED: testLoginWithValidCredentials
[ERROR] Error: Credentials rejected - invalid username or password
[ERROR] BUILD FAILURE
```

---

## 📁 Output Locations

After running tests:

- **Logs:** `logs/automation-framework.log`
- **TestNG Report:** `target/surefire-reports/index.html`
- **Console Output:** Displayed in command window

---

## 🐛 Troubleshooting

### Java Not Found
**Error:** `'java' is not recognized`
- **Solution:** Install Java and add to PATH
- **Verify:** `java -version` should work

### Maven Not Found
**Error:** `'mvn' is not recognized`
- **Solution:** Install Maven and add to PATH
- **Verify:** `mvn -version` should work

### Browser Not Starting
**Error:** Chrome/Firefox doesn't open
- **Solution:** Install Chrome or Firefox
- **Verify:** Can open browser manually

### WebDriver Download Fails
**Error:** Driver download timeout
- **Solution:** Check internet connection
- **Alternative:** Download manually and add to PATH

### Invalid Credentials
**Error:** Login fails even with correct password
- **Solution:** Update Constants.java with working credentials
- **Note:** May need to use test account instead of production

### Port Already in Use
**Error:** `Address already in use`
- **Solution:** Close other Maven processes or restart computer

---

## 🎯 First Test Success

### Quick Test: testLoginPageLoad (No credentials needed)

1. Open Command Prompt
2. Navigate to project:
   ```bash
   cd C:\Users\Asmita\OneDrive\Documents\AiTesterBluePrint3X\Project_02\AdvancedSeleniumFramework
   ```

3. Build project:
   ```bash
   mvn clean install
   ```

4. Run test:
   ```bash
   mvn test -Dtest=LoginTestValid#testLoginPageLoad
   ```

5. **Expected Result:** ✅ GREEN (PASSED)
   - Chrome opens
   - Navigates to login page
   - Verifies username field is visible
   - Browser closes
   - Test passes

---

## 📞 Support

### Common Issues & Solutions:

| Issue | Solution |
|-------|----------|
| Tests hang | Increase EXPLICIT_WAIT in Constants.java from 15 to 30 |
| Browser doesn't close | Check DriverManager.closeDriver() is called |
| Element not found | Verify XPath in browser DevTools |
| Login fails | Update credentials in Constants.java |
| No log file | Check logs/ folder exists, create if needed |

---

## 📖 Next Steps

1. ✅ Install Java & Maven (steps above)
2. ✅ Update credentials in Constants.java
3. ✅ Run: `mvn clean install`
4. ✅ Run: `mvn test -Dtest=LoginTestValid#testLoginPageLoad`
5. ✅ Verify: Test passes in console
6. ✅ Run: `mvn test` (all tests)
7. ✅ Check: `logs/automation-framework.log` for details

---

**Status:** ✅ Ready for Execution  
**Framework:** Advanced Selenium with Java  
**Version:** 1.0.0-RELEASE
