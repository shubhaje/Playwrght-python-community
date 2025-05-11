from playwright.sync_api import Page
from config.test_data import USER_CREDENTIALS, DEFAULT_ENV

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
        
    def get_user_credentials(self, user_type: str, env: str = DEFAULT_ENV) -> dict:
        """Get user credentials from test data for specified user type and environment"""
        return USER_CREDENTIALS[env][user_type]