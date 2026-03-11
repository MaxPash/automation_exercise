"""API tests for products list endpoint (GET /api/productsList, POST returns 405)."""

from framework.api.products_api import ProductsAPI
from framework.schemas.api_responses import MessageResponse, ProductsListResponse


def test_get_all_products_returns_200(products_api: ProductsAPI):
    """GET /api/productsList returns HTTP 200 and responseCode 200."""
    # When: request all products
    response = products_api.get_all_products()

    # Then: HTTP status and body indicate success
    assert response.status == 200
    body = response.json()
    assert body["responseCode"] == 200


def test_products_schema_validation(products_api: ProductsAPI):
    """GET /api/productsList response matches ProductsListResponse schema."""
    # When: request all products
    response = products_api.get_all_products()

    # Then: response validates against schema
    assert response.status == 200
    ProductsListResponse.model_validate(response.json())


def test_products_list_not_empty(products_api: ProductsAPI):
    """GET /api/productsList returns a non-empty products list."""
    # When: request all products
    response = products_api.get_all_products()

    # Then: products list is not empty
    assert response.status == 200
    body = ProductsListResponse.model_validate(response.json())
    assert len(body.products) > 0


def test_post_products_list_returns_405(products_api: ProductsAPI):
    """POST /api/productsList returns 405 in body and message 'This request method is not supported.'."""
    # When: POST to products list (method not allowed)
    response = products_api.post_products_list()

    # Then: response body indicates method not allowed (server may return HTTP 200 with responseCode 405)
    body = MessageResponse.model_validate(response.json())
    assert body.responseCode == 405
    assert body.message == "This request method is not supported."
