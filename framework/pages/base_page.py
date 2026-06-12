import logging
import time
from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect

from framework.utils.popup import close_ad_popup


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._accept_cookies_btn = page.get_by_role("button", name="Consent")
        self._delete_account_btn = page.get_by_role("listitem").filter(has_text="Delete Account")
        self._log_out_btn = page.get_by_role("listitem").filter(has_text="Logout")
        self._products_btn = page.get_by_role("listitem").filter(has_text="Products")

    def navigate(self, url: str) -> None:
        max_attempts = 3
        last_error = None

        for attempt in range(1, max_attempts + 1):
            logging.info("Navigate attempt %s/%s to %s", attempt, max_attempts, url)
            try:
                self.page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=60000,
                )
                logging.info("Navigation successful on attempt %s to %s", attempt, url)
                return
            except PlaywrightTimeoutError as error:
                last_error = error
                logging.warning(
                    "Navigate timeout on attempt %s/%s for %s: %s",
                    attempt,
                    max_attempts,
                    url,
                    error,
                )
                if attempt < max_attempts:
                    time.sleep(2)

        logging.error("Navigation failed after %s attempts for %s", max_attempts, url)
        raise last_error

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
        """Close ad popup if present, using multiple possible close button locators."""
        close_ad_popup(self.page)

    def should_have_base_title(self) -> None:
        expect(self.page).to_have_title("Automation Exercise")

    def log_out(self) -> None:
        expect(self._log_out_btn).to_be_visible()
        self._log_out_btn.click()
        expect(self.page).to_have_title("Automation Exercise - Signup / Login")
    
    def go_to_products(self) -> None:
        self._products_btn.click()