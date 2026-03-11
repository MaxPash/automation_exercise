"""API client for Automation Exercise products endpoints."""


class ProductsAPI:
    """Client for /api/productsList (GET all products, POST returns 405)."""

    def __init__(self, request_context):
        self.request = request_context

    def get_all_products(self):
        """GET /api/productsList - returns list of all products."""
        return self.request.get("/api/productsList")

    def post_products_list(self):
        """POST /api/productsList - not supported, returns 405."""
        return self.request.post("/api/productsList")
