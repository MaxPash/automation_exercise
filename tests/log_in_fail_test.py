import logging

def test_login_with_invalid_credentials(pages, url, signup_data):
    data = signup_data

    logging.info("Starting test: login with invalid credentials")

    # Given: Open home, login page and start signup
    pages.base.open_home(url)
    pages.login.open()
    # When: Fill invalid credentials and submit
    pages.login.log_in(data["email"], "invalid_password")
    # Then: Verify error message
    pages.login.should_show_error_message()
    error_msg = pages.login.get_error_message()
    
    logging.info("Error message: %s", error_msg)
    logging.info("Test ended: login with invalid credentials")