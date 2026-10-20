# Migraciones

Crear una migración con:

```bash
alembic revision -m "descripcion"
alembic upgrade head
```

Las migraciones deben revisarse antes de ejecutarse en producción.
