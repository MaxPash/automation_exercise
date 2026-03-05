import logging


def test_register_user(pages, url, signup_data):
    data = signup_data

    logging.info("Starting test: register user")
    logging.info("URL: %s", url)

    # Given: Open home, login page and start signup
    pages.base.open_home(url)
    pages.login.open()
    pages.login.start_signup(data["name"], data["email"])

    # When: Fill required fields and submit
    pages.signup.should_be_opened()
    pages.signup.fill_required_fields(data)
    pages.signup.submit()

    # Then: Verify account created and logged in name
    pages.account_created.should_show_account_created_and_continue()
    pages.base.should_show_logged_in_name(data["name"])
    
    # Finally: Delete account and verify deleted
    pages.base.delete_account()
    pages.delete.should_show_deleted_and_continue()

    pages.base.should_have_base_title()
    logging.info("Test ended: account created and deleted")
