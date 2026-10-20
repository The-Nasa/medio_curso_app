from app.api.dependencies import get_current_user
from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


def test_password_is_hashed_and_verifies() -> None:
    hashed = hash_password("secret123")

    assert hashed != "secret123"
    assert verify_password("secret123", hashed)
    assert not verify_password("incorrecta", hashed)


def test_jwt_contains_user_and_role() -> None:
    token = create_access_token(7, "client")
    payload = decode_access_token(token)

    assert payload["sub"] == "7"
    assert payload["role"] == "client"


def test_invalid_token_is_rejected() -> None:
    try:
        get_current_user(None)
    except Exception as error:
        assert getattr(error, "status_code", None) == 401
    else:
        raise AssertionError("Se esperaba rechazo de autenticación")
