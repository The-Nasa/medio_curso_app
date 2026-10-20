from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.auth import AuthResponse, LoginRequest, RegisterRequest
from app.services.auth_service import AuthError, login, register

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_endpoint(data: RegisterRequest, db: Session = Depends(get_db)) -> dict[str, object]:
    try:
        user = register(db, data)
    except AuthError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return {"id": user.id, "name": user.name, "email": user.email, "role": user.role}


@router.post("/login", response_model=AuthResponse)
def login_endpoint(data: LoginRequest, db: Session = Depends(get_db)) -> AuthResponse:
    try:
        token = login(db, data)
    except AuthError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc
    return AuthResponse(access_token=token)
