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
public class LoginTestValid {

	private static final Logger logger = LogManager.getLogger(LoginTestValid.class);
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

	@Test(description = "Verify login page loads successfully", priority = 1)
	public void testLoginPageLoad() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			Assert.assertTrue(loginPage.isUsernameFieldVisible(), "Username field should be visible on login page");
			logger.info("Test passed: Login page loaded successfully");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Login page load test failed", e);
		}
	}

	@Test(description = "Verify login with valid credentials", priority = 2, dependsOnMethods = {"testLoginPageLoad"})
	public void testLoginWithValidCredentials() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.login(Constants.VALID_USERNAME, Constants.VALID_PASSWORD);

			Thread.sleep(3000);
			String currentUrl = loginPage.getCurrentUrl();

			Assert.assertTrue(currentUrl.contains("salesforce") || currentUrl.contains("home"),
				"User should be redirected to Salesforce dashboard after successful login");
			logger.info("Test passed: Login with valid credentials successful");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Valid login test failed", e);
		}
	}

	@Test(description = "Verify password field is masked", priority = 3, dependsOnMethods = {"testLoginPageLoad"})
	public void testPasswordFieldMasking() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.enterPassword("TestPassword123");

			String fieldType = loginPage.driver.findElement(org.openqa.selenium.By.xpath("//input[@id='password']"))
				.getAttribute("type");

			Assert.assertEquals(fieldType, "password", "Password field should be of type password (masked)");
			logger.info("Test passed: Password field is properly masked");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Password masking test failed", e);
		}
	}

	@Test(description = "Verify login with Remember Me checked", priority = 4, dependsOnMethods = {"testLoginPageLoad"})
	public void testLoginWithRememberMe() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);
			loginPage.loginWithRememberMe(Constants.VALID_USERNAME, Constants.VALID_PASSWORD);

			Thread.sleep(3000);
			String currentUrl = loginPage.getCurrentUrl();

			Assert.assertTrue(currentUrl.contains("salesforce") || currentUrl.contains("home"),
				"User should be logged in with Remember Me option");
			logger.info("Test passed: Login with Remember Me successful");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Remember Me login test failed", e);
		}
	}

	@Test(description = "Verify forgot password link is clickable", priority = 5, dependsOnMethods = {"testLoginPageLoad"})
	public void testForgotPasswordLinkPresence() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);

			org.openqa.selenium.WebElement forgotPasswordLink = driver.findElement(
				org.openqa.selenium.By.xpath("//a[contains(text(), 'Forgot Your Password?')]")
			);

			Assert.assertTrue(forgotPasswordLink.isDisplayed(), "Forgot Password link should be visible");
			Assert.assertTrue(forgotPasswordLink.isEnabled(), "Forgot Password link should be enabled");
			logger.info("Test passed: Forgot Password link is present and clickable");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Forgot Password link test failed", e);
		}
	}

	@Test(description = "Verify login button is present", priority = 6, dependsOnMethods = {"testLoginPageLoad"})
	public void testLoginButtonPresence() {
		try {
			loginPage.navigateToLoginPage(Constants.BASE_URL);

			org.openqa.selenium.WebElement loginButton = driver.findElement(
				org.openqa.selenium.By.xpath("//input[@id='Login']")
			);

			Assert.assertTrue(loginButton.isDisplayed(), "Login button should be visible");
			Assert.assertTrue(loginButton.isEnabled(), "Login button should be enabled");
			logger.info("Test passed: Login button is present and enabled");
		} catch (Exception e) {
			logger.error("Test failed: " + e.getMessage(), e);
			throw new AssertionError("Login button presence test failed", e);
		}
	}
}
