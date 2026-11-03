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

## Revisión de pull requests con CodeGuardian

CodeGuardian Technical revisa los PR internos hacia la rama principal.
Ruff analiza los archivos Python modificados y pytest ejecuta la suite
con las dependencias de desarrollo del proyecto. El informe JSON se
descarga en Actions como codeguardian-review.

El motor está fijado a un commit de The-Nasa/codeguardian-ai. El check
lee codeguardian.yml del commit base. Si la rama base aún no incluye una
política, usa la política Standard incluida en el motor fijado. pytest es
obligatorio y los hallazgos de Ruff se reportan como advertencias.

Abre un PR interno con un cambio Python pequeño para verificar la
instalación. Revisa el check y su informe antes de exigirlo para fusionar.
