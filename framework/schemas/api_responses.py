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
