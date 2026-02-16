from playwright.sync_api import Page

class AccountCreatedPage:
    def __init__(self, page: Page):
        self.page = page

        self.continue_button = page.locator("[data-qa='continue-button']")
        self.account_created_msg = page.locator("[data-qa='account-created']")
