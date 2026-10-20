# Requirements — project_setup

## R1
CUANDO una persona siga las instrucciones del proyecto, el sistema DEBE iniciar una API mínima de FastAPI mediante un comando documentado.

## R2
CUANDO la aplicación se inicie, el sistema DEBE leer su configuración desde variables de entorno y NO depender de secretos escritos en el código.

## R3
CUANDO la aplicación ejecute una operación de persistencia, el sistema DEBE utilizar SQLAlchemy con PostgreSQL configurado mediante `DATABASE_URL`.

## R4
CUANDO una persona ejecute `docker compose up -d postgres`, el sistema DEBE iniciar PostgreSQL con persistencia en un volumen y un health check funcional.

## R5
CUANDO una persona revise el código, el sistema DEBE separar las capas `api`, `services`, `repositories`, `models` y `schemas`.

## R6
CUANDO una persona ejecute las herramientas de calidad documentadas, Ruff, mypy y pytest DEBEN poder ejecutarse mediante comandos reproducibles.

## R7
CUANDO se ejecute la suite inicial, el sistema DEBE verificar que la aplicación puede iniciar y responder al health check.

## R8
CUANDO una persona ejecute `docker compose up -d postgres`, el sistema DEBE permitir que la aplicación se conecte usando la `DATABASE_URL` del entorno local.

## R9
CUANDO se prepare la base de datos, el sistema DEBE aplicar cambios de esquema mediante migraciones versionadas de Alembic y NO mediante creación manual de tablas.

## R10
CUANDO se ejecuten las pruebas, el sistema DEBE usar una configuración de prueba aislada y NO debe modificar datos de desarrollo o producción.
