package com.salesforce.pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import com.salesforce.driver.DriverManager;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class LoginPage {

	private static final Logger logger = LogManager.getLogger(LoginPage.class);
	private WebDriver driver;
	private WebDriverWait wait;

	@FindBy(xpath = "//input[@id='username']")
	private WebElement usernameField;

	@FindBy(xpath = "//input[@id='password']")
	private WebElement passwordField;

	@FindBy(xpath = "//input[@id='Login']")
	private WebElement loginButton;

	@FindBy(xpath = "//input[@id='rememberUn']")
	private WebElement rememberMeCheckbox;

	@FindBy(xpath = "//div[@id='error']")
	private WebElement errorMessage;

	@FindBy(xpath = "//a[contains(text(), 'Forgot Your Password?')]")
	private WebElement forgotPasswordLink;

	public LoginPage(WebDriver driver) {
		this.driver = driver;
		this.wait = DriverManager.getWait();
		PageFactory.initElements(driver, this);
		logger.info("LoginPage initialized");
	}

	public void navigateToLoginPage(String url) {
		try {
			driver.navigate().to(url);
			wait.until(ExpectedConditions.presenceOf(usernameField));
			logger.info("Navigated to login page: " + url);
		} catch (Exception e) {
			logger.error("Failed to navigate to login page: " + e.getMessage(), e);
			throw new RuntimeException("Navigation failed", e);
		}
	}

	public void enterUsername(String username) {
		try {
			wait.until(ExpectedConditions.visibilityOf(usernameField));
			usernameField.clear();
			usernameField.sendKeys(username);
			logger.info("Username entered: " + username);
		} catch (Exception e) {
			logger.error("Failed to enter username: " + e.getMessage(), e);
			throw new RuntimeException("Username entry failed", e);
		}
	}

	public void enterPassword(String password) {
		try {
			wait.until(ExpectedConditions.visibilityOf(passwordField));
			passwordField.clear();
			passwordField.sendKeys(password);
			logger.info("Password entered successfully");
		} catch (Exception e) {
			logger.error("Failed to enter password: " + e.getMessage(), e);
			throw new RuntimeException("Password entry failed", e);
		}
	}

	public void clickRememberMe() {
		try {
			wait.until(ExpectedConditions.elementToBeClickable(rememberMeCheckbox));
			if (!rememberMeCheckbox.isSelected()) {
				rememberMeCheckbox.click();
				logger.info("Remember Me checkbox clicked");
			}
		} catch (Exception e) {
			logger.error("Failed to click Remember Me checkbox: " + e.getMessage(), e);
			throw new RuntimeException("Remember Me click failed", e);
		}
	}

	public void clickLoginButton() {
		try {
			wait.until(ExpectedConditions.elementToBeClickable(loginButton));
			loginButton.click();
			logger.info("Login button clicked");
		} catch (Exception e) {
			logger.error("Failed to click login button: " + e.getMessage(), e);
			throw new RuntimeException("Login button click failed", e);
		}
	}

	public String getErrorMessage() {
		try {
			wait.until(ExpectedConditions.visibilityOf(errorMessage));
			String message = errorMessage.getText();
			logger.info("Error message retrieved: " + message);
			return message;
		} catch (Exception e) {
			logger.error("Failed to get error message: " + e.getMessage(), e);
			throw new RuntimeException("Error message retrieval failed", e);
		}
	}

	public boolean isErrorMessageDisplayed() {
		try {
			wait.until(ExpectedConditions.visibilityOf(errorMessage));
			boolean isDisplayed = errorMessage.isDisplayed();
			logger.info("Error message displayed: " + isDisplayed);
			return isDisplayed;
		} catch (Exception e) {
			logger.warn("Error message not displayed: " + e.getMessage());
			return false;
		}
	}

	public boolean isUsernameFieldVisible() {
		try {
			return wait.until(ExpectedConditions.visibilityOf(usernameField)).isDisplayed();
		} catch (Exception e) {
			logger.warn("Username field not visible: " + e.getMessage());
			return false;
		}
	}

	public String getCurrentUrl() {
		String url = driver.getCurrentUrl();
		logger.info("Current URL: " + url);
		return url;
	}

	public void login(String username, String password) {
		try {
			enterUsername(username);
			enterPassword(password);
			clickLoginButton();
			logger.info("Login attempt completed with username: " + username);
		} catch (Exception e) {
			logger.error("Login failed: " + e.getMessage(), e);
			throw new RuntimeException("Login process failed", e);
		}
	}

	public void loginWithRememberMe(String username, String password) {
		try {
			enterUsername(username);
			enterPassword(password);
			clickRememberMe();
			clickLoginButton();
			logger.info("Login with Remember Me completed");
		} catch (Exception e) {
			logger.error("Login with Remember Me failed: " + e.getMessage(), e);
			throw new RuntimeException("Login with Remember Me failed", e);
		}
	}
}
