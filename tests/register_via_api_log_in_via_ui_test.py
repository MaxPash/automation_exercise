import logging

from framework.flows.api_user_flows import ApiUserFlows


def test_api_create_ui_login_delete(pages, api_context, url):
    user_api = UserAPI(api_context)

    with open("framework/data/test_signup_data.json") as f:
        payload = json.load(f)

    email = generate_email()
    payload["email"] = email
    password = payload["password"]
    name = payload["name"]
    # Given: Create user via API
    email, password = api_user_flows.create_unique_user(payload)
    logging.info("account created with name: %s", name)
    # When: Login via UI
    pages.base.open_home(url)
    pages.login.open()
    pages.login.log_in(email, password)
    # Then: Verify logged in name
    pages.base.should_show_logged_in_name(name)
    logging.info("account name verified: %s", name)
    # Finally: Delete user via API
    api_user_flows.delete_user(email, password)
    logging.info("account deleted")
