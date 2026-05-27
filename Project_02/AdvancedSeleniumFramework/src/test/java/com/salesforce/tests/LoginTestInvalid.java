package com.salesforce.tests;

import org.testng.Assert;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.AfterTest;
import org.testng.annotations.Test;
import org.testng.annotations.Listeners;
import org.openqa.selenium.WebDriver;
import com.salesforce.driver.DriverManager;
import com.salesforce.pages.LoginPage;
import com.salesforce.config.Constants;
import com.salesforce.listeners.TestListener;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

@Listeners(TestListener.class)
public class LoginTestInvalid {

	private static final Logger logger = LogManager.getLogger(LoginTestInvalid.class);
	private WebDriver driver;
	private LoginPage loginPage;

	@BeforeTest
	public void setUp() {
		try {
			driver = DriverManager.initializeDriver(Constants.BROWSER);
			loginPage = new LoginPage(driver);
			logger.info("Test setup completed");
		} catch (Exception e) {
			logger.error("Setup failed: " + e.getMessage(), e);
			throw new RuntimeException("Test setup failed", e);
		}
	}

	@AfterTest
	public void tearDown() {
		try {
			DriverManager.closeDriver();
			logger.info("Test teardown completed");
		} catch (Exception e) {
			logger.error("Teardown failed: " + e.getMessage(), e);
		}
	}

	@Test(description = "Verify login fails with empty username and password", priority = 1)
	public void testLoginWithEmptyCredentials() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.EMPTY_STRING, Constants.EMPTY_STRING);

			Thread.sleep(2000);

			boolean isErrorDisplayed = loginPage.isErrorMessageDisplayed();
			Assert.assertTrue(isErrorDisplayed, "Error message should be displayed for empty credentials");
			logger.info("Test passed: Login correctly rejected with empty credentials");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Empty credentials test failed", e);
		}
	}

	@Test(description = "Verify login fails with valid username but invalid password", priority = 2)
	public void testLoginWithInvalidPassword() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.VALID_USERNAME, Constants.INVALID_PASSWORD);

			Thread.sleep(2000);

			boolean isErrorDisplayed = loginPage.isErrorMessageDisplayed();
			Assert.assertTrue(isErrorDisplayed, "Error message should be displayed for invalid password");

			String currentUrl = loginPage.getCurrentUrl();
			Assert.assertTrue(currentUrl.contains("login.salesforce.com"),
				"User should remain on login page after failed login attempt");
			logger.info("Test passed: Login correctly rejected with invalid password");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Invalid password test failed", e);
		}
	}

	@Test(description = "Verify login fails with invalid username format", priority = 3)
	public void testLoginWithInvalidEmailFormat() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.INVALID_EMAIL_FORMAT, Constants.VALID_PASSWORD);

			Thread.sleep(2000);

			boolean isErrorDisplayed = loginPage.isErrorMessageDisplayed();
			Assert.assertTrue(isErrorDisplayed, "Error message should be displayed for invalid email format");
			logger.info("Test passed: Login correctly rejected with invalid email format");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Invalid email format test failed", e);
		}
	}

	@Test(description = "Verify login fails with empty password", priority = 4)
	public void testLoginWithEmptyPassword() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.VALID_USERNAME, Constants.EMPTY_STRING);

			Thread.sleep(2000);

			boolean isErrorDisplayed = loginPage.isErrorMessageDisplayed();
			Assert.assertTrue(isErrorDisplayed, "Error message should be displayed for empty password");
			logger.info("Test passed: Login correctly rejected with empty password");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Empty password test failed", e);
		}
	}

	@Test(description = "Verify login fails with non-existent username", priority = 5)
	public void testLoginWithNonExistentUsername() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.INVALID_USERNAME, Constants.INVALID_PASSWORD);

			Thread.sleep(2000);

			boolean isErrorDisplayed = loginPage.isErrorMessageDisplayed();
			Assert.assertTrue(isErrorDisplayed, "Error message should be displayed for non-existent username");

			String currentUrl = loginPage.getCurrentUrl();
			Assert.assertTrue(currentUrl.contains("login.salesforce.com"),
				"User should remain on login page after failed login attempt");
			logger.info("Test passed: Login correctly rejected with non-existent username");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Non-existent username test failed", e);
		}
	}

	@Test(description = "Verify error message is displayed after failed login", priority = 6)
	public void testErrorMessageDisplay() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.INVALID_USERNAME, Constants.INVALID_PASSWORD);

			Thread.sleep(2000);

			Assert.assertTrue(loginPage.isErrorMessageDisplayed(), "Error message should be visible after failed login");

			String errorText = loginPage.getErrorMessage();
			Assert.assertNotNull(errorText, "Error message text should not be null");
			Assert.assertFalse(errorText.isEmpty(), "Error message should not be empty");
			logger.info("Test passed: Error message displayed correctly with text: " + errorText);
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Error message display test failed", e);
		}
	}

	@Test(description = "Verify login page title on invalid login attempt", priority = 7)
	public void testLoginPageTitleAfterFailedLogin() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.INVALID_USERNAME, Constants.INVALID_PASSWORD);

			Thread.sleep(2000);

			String pageTitle = driver.getTitle();
			Assert.assertTrue(pageTitle.toLowerCase().contains("salesforce") || pageTitle.toLowerCase().contains("login"),
				"Page title should indicate login page after failed authentication");
			logger.info("Test passed: Page title is correct after failed login: " + pageTitle);
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Page title test failed", e);
		}
	}

	@Test(description = "Verify username field accepts input after failed login", priority = 8)
	public void testUsernameFieldAfterFailedLogin() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.INVALID_USERNAME, Constants.INVALID_PASSWORD);

			Thread.sleep(2000);

			loginPage.enterUsername(Constants.VALID_USERNAME);

			org.openqa.selenium.WebElement usernameField = driver.findElement(
				org.openqa.selenium.By.xpath("//input[@id='username']")
			);
			String enteredValue = usernameField.getAttribute("value");
			Assert.assertEquals(enteredValue, Constants.VALID_USERNAME, "Username field should accept new input after failed login");
			logger.info("Test passed: Username field is functional after failed login attempt");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Username field test failed", e);
		}
	}
}
