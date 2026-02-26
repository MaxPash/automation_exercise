import logging
from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.accept_cookies_btn = page.get_by_role("button", name="Consent")
        self.delete_account_btn = page.get_by_role("listitem").filter(has_text="Delete Account")
        self.close_add_btn = page.locator("iframe[name=\"aswift_2\"]").content_frame.locator("iframe[name=\"ad_iframe\"]").content_frame.get_by_role("button", name="Close ad")

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def accept_cookies(self, timeout: int = 3000 ):
        try
            self.accept_cookies_btn.click(timeout=timeout)
            logging.info("Cookie banner accepted")
        except PlaywrightTimeoutError:
            logging.info("No cookie banner found")


    def check_logged_in_name(self, name: str):
        return self.page.get_by_role("listitem").filter(has_text=f"Logged in as {name}")

    def delete_account(self):
        self.delete_account_btn.click()

    def close_add(self):
        self.close_add_btn.click()



    