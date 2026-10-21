# Requirements — deployment

## R1 — Gestión segura de configuración y secretos
EL SISTEMA DEBE configurarse exclusivamente a través de variables de entorno y NUNCA debe almacenar credenciales, claves secretas ni tokens en el repositorio o en los artefactos de código fuente.

## R2 — Contenedorización reproducible de la API
CUANDO se construya la imagen de contenedor para la API, el sistema DEBE contar con un `Dockerfile` reproducible y optimizado basado en Python 3.12 que empaquete la aplicación e instale sus dependencias sin incluir archivos innecesarios ni secretos.

## R3 — Integración continua de validaciones y pruebas
CUANDO se realice un push o pull request, el sistema DEBE ejecutar automáticamente un workflow de GitHub Actions que valide el formato y linting con Ruff, el chequeo estático de tipos con mypy y la suite completa de pruebas con pytest.

## R4 — Workflow de construcción de imagen Docker
CUANDO se ejecute la canalización de entrega continua, el sistema DEBE disponer de un workflow de GitHub Actions que construya y verifique la imagen Docker de la API asegurando su integridad.

## R5 — Configuración para PostgreSQL de producción
EL SISTEMA DEBE disponer de documentación y configuración explícita para la conexión y operación con PostgreSQL en entorno de producción, detallando variables requeridas y políticas de aislamiento de red.

## R6 — Ejecución automática de migraciones
CUANDO se inicie el contenedor de la aplicación en el despliegue, el sistema DEBE ejecutar automáticamente las migraciones pendientes de Alembic (`alembic upgrade head`) antes de habilitar el servicio HTTP para garantizar la consistencia del esquema.

## R7 — Endpoint de health check
CUANDO un cliente, balanceador o servicio de monitoreo realice una petición `GET` al endpoint de verificación de salud (`/health`), el sistema DEBE responder con código HTTP 200 y el estado de operatividad de la aplicación.

## R8 — Validación previa a la publicación
CUANDO se dispare el workflow de despliegue, el sistema DEBE comprobar que la totalidad de pruebas automatizadas y chequeos de calidad pasen satisfactoriamente ANTES de proceder con la publicación del artefacto o servicio.

## R9 — Verificación de disponibilidad en la URL desplegada
CUANDO el despliegue finalice, la URL pública o de servicio de la API desplegada DEBE responder exitosamente a las consultas del endpoint de health check para validar su disponibilidad operativa.

## R10 — Procedimientos documentados de rollback y observabilidad
EL SISTEMA DEBE contar con documentación operativa que defina detalladamente los pasos a seguir para revertir una versión defectuosa (rollback) y los mecanismos para consultar e inspeccionar los logs de la aplicación.
