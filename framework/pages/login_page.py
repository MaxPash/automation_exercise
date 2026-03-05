from playwright.sync_api import Page, expect

from framework.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._signup_login_button = page.get_by_role("link", name="Signup / Login")
        self._login_email_input = page.locator("[data-qa='login-email']")
        self._login_password_input = page.locator("[data-qa='login-password']")
        self._login_button = page.locator("[data-qa='login-button']")
        self._signup_name_input = page.locator("[data-qa='signup-name']")
        self._signup_email_input = page.locator("[data-qa='signup-email']")
        self._signup_button = page.locator("[data-qa='signup-button']")
        self._error_msg = page.locator("p").filter(has_text="incorrect")
    
    def open(self) -> None:
        """Navigate to login page and check title."""
        self._signup_login_button.click()
        expect(self.page).to_have_title("Automation Exercise - Signup / Login")

    def fill_login_email(self, email: str) -> None:
        self._login_email_input.fill(email)

    def fill_login_password(self, password: str) -> None:
        self._login_password_input.fill(password)

    def log_in(self, email: str, password: str) -> None:
        self.fill_login_email(email)
        self.fill_login_password(password)
        self._login_button.click()

    def start_signup(self, name: str, email: str) -> None:
        """Fill name and email and click Signup."""
        self._signup_name_input.fill(name)
        self._signup_email_input.fill(email)
        expect(self._signup_button).to_be_enabled()
        self._signup_button.click()

    def should_show_error_message(self) -> None:
        expect(self._error_msg).to_be_visible()

    def get_error_message(self) -> str:
        return self._error_msg.text_content()

    def should_show_login_page(self) -> None:
        expect(self.page).to_have_title("Automation Exercise - Signup / Login")