import logging
from copy import deepcopy
from typing import Tuple

from framework.api.user_api import UserAPI
from framework.utils.helper import generate_email


class ApiUserFlows:
    """High-level user flows built on top of UserAPI."""

    def __init__(self, user_api: UserAPI) -> None:
        self.user_api = user_api
        self.logger = logging.getLogger(__name__)

    def create_user(self, payload: dict):
        """Create user via API and assert success."""
        response = self.user_api.create_user(payload)
        body = response.json()
        assert body.get("responseCode") == 201, f"Unexpected create_user code: {body}"
        self.logger.info("User created via API with email: %s", payload.get("email"))
        return response

    def verify_login(self, email: str, password: str) -> None:
        """Verify login via API and assert success."""
        response = self.user_api.verify_login(email, password)
        body = response.json()
        assert body.get("responseCode") == 200, f"Unexpected verify_login code: {body}"
        self.logger.info("User login verified via API for email: %s", email)

    def delete_user(self, email: str, password: str) -> None:
        """Delete user via API and assert success."""
        response = self.user_api.delete_user(email, password)
        body = response.json()
        assert body.get("responseCode") == 200, f"Unexpected delete_user code: {body}"
        self.logger.info("User deleted via API for email: %s", email)

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

