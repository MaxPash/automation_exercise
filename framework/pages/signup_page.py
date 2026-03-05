from playwright.sync_api import Page, expect

from framework.pages.base_page import BasePage


class SignupPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._title_mr_radio = page.locator("[id='uniform-id_gender1']")
        self._title_mrs_radio = page.locator("[id='uniform-id_gender2']")
        self._name_input = page.locator("[data-qa='name']")
        self._password_input = page.locator("[data-qa='password']")
        self._first_name_input = page.locator("[data-qa='first_name']")
        self._last_name_input = page.locator("[data-qa='last_name']")
        self._address1_input = page.locator("[data-qa='address']")
        self._country_select = page.locator("[data-qa='country']")
        self._state_input = page.locator("[data-qa='state']")
        self._zip_code_input = page.locator("[data-qa='zipcode']")
        self._mobile_input = page.locator("[data-qa='mobile_number']")
        self._city_input = page.locator("[data-qa='city']")
        self._submit_button = page.locator("[data-qa='create-account']")

    def should_be_opened(self) -> None:
        expect(self.page).to_have_title("Automation Exercise - Signup")

    def fill_required_fields(self, data: dict) -> None:
        """Fill form from dictionary with keys as in test_signup_data.json."""
        self._password_input.fill(data["password"])
        self._first_name_input.fill(data["firstname"])
        self._last_name_input.fill(data["lastname"])
        self._address1_input.fill(data["address1"])
        self._country_select.select_option(data["country"])
        self._state_input.fill(data["state"])
        self._city_input.fill(data["city"])
        self._zip_code_input.fill(data["zipcode"])
        self._mobile_input.fill(data["mobile_number"])

    def submit(self) -> None:
        expect(self._submit_button).to_be_enabled()
        self._submit_button.click()
