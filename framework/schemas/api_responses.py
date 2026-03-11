"""Pydantic schemas for Automation Exercise API responses.

Response structure per https://www.automationexercise.com/api_list:
responseCode (int) and message (str).
"""

from pydantic import BaseModel


class CreateAccountResponse(BaseModel):
    """Response for POST /api/createAccount. Success: 201, message 'User created!'."""

    responseCode: int
    message: str


class VerifyLoginResponse(BaseModel):
    """Response for POST /api/verifyLogin. Success: 200 'User exists!', 404 'User not found!'."""

    responseCode: int
    message: str


class DeleteAccountResponse(BaseModel):
    """Response for DELETE /api/deleteAccount. Success: 200, message 'Account deleted!'."""

    responseCode: int
    message: str


# --- Products List API (GET /api/productsList) ---


class ProductCategoryUsertype(BaseModel):
    """Nested usertype inside product category."""

    usertype: str


class ProductCategory(BaseModel):
    """Product category with usertype and category name."""

    usertype: ProductCategoryUsertype
    category: str


class Product(BaseModel):
    """Single product from GET /api/productsList."""

    id: int
    name: str
    price: str
    brand: str
    category: ProductCategory


class ProductsListResponse(BaseModel):
    """Response for GET /api/productsList. responseCode 200, products list."""

    responseCode: int
    products: list[Product]


class MessageResponse(BaseModel):
    """Generic response with responseCode and message (e.g. 405 Method Not Allowed)."""

    responseCode: int
    message: str
