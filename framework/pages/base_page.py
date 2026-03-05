import logging
from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._accept_cookies_btn = page.get_by_role("button", name="Consent")
        self._delete_account_btn = page.get_by_role("listitem").filter(has_text="Delete Account")
        self._close_add_btn = page.locator("iframe[name=\"aswift_2\"]").content_frame.locator("iframe[name=\"ad_iframe\"]").content_frame.get_by_role("button", name="Close ad")

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def get_title(self) -> str:
        return self.page.title()

    def get_url(self) -> str:
        return self.page.url

    def open_home(self, url: str) -> None:
        """Open home, accept cookies and check title."""
        self.navigate(url)
        self.handle_cookies()
        self.should_have_base_title()

    def handle_cookies(self) -> None:
        try:
            self._accept_cookies_btn.click(timeout=3000)
            logging.info("Cookies accepted")
        except PlaywrightTimeoutError:
            logging.info("No cookie banner present")

    def should_show_logged_in_name(self, name: str) -> None:
        """Check that 'Logged in as {name}' is displayed."""
        locator = self.page.get_by_role("listitem").filter(has_text=f"Logged in as {name}")
        expect(locator).to_be_visible()

    def delete_account(self) -> None:
        self._delete_account_btn.click()

    def close_add(self) -> None:
        self._close_add_btn.click()

    def should_have_base_title(self) -> None:
        expect(self.page).to_have_title("Automation Exercise")
