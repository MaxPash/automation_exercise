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
        expected_status = 200  # API returns 200; body contains responseCode 201 for success
        actual_status = response.status
        if actual_status != expected_status:
            body_preview = response.text()[:200] if response.text() else ""
            raise AssertionError(
                f"create_user: expected HTTP {expected_status}, got {actual_status}. Body: {body_preview!r}"
            )
        body = response.json()
        validated = CreateAccountResponse.model_validate(body)
        if validated.responseCode != 201:
            raise AssertionError(
                f"create_user: expected responseCode 201, got {validated.responseCode}"
            )
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
        expected_status = 200
        actual_status = response.status
        if actual_status != expected_status:
            body_preview = response.text()[:200] if response.text() else ""
            raise AssertionError(
                f"verify_login: expected HTTP {expected_status}, got {actual_status}. Body: {body_preview!r}"
            )
        body = response.json()
        validated = VerifyLoginResponse.model_validate(body)
        if validated.responseCode != 200:
            raise AssertionError(
                f"verify_login: expected responseCode 200, got {validated.responseCode}"
            )
        self.logger.info("User login verified via API for email: %s", email)
        return validated

    def delete_user(self, email: str, password: str) -> DeleteAccountResponse:
        """Delete user via API and assert success. Returns validated response."""
        response = self.user_api.delete_user(email, password)
        expected_status = 200
        actual_status = response.status
        if actual_status != expected_status:
            body_preview = response.text()[:200] if response.text() else ""
            raise AssertionError(
                f"delete_user: expected HTTP {expected_status}, got {actual_status}. Body: {body_preview!r}"
            )
        body = response.json()
        validated = DeleteAccountResponse.model_validate(body)
        if validated.responseCode != 200:
            raise AssertionError(
                f"delete_user: expected responseCode 200, got {validated.responseCode}"
            )
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

