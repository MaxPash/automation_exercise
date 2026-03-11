"""Negative API tests for create user endpoint."""

from framework.api.user_api import UserAPI
from framework.data.user_factory import UserFactory
from framework.schemas.api_responses import CreateAccountResponse


def test_create_user_with_invalid_email_returns_error(user_api: UserAPI):
    """Create user with invalid email; verify HTTP 200 and body returns error responseCode 400."""
    payload = UserFactory.invalid_email_user()
    response = user_api.create_user(payload)
    assert response.status == 200
    body = CreateAccountResponse.model_validate(response.json())
    assert body.responseCode == 400


def test_create_user_with_empty_password_returns_error(user_api: UserAPI):
    """Create user with empty password; verify HTTP 200 and body returns error responseCode 400."""
    payload = UserFactory.empty_password_user()
    response = user_api.create_user(payload)
    assert response.status == 200
    body = CreateAccountResponse.model_validate(response.json())
    assert body.responseCode == 400
