# Verificación

Antes de marcar una feature como `done`, ejecutar:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy app
python -m pytest -q --cov=app --cov-fail-under=80
```

Cada requisito `R<n>` debe estar relacionado con una prueba concreta. Las pruebas de API deben usar `TestClient` o `httpx` y una base de datos de prueba; nunca deben depender de datos reales.
