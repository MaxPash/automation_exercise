import logging

from framework.flows.api_user_flows import ApiUserFlows

def test_login_with_invalid_credentials(pages, api_user_flows: ApiUserFlows, signup_payload: dict, url):
    payload = signup_payload
    
    # Given: Create user via API, Open home, login page and start signup
    email, password = api_user_flows.create_unique_user(payload)
    pages.base.open_home(url)
    pages.login.open()
    
    # When: Fill invalid credentials and submit
    pages.login.log_in(email, "invalid_password")
    
    # Then: Verify error message
    pages.login.should_show_error_message()
    error_msg = pages.login.get_error_message()
    logging.info("Error message: %s", error_msg)

    # Finally: Delete user via API
    api_user_flows.delete_user(email, password)
        