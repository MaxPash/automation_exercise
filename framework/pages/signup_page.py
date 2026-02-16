from playwright.sync_api import Page

class SignupPage(Page):
    def __init__(self, page: Page):
        self.page = page

        self.title_mr_radio = page.locator("[id='uniform-id_gender1']")
        self.title_mrs_radio = page.locator("[id='uniform-id_gender2']")

        self.name_input = page.locator("[id='name']")