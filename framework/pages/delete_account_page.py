from playwright.sync_api import Page, expect

from framework.pages.base_page import BasePage


class DeleteAccountPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._account_deleted_msg = page.locator("[data-qa='account-deleted']")
        self._continue_button = page.locator("[data-qa='continue-button']")

    def should_show_deleted_and_continue(self) -> None:
        """Проверить сообщение об удалении и нажать Continue."""
        expect(self._account_deleted_msg).to_be_visible()
        expect(self._continue_button).to_be_enabled()
        self._continue_button.click()
