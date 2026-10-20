# Requirements — project_setup

## R1
CUANDO una persona siga las instrucciones del proyecto, el sistema DEBE iniciar una API mínima de FastAPI mediante un comando documentado.

## R2
CUANDO la aplicación se inicie, el sistema DEBE leer su configuración desde variables de entorno y NO depender de secretos escritos en el código.

## R3
CUANDO la aplicación ejecute una operación de persistencia, el sistema DEBE utilizar SQLAlchemy con PostgreSQL configurado mediante `DATABASE_URL`.

## R4
CUANDO una persona revise el código, el sistema DEBE separar las capas `api`, `services`, `repositories`, `models` y `schemas`.

## R5
CUANDO una persona ejecute las herramientas de calidad documentadas, Ruff, mypy y pytest DEBEN poder ejecutarse mediante comandos reproducibles.

## R6
CUANDO se ejecute la suite inicial, el sistema DEBE verificar que la aplicación puede iniciar y responder al health check.
