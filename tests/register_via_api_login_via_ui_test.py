import json
import time
import logging
from framework.api.user_api import UserAPI
from framework.config.env_selection import get_url
from framework.utils.helper import generate_email
from playwright.sync_api import expect



url = get_url()

def test_api_create_ui_login_delete(pages, api_context):

    # init api
    user_api = UserAPI(api_context)

    # load data
    with open("framework/data/test_signup_data.json") as f:
        payload = json.load(f)

    # make email unique
    email = generate_email()
    payload["email"] = email
    password = payload["password"]
    name = payload["name"]

    # create user via api
    create_response = user_api.create_user(payload)
    assert create_response.json()["responseCode"] == 201
    logging.info(f"account created with name: {name}")

    try:
        # login via ui
        base_page = pages["base_page"]
        login_page = pages["login_page"]

        base_page.navigate(url)
        base_page.handle_cookies()
        base_page.should_have_base_title()

        login_page.go_to_login_page()
        login_page.should_have_login_title()

        login_page.fill_login_email(email)
        login_page.fill_login_password(password)
        login_page.log_in()

        # check login
        expect(base_page.check_logged_in_name(name)).to_be_visible()
        logging.info(f"account name verified: {name}")

    finally:
        # delete via api
        delete_response = user_api.delete_user(email, password)
        assert delete_response.json()["responseCode"] == 200
        logging.info(f"account deleted")