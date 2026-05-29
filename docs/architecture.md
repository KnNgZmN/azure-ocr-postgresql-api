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

## Estrategia de Ambientes

La solución contempla dos ambientes independientes:

### QA

- Azure App Service Plan QA
- Azure App Service QA
- Azure Database for PostgreSQL QA
- Variables de entorno QA

Objetivo:
Validar nuevas funcionalidades antes de producción.

### Producción

- Azure App Service Plan PROD
- Azure App Service PROD
- Azure Database for PostgreSQL PROD
- Azure Key Vault
- Azure Monitor

Objetivo:
Atender usuarios finales garantizando disponibilidad y seguridad.

## Seguridad

- Secretos almacenados en Azure Key Vault.
- Acceso HTTPS.
- Variables de entorno protegidas.
- Control de acceso mediante Azure RBAC.

## Escalabilidad

- Escalado horizontal en App Service.
- PostgreSQL Flexible Server.
- Posibilidad de desacoplar OCR mediante Azure Functions.
