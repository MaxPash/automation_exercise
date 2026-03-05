import logging

from framework.flows.api_user_flows import ApiUserFlows


def test_register_via_api_log_in_via_ui(pages, api_user_flows: ApiUserFlows, signup_payload: dict, url):
    payload = signup_payload
    name = payload["name"]
    # Given: Create user via API
    email, password = api_user_flows.create_unique_user(payload)
    logging.info("User created with email: %s and name: %s", email, name)
    # When: Login via UI
    pages.base.open_home(url)
    pages.login.open()
    pages.login.log_in(email, password)
    # Then: Verify logged in name
    pages.base.should_show_logged_in_name(name)
    logging.info("User name verified: %s", name)
    # Finally: Delete user via API
    api_user_flows.delete_user(email, password)
    logging.info("User deleted with email: %s", email)
