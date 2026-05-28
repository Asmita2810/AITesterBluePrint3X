package com.salesforce.driver;

import java.time.Duration;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import io.github.bonigarcia.wdm.WebDriverManager;
import com.salesforce.config.Constants;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class DriverManager {

	private static final Logger logger = LogManager.getLogger(DriverManager.class);
	private static final ThreadLocal<WebDriver> driver = new ThreadLocal<>();
	private static final ThreadLocal<WebDriverWait> wait = new ThreadLocal<>();

	public static WebDriver initializeDriver(String browser) {
		try {
			WebDriver webDriver;
			String browserType = browser.toLowerCase();

			if (browserType.equals("chrome")) {
				WebDriverManager.chromedriver().setup();
				webDriver = new ChromeDriver();
				logger.info("Chrome browser initialized");
			} else if (browserType.equals("firefox")) {
				WebDriverManager.firefoxdriver().setup();
				webDriver = new FirefoxDriver();
				logger.info("Firefox browser initialized");
			} else {
				WebDriverManager.chromedriver().setup();
				webDriver = new ChromeDriver();
				logger.warn("Unknown browser type, defaulting to Chrome");
			}

			webDriver.manage().timeouts().implicitlyWait(Duration.ofSeconds(Constants.IMPLICIT_WAIT));
			webDriver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(Constants.PAGE_LOAD_TIMEOUT));
			webDriver.manage().window().maximize();

			driver.set(webDriver);
			wait.set(new WebDriverWait(webDriver, Duration.ofSeconds(Constants.EXPLICIT_WAIT)));

			logger.info("WebDriver initialized successfully");
			return webDriver;

		} catch (Exception e) {
			logger.error("Failed to initialize WebDriver: " + e.getMessage(), e);
			throw new RuntimeException("Driver initialization failed", e);
		}
	}

	public static WebDriver getDriver() {
		if (driver.get() == null) {
			throw new RuntimeException("WebDriver not initialized. Call initializeDriver() first");
		}
		return driver.get();
	}

	public static WebDriverWait getWait() {
		if (wait.get() == null) {
			throw new RuntimeException("WebDriverWait not initialized. Call initializeDriver() first");
		}
		return wait.get();
	}

	public static void closeDriver() {
		try {
			WebDriver webDriver = driver.get();
			if (webDriver != null) {
				webDriver.quit();
				driver.remove();
				wait.remove();
				logger.info("WebDriver closed successfully");
			}
		} catch (Exception e) {
			logger.error("Error closing WebDriver: " + e.getMessage(), e);
		}
	}
}
