import logging

from framework.flows.api_user_flows import ApiUserFlows

def test_register_with_existing_email(pages, api_user_flows: ApiUserFlows, signup_payload: dict, url):
    payload = signup_payload
    name = payload["name"]
        
    # Given: Create user via API
    email, password = api_user_flows.create_unique_user(payload)
    
    # When: Register with existing email
    pages.base.open_home(url)
    pages.login.open()
    pages.login.start_signup(name, email)
    
    # Then: Verify error message
    pages.signup.should_show_error_message()
    error_msg = pages.signup.get_error_message()
    logging.info("Error message: %s", error_msg)
    
    # Finally: Delete user via API
    api_user_flows.delete_user(email, password)
    