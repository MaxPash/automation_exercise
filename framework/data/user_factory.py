"""Factory for generating test user registration payloads."""

from framework.utils.helper import generate_email, load_signup_payload


class UserFactory:
    """Builds signup payload dictionaries for tests. No API calls."""

    @staticmethod
    def valid_user() -> dict:
        """Return a payload with a unique email; all other fields from template."""
        payload = load_signup_payload()
        result = payload.copy()
        result["email"] = generate_email()
        return result

    @staticmethod
    def invalid_email_user() -> dict:
        """Return a payload with an invalid email value."""
        payload = load_signup_payload()
        result = payload.copy()
        result["email"] = "invalid-email"
        return result

    @staticmethod
    def empty_password_user() -> dict:
        """Return a payload with an empty password."""
        payload = load_signup_payload()
        result = payload.copy()
        result["password"] = ""
        return result
