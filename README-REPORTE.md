# Reporte del entorno

## Objetivo

Preparar un repositorio para desarrollar una plataforma de reservas en Python con dos personas usando Harness Engineering y Spec-Driven Development.

## División

- Persona 1: `auth` — registro, login, usuarios y JWT.
- Persona 2: `reservations` — disponibilidad, reservas y cancelaciones.

## Cómo funciona

`feature_list.json` controla el estado de cada funcionalidad. Las specs de cada feature están en `specs/<feature>/` y contienen requisitos, diseño y tareas. `AGENTS.md` define las reglas del agente y `docs/` contiene las reglas comunes del proyecto.

## Despliegue

La persona encargada del despliegue debe leer `deployment/README.md` e `infra/terraform/README.md`. La estructura incluye ejemplos de backend remoto, variables por entorno, Docker y `.env.example`, pero no contiene secretos ni ejecuta recursos cloud automáticamente.

## Próximo paso

El `leader` debe tomar la primera feature `pending` de `feature_list.json` y lanzar al `spec_author`. Este crea los tres archivos de spec a partir de `description` y `acceptance`. Luego cambia la feature a `spec_ready` y espera la aprobación humana. Todavía no hay specs generadas ni código de aplicación.
