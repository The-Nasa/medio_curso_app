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
- Los recursos de infraestructura se definen en Terraform y se revisan mediante `terraform plan`.
- No guardar `.tfvars` con secretos; usar variables de entorno o el gestor de secretos del proveedor cloud.
- No ejecutar `terraform apply` desde una rama sin revisión.
