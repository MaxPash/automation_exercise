import pytest
from framework.config.env_selection import get_url


@pytest.fixture(scope="session")
def api_context(playwright):
    base_url = get_url()

    request_context = playwright.request.new_context(
        base_url=base_url
    )

    yield request_context

    request_context.dispose()