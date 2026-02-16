from playwright.sync_api import Page

class SignupPage(Page):
    def __init__(self, page: Page):
        self.page = page

        # optional data
        self.title_mr_radio = page.locator("[id='uniform-id_gender1']")
        self.title_mrs_radio = page.locator("[id='uniform-id_gender2']")

        # required data
        self.name_input = page.locator("[data-qa='name']")
        self.password_input = page.locator("[data-qa='password']")
        self.first_name_input = page.locator("[data-qa='first_name']")
        self.last_name_input = page.locator("[data-qa='last_name']")
        self.address1_input = page.locator("[data-qa='address1']")
        self.country_select = page.locator("[data-qa='country']")
        self.state_input = page.locator("[data-qa='state']")
        self.zip_code_input = page.locator("[data-qa='zipcode']")
        self.mobile_input = page.locator("[data-qa='mobile_number']")

        # buttons
        self.submit_button = page.locator("[data-qa='create-account']")

    def fill_name(self, name: str):
        self.name_input.fill(name)

    def fill_password(self, password: str):
        self.password_input.fill(password)

    def fill_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def fill_address1(self, address: str):
        self.address1_input.fill(address)

    def select_country(self, country: str):
        self.country_select.select_option(country)

    def fill_state(self, state: str):
        self.state_input.fill(state)

    def fill_zip_code(self, zip_code: str):
        self.zip_code_input.fill(zip_code)

    def fill_mobile(self, mobile: str):
        self.mobile_input.fill(mobile)

    def create_account(self):
        self.submit_button.click()


