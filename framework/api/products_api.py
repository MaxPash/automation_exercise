"""API client for Automation Exercise products endpoints."""


class ProductsAPI:
    """Client for /api/productsList and /api/searchProduct."""

    def __init__(self, request_context):
        self.request = request_context

    def get_all_products(self):
        """GET /api/productsList - returns list of all products."""
        return self.request.get("/api/productsList")

    def post_products_list(self):
        """POST /api/productsList - not supported, returns 405."""
        return self.request.post("/api/productsList")

    def search_product(self, search_term: str):
        """POST /api/searchProduct with search_product parameter."""
        return self.request.post("/api/searchProduct", form={"search_product": search_term})

    def search_product_without_param(self):
        """POST /api/searchProduct without search_product (returns 400)."""
        return self.request.post("/api/searchProduct")
