from playwright.sync_api import Page

class DeleteAccountPage:
    def __init__(self, page: Page):
        self.page = page

        self.account_deleted_msg = page.locator("[data-qa='account-deleted']")
        self.continue_button = page.locator("[data-qa='continue-button']")