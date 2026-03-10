import logging
from copy import deepcopy
from typing import Tuple

from framework.api.user_api import UserAPI
from framework.schemas import (
    CreateAccountResponse,
    DeleteAccountResponse,
    VerifyLoginResponse,
)
from framework.utils.helper import generate_email


class ApiUserFlows:
    """High-level user flows built on top of UserAPI."""

    def __init__(self, user_api: UserAPI) -> None:
        self.user_api = user_api
        self.logger = logging.getLogger(__name__)

    def create_user(self, payload: dict) -> CreateAccountResponse:
        """Create user via API and assert success. Returns validated response."""
        response = self.user_api.create_user(payload)
        body = response.json()
        validated = CreateAccountResponse.model_validate(body)
        assert validated.responseCode == 201, f"Unexpected create_user code: {validated}"
        self.logger.info("User created via API with email: %s", payload.get("email"))
        return validated

    def create_user_response(self, payload: dict) -> CreateAccountResponse:
        """Create user via API and return validated response without asserting success.
        Use for negative tests that expect non-201 response codes.
        """
        response = self.user_api.create_user(payload)
        body = response.json()
        return CreateAccountResponse.model_validate(body)

    def verify_login(self, email: str, password: str) -> VerifyLoginResponse:
        """Verify login via API and assert success. Returns validated response."""
        response = self.user_api.verify_login(email, password)
        body = response.json()
        validated = VerifyLoginResponse.model_validate(body)
        assert validated.responseCode == 200, f"Unexpected verify_login code: {validated}"
        self.logger.info("User login verified via API for email: %s", email)
        return validated

    def delete_user(self, email: str, password: str) -> DeleteAccountResponse:
        """Delete user via API and assert success. Returns validated response."""
        response = self.user_api.delete_user(email, password)
        body = response.json()
        validated = DeleteAccountResponse.model_validate(body)
        assert validated.responseCode == 200, f"Unexpected delete_user code: {validated}"
        self.logger.info("User deleted via API for email: %s", email)
        return validated

    def create_unique_user(self, base_payload: dict) -> Tuple[str, str]:
        """Create a user with a unique email based on the given payload template.

        Returns a tuple of (email, password) that can be used in tests.
        """
        payload = deepcopy(base_payload)
        email = generate_email()
        password = payload["password"]
        payload["email"] = email

        self.create_user(payload)
        return email, password

    def full_lifecycle(self, base_payload: dict) -> None:
        """Create user, verify login, and delete user via API."""
        payload = deepcopy(base_payload)
        email = generate_email()
        password = payload["password"]
        payload["email"] = email

        self.create_user(payload)
        try:
            self.verify_login(email, password)
        finally:
            self.delete_user(email, password)

