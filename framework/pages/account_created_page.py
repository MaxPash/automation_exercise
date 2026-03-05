from playwright.sync_api import Page, expect

from framework.pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._account_created_msg = page.locator("[data-qa='account-created']")
        self._continue_button = page.locator("[data-qa='continue-button']")

    def should_have_account_created_title(self) -> None:
        expect(self.page).to_have_title("Automation Exercise - Account Created")

    def should_show_account_created_and_continue(self) -> None:
        """Check account created message and click Continue."""
        self.should_have_account_created_title()
        expect(self._account_created_msg).to_be_visible()
        expect(self._continue_button).to_be_enabled()
        self._continue_button.click()

