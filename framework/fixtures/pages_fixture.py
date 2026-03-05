from dataclasses import dataclass

import pytest
from playwright.sync_api import Page

from framework.pages.base_page import BasePage
from framework.pages.login_page import LoginPage
from framework.pages.signup_page import SignupPage
from framework.pages.account_created_page import AccountCreatedPage
from framework.pages.delete_account_page import DeleteAccountPage


@dataclass
class Pages:
    base: BasePage
    login: LoginPage
    signup: SignupPage
    account_created: AccountCreatedPage
    delete: DeleteAccountPage


@pytest.fixture(scope="function")
def pages(page: Page) -> Pages:
    return Pages(
        base=BasePage(page),
        login=LoginPage(page),
        signup=SignupPage(page),
        account_created=AccountCreatedPage(page),
        delete=DeleteAccountPage(page),
    )
