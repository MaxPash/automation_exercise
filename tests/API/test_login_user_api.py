"""API tests for login/verify user endpoint."""

from framework.api.user_api import UserAPI
from framework.data.user_factory import UserFactory
from framework.flows.api_user_flows import ApiUserFlows


def test_login_after_create(user_api: UserAPI, api_user_flows: ApiUserFlows):
    """Create user via API, verify login returns HTTP 200, then delete for isolation."""
    # Given: valid user payload and user created via API
    payload = UserFactory.valid_user()
    api_user_flows.create_user(payload)

    # When: verify login via API
    response = user_api.verify_login(payload["email"], payload["password"])

    # Then: HTTP status is 200 (contract)
    assert response.status == 200

    # Cleanup: delete user to keep tests isolated
    api_user_flows.delete_user(payload["email"], payload["password"])
