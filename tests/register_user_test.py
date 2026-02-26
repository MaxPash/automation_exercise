import logging
from playwright.sync_api import expect
from framework.utils.helper import load_signup_data
from framework.fixtures.pages_fixture import pages
from framework.config.env_selection import get_url


url = get_url()


def test_register_user(pages):
    logging.info("Starting test")
    logging.info(f'URL: {url}')


    base_page = pages["base_page"]
    login_page = pages["login_page"]
    signup_page = pages["signup_page"]
    account_created_page = pages["account_created_page"]
    delete_account_page = pages["delete_account_page"]


    new_name = load_signup_data("name")
    new_email = load_signup_data("email")
    new_password = load_signup_data("password")
    new_first_name = load_signup_data("firstName")
    new_last_name = load_signup_data("lastName")
    new_address1 = load_signup_data("address1")
    new_country = load_signup_data("country")
    new_state = load_signup_data("state")
    new_city = load_signup_data("city")
    new_zip_code = load_signup_data("zipCode")
    new_mobile = load_signup_data("mobileNumber")


    base_page.navigate(url)

    if base_page.accept_cookies():
        logging.info("Cookies accepted")
    else:
        logging.info("No cookie banner present")

    expect(base_page.page).to_have_title("Automation Exercise")

    login_page.go_to_login_page()
    expect(login_page.page).to_have_title("Automation Exercise - Signup / Login")

    login_page.fill_sign_up_name(new_name)
    login_page.fill_sign_up_email(new_email)
    logging.info(f"filled login data on page: {base_page.get_url()}")

    expect(login_page.signup_button).to_be_enabled()
    login_page.sign_up()

    expect(signup_page.page).to_have_title("Automation Exercise - Signup")

    signup_page.fill_password(new_password)
    signup_page.fill_first_name(new_first_name)
    signup_page.fill_last_name(new_last_name)
    signup_page.fill_address1(new_address1)
    signup_page.select_country(new_country)
    signup_page.fill_state(new_state)
    signup_page.fill_city(new_city)
    signup_page.fill_zip_code(new_zip_code)
    signup_page.fill_mobile(new_mobile)
    logging.info(f"filled sign up data on page: {base_page.get_url()}")

    expect(signup_page.submit_button).to_be_enabled()
    signup_page.create_account()
    logging.info(f"account created with name: {new_name}")

    expect(account_created_page.page).to_have_title("Automation Exercise - Account Created")
    expect(account_created_page.account_created_msg).to_be_visible()

    expect(account_created_page.continue_button).to_be_enabled()
    account_created_page.continue_button.click()


    expect(base_page.check_logged_in_name(new_name)).to_be_visible()
    logging.info(f"account name verified: {new_name}")

    base_page.delete_account()
    expect(delete_account_page.account_deleted_msg).to_be_visible()

    expect(delete_account_page.continue_button).to_be_enabled()
    delete_account_page.continue_button.click()
    logging.info("account deleted")

    expect(base_page.page).to_have_title("Automation Exercise")
    logging.info("test ended")


