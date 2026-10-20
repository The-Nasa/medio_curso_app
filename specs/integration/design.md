# Design — integration

## Responsable

Ambos: Persona 1 integra el flujo de negocio; Persona 2 mantiene la configuración de ejecución y deployment.

## Alcance

Validar que `auth`, `availability` y `reservations` funcionen como un único flujo HTTP, sin agregar nuevas reglas de negocio.

## Flujo principal

```text
register/login → token JWT → GET availability → POST reservation
→ disponibilidad ocupada → DELETE reservation → disponibilidad liberada
```

## Componentes

- `tests/test_integration.py`: pruebas HTTP aisladas con base de datos de prueba.
- `app/api/`: routers existentes y dependencias de autenticación.
- `app/services/`: reglas ya implementadas de roles, disponibilidad y reservas.
- `docker-compose.yml`: PostgreSQL local para ejecución manual.
- `docs/`: instrucciones de configuración y verificación.

## Decisiones técnicas

- Reutilizar los endpoints y esquemas existentes; no duplicar lógica en las pruebas.
- Usar usuarios de prueba con roles cliente y administrador.
- Aislar cada escenario y limpiar sus datos.
- Validar códigos HTTP y efectos persistidos, no solo respuestas superficiales.
- Ejecutar las comprobaciones de calidad antes del cierre.

## Fuera de alcance

El despliegue productivo queda en la feature `deployment`, a cargo de Persona 2.
