import pytest
from playwright.sync_api import Page
from framework.pages.base_page import BasePage
from framework.pages.login_page import LoginPage
from framework.pages.signup_page import SignupPage
from framework.pages.account_created_page import AccountCreatedPage

@pytest.fixture(scope="function")
def pages(page: Page):
    web_page = {
        "base_page": BasePage(page),
        "login_page": LoginPage(page),
        "signup_page": SignupPage(page),
        "account_created_page": AccountCreatedPage(page),
    }

    return web_page