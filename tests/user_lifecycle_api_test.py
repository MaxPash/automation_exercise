import json
import logging

from framework.api.user_api import UserAPI
from framework.utils.helper import generate_email

def test_user_lifecycle(api_context):

    user_api = UserAPI(api_context)

    with open("framework/data/test_signup_data.json") as f:
        payload = json.load(f)

    email = generate_email()
    password = payload["password"]
    payload["email"] = email

    # Given: Create user via API
    create_response = user_api.create_user(payload)
    assert create_response.json()["responseCode"] == 201
    logging.info(f"User created with email: {email}")
    # When: Verify login via API
    login_response = user_api.verify_login(email, password)
    assert login_response.json()["responseCode"] == 200
    logging.info(f"User verified email: {email}")
    # Finally: Delete user via API
    delete_response = user_api.delete_user(email, password)
    assert delete_response.json()["responseCode"] == 200
    logging.info(f"User deleted with email: {email}")