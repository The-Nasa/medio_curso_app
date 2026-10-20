# Design — auth

## Responsable

Persona 1.

## Alcance

Implementar autenticación básica para clientes y administradores usando FastAPI, SQLAlchemy, Pydantic y JWT.

## Archivos previstos

```text
app/models/user.py
app/schemas/auth.py
app/repositories/user_repository.py
app/services/auth_service.py
app/api/auth.py
app/core/security.py
app/api/dependencies.py
alembic/versions/<revision>_create_users.py
tests/test_auth.py
```

## Decisiones técnicas

- La contraseña se almacenará con Argon2 mediante `pwdlib`.
- El token será JWT y contendrá el identificador del usuario y su rol.
- La validación de entrada se hará con esquemas Pydantic.
- La API devolverá `409` para correo duplicado, `401` para credenciales inválidas y `401` para tokens inválidos.
- La lógica de negocio vivirá en `auth_service.py`; el endpoint no accederá directamente a la base de datos.
- El primer usuario administrador se creará mediante una estrategia documentada, no mediante una ruta pública especial.

## Alternativa descartada

Se descarta guardar sesiones en memoria porque no funcionaría correctamente cuando existan varias instancias de la API.
