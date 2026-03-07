"""API tests for login/verify user endpoint."""

from framework.data.user_factory import UserFactory
from framework.flows.api_user_flows import ApiUserFlows


def test_login_after_create(api_user_flows: ApiUserFlows):
    """Create user via API, verify login, then delete for isolation."""
    # Given: valid user payload and user created via API
    payload = UserFactory.valid_user()
    api_user_flows.create_user(payload)

    # When: verify login via API
    api_user_flows.verify_login(payload["email"], payload["password"])

    # Cleanup: delete user to keep tests isolated
    api_user_flows.delete_user(payload["email"], payload["password"])
