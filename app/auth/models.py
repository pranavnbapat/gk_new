from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access: str
    refresh: str

class LogoutRequest(BaseModel):
    refresh: str

class TokenValidationRequest(BaseModel):
    token: str
    token_type: str = "access"
