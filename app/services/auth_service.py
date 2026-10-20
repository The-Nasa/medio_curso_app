from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.repositories import user_repository
from app.schemas.auth import LoginRequest, RegisterRequest


class AuthError(Exception):
    pass


def register(db: Session, data: RegisterRequest) -> User:
    email = str(data.email).lower()
    if user_repository.get_by_email(db, email):
        raise AuthError("El correo ya está registrado")
    return user_repository.create(
        db,
        User(name=data.name, email=email, password_hash=hash_password(data.password)),
    )


def login(db: Session, data: LoginRequest) -> str:
    user = user_repository.get_by_email(db, str(data.email).lower())
    if user is None or not verify_password(data.password, user.password_hash):
        raise AuthError("Credenciales inválidas")
    return create_access_token(user.id, user.role)
