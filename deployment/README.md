# Guía de despliegue

Esta carpeta contiene el contexto para que la persona encargada implemente el despliegue después de clonar el repositorio.

## Orden obligatorio

1. Leer `AGENTS.md`, `docs/architecture.md`, `docs/verification.md` y la feature `deployment` de `feature_list.json`.
2. Esperar a que el `spec_author` cree y se apruebe `specs/deployment/`.
3. Crear el `Dockerfile` de la API Python.
4. Crear la infraestructura Terraform dentro de `infra/terraform/`.
5. Ejecutar `terraform fmt -check`.
6. Ejecutar `terraform init`.
7. Ejecutar `terraform validate`.
8. Ejecutar `terraform plan` y revisar el plan con el equipo.
9. Ejecutar `terraform apply` solo con aprobación humana.
10. Ejecutar migraciones Alembic y verificar `/health`.

## Prohibiciones

- No guardar secretos en Git.
- No subir archivos `.tfvars` reales.
- No ejecutar `apply` sin revisar el plan.
- No crear recursos destructivos sin aprobación.

## Entregables esperados

- `Dockerfile`.
- `infra/terraform/*.tf`.
- `.env.example` sin secretos reales.
- Estado remoto de Terraform documentado.
- Health check.
- Informe en `progress/deploy_deployment.md`.
