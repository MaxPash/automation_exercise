"""Negative API tests for create user endpoint."""

from framework.api.user_api import UserAPI
from framework.data.user_factory import UserFactory


def test_create_user_with_invalid_email_returns_error(user_api: UserAPI):
    """Create user with invalid email; API must return error response code."""
    payload = UserFactory.invalid_email_user()
    response = user_api.create_user(payload)
    body = response.json()
    # API returns error, not success (201)
    assert body.get("responseCode") != 201


def test_create_user_with_empty_password_returns_error(user_api: UserAPI):
    """Create user with empty password; API must return error response code."""
    payload = UserFactory.empty_password_user()
    response = user_api.create_user(payload)
    body = response.json()
    # API returns error, not success (201)
    assert body.get("responseCode") != 201
