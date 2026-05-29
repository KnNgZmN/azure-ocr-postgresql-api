# Arquitectura Azure - Prueba Técnica Aseneg

## Descripción General

La solución permite recibir documentos PDF o imágenes, extraer texto mediante OCR utilizando Azure AI Document Intelligence, procesar el contenido y almacenarlo en PostgreSQL.

## Arquitectura

Usuario
│
▼
Azure App Service (FastAPI)
│
├── Azure AI Document Intelligence
│
├── Azure Database for PostgreSQL
│
├── Azure Key Vault
│
└── Azure Monitor

## Flujo

1. El usuario carga un documento.
2. FastAPI recibe el archivo.
3. Azure Document Intelligence extrae el texto.
4. Se realiza limpieza y normalización del texto.
5. La información se almacena en PostgreSQL.
6. La API retorna el resultado al usuario.

## Ambiente QA

- Azure App Service (QA)
- PostgreSQL QA
- Variables de entorno QA
- Recursos aislados

## Ambiente Producción

- Azure App Service (PROD)
- PostgreSQL PROD
- Azure Key Vault
- Azure Monitor
- Auto Scaling

## Seguridad

- Secretos almacenados en Azure Key Vault.
- Acceso HTTPS.
- Variables de entorno protegidas.
- Control de acceso mediante Azure RBAC.

## Escalabilidad

- Escalado horizontal en App Service.
- PostgreSQL Flexible Server.
- Posibilidad de desacoplar OCR mediante Azure Functions.
