# Terraform

Aquí se implementará la infraestructura cloud de la plataforma.

## Archivos esperados

```text
infra/terraform/
├── providers.tf
├── variables.tf
├── main.tf
├── outputs.tf
├── versions.tf
├── backend.tf.example
└── environments/
    ├── dev.tfvars.example
    └── prod.tfvars.example
```

## Requisitos

- Definir el proveedor cloud en `providers.tf`.
- Definir versiones en `versions.tf`.
- Usar variables, no valores sensibles codificados.
- Configurar estado remoto antes de producción.
- Exportar la URL de la API y la información necesaria para operar el servicio.

## Comandos

```bash
terraform fmt -check
terraform init
terraform validate
terraform plan -var-file=environments/dev.tfvars
terraform apply -var-file=environments/dev.tfvars
```

Los comandos `plan` y `apply` requieren revisión humana. El proveedor cloud y la región se decidirán en la spec aprobada de `deployment`.
