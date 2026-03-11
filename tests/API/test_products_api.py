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
    assert response.status == 200
    body = MessageResponse.model_validate(response.json())
    assert body.responseCode == 405
    assert body.message == "This request method is not supported."


# --- Search Product API (POST /api/searchProduct) ---


def test_search_product_returns_results(products_api: ProductsAPI):
    """POST /api/searchProduct with valid term returns 200 and products list."""
    # When: search with existing term (e.g. "top")
    response = products_api.search_product("top")

    # Then: success and list of products (non-empty for this query)
    assert response.status == 200
    body = ProductsListResponse.model_validate(response.json())
    assert body.responseCode == 200
    assert len(body.products) > 0


def test_search_product_results_match_query(products_api: ProductsAPI):
    """POST /api/searchProduct results contain the search term in name, brand or category."""
    # When: search for "tshirt"
    response = products_api.search_product("tshirt")

    # Then: each product has query substring in name, brand or category
    assert response.status == 200
    body = ProductsListResponse.model_validate(response.json())
    assert body.responseCode == 200
    query = "tshirt"
    query_lower = query.lower()
    for product in body.products:
        searchable = [
            product.name,
            product.brand,
            product.category.category,
            product.category.usertype.usertype,
        ]
        assert any(
            query_lower in (s or "").lower() for s in searchable
        ), f"Product {product.name} does not contain '{query}' in name, brand or category"


def test_search_product_no_results(products_api: ProductsAPI):
    """POST /api/searchProduct with non-matching term returns 200 and empty products list."""
    # When: search for term that matches nothing
    response = products_api.search_product("nonexistentxyz123")

    # Then: success with empty products list
    assert response.status == 200
    body = ProductsListResponse.model_validate(response.json())
    assert body.responseCode == 200
    assert len(body.products) == 0


def test_search_product_empty_query(products_api: ProductsAPI):
    """POST /api/searchProduct without search_product returns 400 and expected message."""
    # When: POST without search_product parameter (API 6)
    response = products_api.search_product_without_param()

    # Then: response body indicates bad request (server may return HTTP 200 with responseCode 400)
    assert response.status == 200
    body = MessageResponse.model_validate(response.json())
    assert body.responseCode == 400
    assert body.message == "Bad request, search_product parameter is missing in POST request."
