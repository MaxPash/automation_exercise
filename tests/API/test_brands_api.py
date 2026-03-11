"""API tests for brands list endpoint (GET /api/brandsList, PUT returns 405)."""

from framework.api.brands_api import BrandsAPI
from framework.schemas.api_responses import BrandsListResponse, MessageResponse


def test_get_all_brands_returns_200(brands_api: BrandsAPI):
    """GET /api/brandsList returns HTTP 200 and responseCode 200."""
    # When: request all brands
    response = brands_api.get_all_brands()

    # Then: HTTP status and body indicate success
    assert response.status == 200
    body = response.json()
    assert body["responseCode"] == 200


def test_brands_schema_validation(brands_api: BrandsAPI):
    """GET /api/brandsList response matches BrandsListResponse schema."""
    # When: request all brands
    response = brands_api.get_all_brands()

    # Then: response validates against schema
    assert response.status == 200
    BrandsListResponse.model_validate(response.json())


def test_brands_list_not_empty(brands_api: BrandsAPI):
    """GET /api/brandsList returns a non-empty brands list."""
    # When: request all brands
    response = brands_api.get_all_brands()

    # Then: brands list is not empty
    assert response.status == 200
    body = BrandsListResponse.model_validate(response.json())
    assert len(body.brands) > 0


def test_put_brands_list_returns_405(brands_api: BrandsAPI):
    """PUT /api/brandsList returns 405 in body and message 'This request method is not supported.'."""
    # When: PUT to brands list (method not allowed)
    response = brands_api.put_brands_list()

    # Then: response body indicates method not allowed (server may return HTTP 200 with responseCode 405)
    body = MessageResponse.model_validate(response.json())
    assert body.responseCode == 405
    assert body.message == "This request method is not supported."
