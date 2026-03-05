import json
import logging

from framework.api.user_api import UserAPI
from framework.utils.helper import generate_email


def test_api_create_ui_login_delete(pages, api_context, url):
    user_api = UserAPI(api_context)

    with open("framework/data/test_signup_data.json") as f:
        payload = json.load(f)

    email = generate_email()
    payload["email"] = email
    password = payload["password"]
    name = payload["name"]

    create_response = user_api.create_user(payload)
    assert create_response.json()["responseCode"] == 201
    logging.info("account created with name: %s", name)

    try:
        pages.base.open_home(url)
        pages.login.open()
        pages.login.log_in(email, password)
        pages.base.should_show_logged_in_name(name)
        logging.info("account name verified: %s", name)
    finally:
        delete_response = user_api.delete_user(email, password)
        assert delete_response.json()["responseCode"] == 200
        logging.info("account deleted")
