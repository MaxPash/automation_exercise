import pytest

from framework.config.env_selection import get_url
from framework.utils.helper import load_signup_payload, generate_email
from framework.fixtures.pages_fixture import *
from framework.fixtures.api_fixture import *


@pytest.fixture
def url() -> str:
    return get_url()


@pytest.fixture
def signup_data() -> dict:
    """Data for registration with unique email."""
    data = load_signup_payload()
    data["email"] = generate_email()
    return data