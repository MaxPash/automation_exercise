"""API tests for create user endpoint."""

from framework.data.user_factory import UserFactory
from framework.flows.api_user_flows import ApiUserFlows


def test_create_user_returns_201(api_user_flows: ApiUserFlows):
    """Create user via API, verify 201, then delete for isolation."""
    # Given: valid user payload
    payload = UserFactory.valid_user()

    # When: create user via API
    result = api_user_flows.create_user(payload)

    # Then: response code is 201
    assert result.responseCode == 201

    # Cleanup: delete user to keep tests isolated
    api_user_flows.delete_user(payload["email"], payload["password"])
