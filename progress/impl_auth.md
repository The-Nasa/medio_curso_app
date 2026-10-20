# Implementación — auth

**Estado:** completado.

## Implementado

- Modelo SQLAlchemy `User`.
- Migración Alembic de usuarios.
- Registro y login.
- Hash Argon2.
- Tokens JWT.
- Schemas Pydantic.
- Repositorio y servicio de autenticación.
- Endpoints `/api/auth/register` y `/api/auth/login`.
- Pruebas unitarias y de servicio.

## Verificación

- Ruff: PASS.
- Mypy: PASS.
- Pytest: 6 passed.
- Alembic: PASS.

## Trazabilidad

- R1 → `test_register_hashes_password_and_login_returns_token`
- R2 → `test_register_rejects_duplicate_email`
- R3 → `test_register_hashes_password_and_login_returns_token`
- R4 → `test_jwt_contains_user_and_role`
- R5 → `test_password_is_hashed_and_verifies`
- R6 → `test_jwt_contains_user_and_role`
- R7 → `test_jwt_contains_user_and_role`
- R8 → suite de pytest
