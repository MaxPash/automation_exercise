"""Negative API tests for create user endpoint."""

from framework.api.user_api import UserAPI
from framework.data.user_factory import UserFactory


def test_create_user_with_invalid_email_returns_error(user_api: UserAPI):
    """Create user with invalid email; verify HTTP 200 and body indicates error (responseCode != 201)."""
    payload = UserFactory.invalid_email_user()
    response = user_api.create_user(payload)
    assert response.status == 200  # API returns 200; error is in body
    body = response.json()
    assert body.get("responseCode") != 201


def test_create_user_with_empty_password_returns_error(user_api: UserAPI):
    """Create user with empty password; verify HTTP 200 and body indicates error (responseCode != 201)."""
    payload = UserFactory.empty_password_user()
    response = user_api.create_user(payload)
    assert response.status == 200  # API returns 200; error is in body
    body = response.json()
    assert body.get("responseCode") != 201
