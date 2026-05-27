package com.salesforce.config;

public class Constants {

	public static final String BASE_URL = "https://login.salesforce.com/?locale=in";
	public static final String BROWSER = "chrome";
	public static final long IMPLICIT_WAIT = 10;
	public static final long EXPLICIT_WAIT = 15;
	public static final long PAGE_LOAD_TIMEOUT = 30;

	public static final String VALID_USERNAME = "testuser@salesforce.com";
	public static final String VALID_PASSWORD = "ValidPassword@123";

	public static final String INVALID_USERNAME = "invalid@test.com";
	public static final String INVALID_PASSWORD = "WrongPassword@123";
	public static final String INVALID_EMAIL_FORMAT = "notanemail";

	public static final String EMPTY_STRING = "";

	public static final String SUCCESS_DASHBOARD_URL = "https://login.salesforce.com/home";
	public static final String ERROR_MESSAGE_INVALID_CREDENTIALS = "Please check your username, password, and organization ID";

	public static final int MAX_RETRY_ATTEMPTS = 3;
	public static final long POLLING_INTERVAL = 500;
}
