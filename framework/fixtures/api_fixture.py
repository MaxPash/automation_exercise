import pytest

from framework.api.products_api import ProductsAPI
from framework.api.user_api import UserAPI
from framework.config.env_selection import get_url
from framework.flows.api_user_flows import ApiUserFlows
from framework.utils.helper import load_signup_payload


@pytest.fixture(scope="session")
def api_context(playwright):
    base_url = get_url()

    request_context = playwright.request.new_context(base_url=base_url)

    yield request_context

    request_context.dispose()


@pytest.fixture
def user_api(api_context) -> UserAPI:
    return UserAPI(api_context)


@pytest.fixture
def products_api(api_context) -> ProductsAPI:
    return ProductsAPI(api_context)


@pytest.fixture
def api_user_flows(user_api: UserAPI) -> ApiUserFlows:
    return ApiUserFlows(user_api)


@pytest.fixture
def signup_payload() -> dict:
    """Base payload for user signup API calls."""
    return load_signup_payload()