# Convenciones de Python

- Usar Python 3.12+, type hints y funciones pequeñas.
- Seguir PEP 8; Ruff es la autoridad de formato y lint.
- Usar nombres `snake_case`, clases `PascalCase` y constantes `UPPER_CASE`.
- No guardar secretos en el repositorio; usar variables de entorno.
- Validar entradas con Pydantic.
- No capturar excepciones genéricas sin registrar o traducir el error.
- Usar transacciones para operaciones que cambien datos.
- No mezclar lógica HTTP con reglas de negocio.
- Escribir pruebas deterministas, aisladas y legibles.
- No usar `print()` para depuración permanente.
- Los workflows de despliegue viven en `.github/workflows/`.
- No guardar secretos en workflows; usar GitHub Actions Secrets.
- El despliegue se ejecuta solo después de que CI pase y la rama esté revisada.
