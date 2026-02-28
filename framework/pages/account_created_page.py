from playwright.sync_api import Page
from playwright.sync_api import expect

class AccountCreatedPage:
    def __init__(self, page: Page):
        self.page = page

        self.account_created_msg = page.locator("[data-qa='account-created']")
        self.continue_button = page.locator("[data-qa='continue-button']")

    def should_have_account_created_title(self):
        expect(self.page).to_have_title("Automation Exercise - Account Created")