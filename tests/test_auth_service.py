from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db.base import Base
from app.schemas.auth import LoginRequest, RegisterRequest
from app.services.auth_service import AuthError, login, register


def make_session() -> Session:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    return Session(engine)


def test_register_hashes_password_and_login_returns_token() -> None:
    db = make_session()

    user = register(db, RegisterRequest(name="Ana", email="ana@test.com", password="secret123"))
    token = login(db, LoginRequest(email="ana@test.com", password="secret123"))

    assert user.email == "ana@test.com"
    assert user.password_hash != "secret123"
    assert token


def test_register_rejects_duplicate_email() -> None:
    db = make_session()
    data = RegisterRequest(name="Ana", email="ana@test.com", password="secret123")
    register(db, data)

    try:
        register(db, data)
    except AuthError as error:
        assert "registrado" in str(error)
    else:
        raise AssertionError("Se esperaba AuthError")
