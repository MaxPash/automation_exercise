"""API tests for delete user endpoint."""

from framework.api.user_api import UserAPI
from framework.data.user_factory import UserFactory
from framework.flows.api_user_flows import ApiUserFlows
from framework.schemas.api_responses import DeleteAccountResponse


def test_delete_user_returns_200(user_api: UserAPI, api_user_flows: ApiUserFlows):
    """Create user via API, delete via API, verify HTTP 200 and business success (responseCode 200)."""
    # Given: valid user payload and user created via API
    payload = UserFactory.valid_user()
    api_user_flows.create_user(payload)

    # When: delete user via API
    response = user_api.delete_user(payload["email"], payload["password"])

    # Then: HTTP status is 200 and body indicates success
    assert response.status == 200
    body = DeleteAccountResponse.model_validate(response.json())
    assert body.responseCode == 200
