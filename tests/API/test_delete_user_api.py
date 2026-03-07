"""API tests for delete user endpoint."""

from framework.api.user_api import UserAPI
from framework.data.user_factory import UserFactory
from framework.flows.api_user_flows import ApiUserFlows


def test_delete_user_returns_200(
    api_user_flows: ApiUserFlows, user_api: UserAPI
):
    """Create user via API, delete via API, verify response code 200."""
    # Given: valid user payload and user created via API
    payload = UserFactory.valid_user()
    api_user_flows.create_user(payload)

    # When: delete user via API
    response = user_api.delete_user(payload["email"], payload["password"])

    # Then: response code is 200
    assert response.json().get("responseCode") == 200
