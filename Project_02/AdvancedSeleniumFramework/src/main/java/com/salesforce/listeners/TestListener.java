package com.salesforce.listeners;

import org.testng.ITestListener;
import org.testng.ITestResult;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import com.salesforce.driver.DriverManager;

public class TestListener implements ITestListener {

	private static final Logger logger = LogManager.getLogger(TestListener.class);

	@Override
	public void onTestStart(ITestResult result) {
		logger.info("========== TEST STARTED: " + result.getMethod().getMethodName() + " ==========");
	}

	@Override
	public void onTestSuccess(ITestResult result) {
		logger.info("✓ TEST PASSED: " + result.getMethod().getMethodName());
		logger.info("Duration: " + (result.getEndMillis() - result.getStartMillis()) + "ms");
	}

	@Override
	public void onTestFailure(ITestResult result) {
		logger.error("✗ TEST FAILED: " + result.getMethod().getMethodName());
		logger.error("Error: " + result.getThrowable().getMessage(), result.getThrowable());
		logger.error("Duration: " + (result.getEndMillis() - result.getStartMillis()) + "ms");
	}

	@Override
	public void onTestSkipped(ITestResult result) {
		logger.warn("⊘ TEST SKIPPED: " + result.getMethod().getMethodName());
		logger.warn("Reason: " + result.getThrowable().getMessage());
	}

	@Override
	public void onTestFailedButWithinSuccessPercentage(ITestResult result) {
		logger.warn("TEST PASSED WITH TOLERANCE: " + result.getMethod().getMethodName());
	}

	@Override
	public void onFinish(org.testng.ITestContext context) {
		logger.info("========== TEST SUITE FINISHED ==========");
		logger.info("Total Tests: " + context.getAllTestMethods().length);
		logger.info("Passed: " + context.getPassedTests().size());
		logger.info("Failed: " + context.getFailedTests().size());
		logger.info("Skipped: " + context.getSkippedTests().size());
	}
}
