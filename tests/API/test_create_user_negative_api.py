"""Negative API tests for create user endpoint."""

from framework.data.user_factory import UserFactory
from framework.flows.api_user_flows import ApiUserFlows


def test_create_user_with_invalid_email_returns_error(api_user_flows: ApiUserFlows):
    """Create user with invalid email; API must return error response code."""
    payload = UserFactory.invalid_email_user()
    result = api_user_flows.create_user_response(payload)
    assert result.responseCode != 201


def test_create_user_with_empty_password_returns_error(api_user_flows: ApiUserFlows):
    """Create user with empty password; API must return error response code."""
    payload = UserFactory.empty_password_user()
    result = api_user_flows.create_user_response(payload)
    assert result.responseCode != 201
