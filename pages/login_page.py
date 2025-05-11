from playwright.sync_api import Page
from config.test_data import USER_CREDENTIALS, DEFAULT_ENV
<<<<<<< HEAD
=======
import os
>>>>>>> 673faee01bed3c0a13a7a4de9732ce684bf40020

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def navigate(self):
        self.page.goto('https://www.saucedemo.com')

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.text_content()
<<<<<<< HEAD
        
    def get_user_credentials(self, user_type: str, env: str = DEFAULT_ENV) -> dict:
        """Get user credentials from test data for specified user type and environment"""
        return USER_CREDENTIALS[env][user_type]
=======

    @staticmethod
    def get_user_credentials(user_type: str, environment: str = None) -> dict:
        """
        Get credentials for a specific user type and environment
        Args:
            user_type: Type of user (e.g., 'standard_user', 'locked_out_user')
            environment: Environment to get credentials for (e.g., 'SIT', 'UAT')
        Returns:
            dict: Dictionary containing username and password
        """
        # Get environment from environment variable or use default
        env = environment or os.getenv('TEST_ENV', DEFAULT_ENV)
        
        # Get credentials for the specified environment
        env_credentials = USER_CREDENTIALS.get(env, USER_CREDENTIALS[DEFAULT_ENV])
        
        return env_credentials.get(user_type, {})
>>>>>>> 673faee01bed3c0a13a7a4de9732ce684bf40020
