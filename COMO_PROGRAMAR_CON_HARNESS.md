# Cómo programar este proyecto con Harness Engineering

Este repositorio usa Harness Engineering y Spec-Driven Development (SDD) para construir la plataforma de reservas con Codex.

## Estructura principal

```text
AGENTS.md              → reglas generales para Codex
agents/                → roles del flujo
feature_list.json      → funcionalidades, responsables y estados
specs/<feature>/       → requirements, design y tasks
progress/              → estado e informes de trabajo
docs/                  → arquitectura y convenciones
infra/terraform/       → contexto del despliegue
```

## Flujo obligatorio

```text
pending
  ↓
leader
  ↓
spec_author
  ↓
spec_ready
  ↓
aprobación humana
  ↓
in_progress
  ↓
implementer
  ↓
reviewer
  ↓
done
```

Para la feature `deployment`, después del reviewer aprobado participa también el `deployer`.

## Cómo iniciar una feature

1. Codex lee `AGENTS.md`, `feature_list.json` y `progress/current.md`.
2. El `leader` toma la primera feature con estado `pending`.
3. El `spec_author` lee `description` y `acceptance` del JSON.
4. El `spec_author` crea:

   ```text
   specs/<feature>/requirements.md
   specs/<feature>/design.md
   specs/<feature>/tasks.md
   ```

5. La feature cambia a `spec_ready`.
6. La persona responsable revisa la spec y responde `Aprobado` o solicita cambios.
7. Solo después de aprobar, la feature pasa a `in_progress`.

## Implementación

El `implementer` ejecuta las tasks en orden, crea código Python y pruebas, y marca cada task como `[x]` únicamente cuando está verificada.

Debe respetar:

- FastAPI.
- SQLAlchemy y PostgreSQL.
- Pydantic.
- Separación entre `api`, `services`, `repositories`, `models` y `schemas`.
- Ruff, mypy y pytest.

El implementer deja evidencia en:

```text
progress/impl_<feature>.md
```

## Revisión

El `reviewer` no modifica código. Comprueba:

- Todas las tasks completadas.
- Cada requisito `R<n>` relacionado con una prueba.
- Todos los criterios `acceptance` cubiertos.
- Ruff, mypy y pytest correctos.
- Arquitectura y seguridad correctas.

El resultado se guarda en:

```text
progress/review_<feature>.md
```

Solo `APPROVED` permite cerrar la feature como `done`.

## Orden del proyecto

```text
project_setup → auth → availability → reservations → integration → deployment
```

Responsabilidades:

- Persona 1: `auth`.
- Persona 2: `availability` y `reservations`.
- Ambos: `project_setup` e `integration`.
- Deployer: `deployment` con Docker y Terraform.

## Verificación

Antes de cerrar una feature se ejecuta:

```bash
bash ./init.sh
python -m ruff check .
python -m ruff format --check .
python -m mypy app
python -m pytest -q --cov=app --cov-fail-under=80
```

## Despliegue

El despliegue se realiza únicamente después de revisar el código y aprobar la spec de `deployment`.

```bash
terraform fmt -check
terraform init
terraform validate
terraform plan
terraform apply
```

`terraform apply` requiere aprobación humana. Nunca se guardan secretos en Git.
