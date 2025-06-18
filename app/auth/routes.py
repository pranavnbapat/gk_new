from fastapi import APIRouter, Depends
from app.auth.models import LoginRequest, TokenResponse, LogoutRequest, TokenValidationRequest
from app.auth.services import login_user
from app.auth.jwt import validate_token
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/login/", response_model=TokenResponse)
def login(data: LoginRequest):
    return login_user(data.username, data.password)

@router.post("/logout/")
def logout(data: LogoutRequest):
    # No blacklist without Redis or DB, so just return success
    return {"success": "Logged out (noop in stateless mode)"}

@router.post("/validate_token/")
def validate_token_route(data: TokenValidationRequest):
    valid, result = validate_token(data.token, data.token_type)
    if not valid:
        return JSONResponse(status_code=400, content={"error": result})
    return {"success": True, "remaining_time_in_seconds": result}
