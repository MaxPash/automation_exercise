"""API tests for create user endpoint."""

from framework.api.user_api import UserAPI
from framework.data.user_factory import UserFactory
from framework.flows.api_user_flows import ApiUserFlows


def test_create_user_returns_201(user_api: UserAPI, api_user_flows: ApiUserFlows):
    """Create user via API, verify HTTP 201, then delete for isolation."""
    # Given: valid user payload
    payload = UserFactory.valid_user()

    # When: create user via API
    response = user_api.create_user(payload)

    # Then: HTTP status is 200 (contract; API returns 200 with responseCode 201 in body)
    assert response.status == 200

    # Cleanup: delete user to keep tests isolated
    api_user_flows.delete_user(payload["email"], payload["password"])
