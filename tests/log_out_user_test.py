import logging

from framework.flows.api_user_flows import ApiUserFlows

def test_log_out_user(pages, api_user_flows: ApiUserFlows, signup_payload: dict, url):
    payload = signup_payload
    name = payload["name"]
    
    # Given: Create user via API
    email, password = api_user_flows.create_unique_user(payload)
        
    # When: Login via UI
    pages.base.open_home(url)
    pages.login.open()
    pages.login.log_in(email, password)
    
    # Then: Verify logged in name and log out
    pages.base.should_show_logged_in_name(name)
    logging.info("User name verified: %s", name)
    pages.base.log_out()
    pages.login.should_show_login_page()
    logging.info("User on log in page")
    
    # Finally: Delete user via API
    api_user_flows.delete_user(email, password)
    
    
