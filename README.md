# Plataforma de Reservas — Harness SDD

Entorno de trabajo para dos personas usando Harness Engineering y Spec-Driven Development, con una API en Python.

## Flujo

`pending → spec_ready → aprobación humana → in_progress → implementación → revisión → done`

Cada funcionalidad tiene su propia carpeta dentro de `specs/`. La Persona 1 trabaja en autenticación y la Persona 2 en reservas.

## Agentes

El flujo reproduce el ejemplo:

```text
leader → spec_author → spec_ready → aprobación humana
→ implementer → reviewer → deployer → done
```

Las definiciones de roles para Codex están en `agents/`. `AGENTS.md` es el punto de entrada del agente principal.
