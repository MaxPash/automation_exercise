from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.accept_cookies_btn = page.get_by_role("button", name="Consent")

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def accept_cookies(self):
        self.accept_cookies_btn.click()
