import logging

from framework.flows.api_user_flows import ApiUserFlows


def test_user_lifecycle(api_user_flows: ApiUserFlows, signup_payload: dict):
    payload = signup_payload

    # Given: Create user via API
    email, password = api_user_flows.create_unique_user(payload)
    logging.info("User created with email: %s", email)

    # When: Verify login via API
    api_user_flows.verify_login(email, password)
    logging.info("User verified email: %s", email)

    # Finally: Delete user via API
    api_user_flows.delete_user(email, password)
    logging.info("User deleted with email: %s", email)