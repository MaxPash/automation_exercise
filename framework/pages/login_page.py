from playwright.sync_api import Page

class LoginPage(Page):
    def __init__(self, page: Page):
        self.page = page

        # Log in
        self.login_email_input = page.locator("[data-qa='login-email']")
        self.login_password_input = page.locator("[data-qa='login-password']")
        self.login_button = page.locator("[data-qa='login-button']")

        #Sign up
        self.signup_name = page.locator("[data-qa='signup-name']")
        self.signup_email = page.locator("[data-qa='signup-email']")
        self.signup_button = page.locator("[data-qa='signup-button']")

    def fill_login_email(self, name):
        self.login_email_input.fill(name)

    def fill_login_password(self, password):
        self.login_password_input.fill(password)

    def log_in(self):
        self.login_button.click()

    def fill_sign_up_name(self, name):
        self.signup_name.fill(name)

    def fill_sign_up_email(self, email):
        self.signup_email.fill(email)

    def sign_up(self):
        self.signup_button.click()
