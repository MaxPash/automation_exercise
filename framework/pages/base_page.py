from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.accept_cookies_btn = page.get_by_role("button", name="Consent")
        self.delete_account_btn = page.get_by_role("listitem").filter(has_text="Delete Account")

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def accept_cookies(self):
        self.accept_cookies_btn.click()

    def check_logged_in_name(self, name: str):
        return self.page.get_by_role("listitem").filter(has_text=f"Logged in as {name}")

    def delete_account(self):
        self.delete_account_btn.click()

    