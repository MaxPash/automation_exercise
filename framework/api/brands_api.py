"""API client for Automation Exercise brands endpoints."""


class BrandsAPI:
    """Client for /api/brandsList (GET all brands, PUT returns 405)."""

    def __init__(self, request_context):
        self.request = request_context

    def get_all_brands(self):
        """GET /api/brandsList - returns list of all brands."""
        return self.request.get("/api/brandsList")

    def put_brands_list(self):
        """PUT /api/brandsList - not supported, returns 405."""
        return self.request.put("/api/brandsList")
