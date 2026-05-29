# Azure OCR PostgreSQL API

Prueba Técnica – Analista de Desarrollo Jr Cloud Azure

## Descripción

Azure OCR PostgreSQL API es una solución desarrollada en Python con FastAPI que permite:

- Recibir documentos PDF o imágenes.
- Extraer texto mediante OCR utilizando Azure AI Document Intelligence.
- Procesar y limpiar el texto extraído.
- Almacenar los resultados en PostgreSQL.
- Consultar los documentos procesados a través de endpoints REST.
- Documentar automáticamente la API mediante Swagger.

---

## Funcionalidades Implementadas

- Carga de documentos PDF e imágenes.
- OCR con Azure AI Document Intelligence.
- Limpieza y normalización de texto.
- Almacenamiento de resultados en PostgreSQL.
- Consulta de documentos procesados.
- Gestión de errores mediante HTTPException.
- Uso de variables de entorno para configuración sensible.
- Documentación automática con Swagger UI.

---

## Tecnologías Utilizadas

### Backend

- Python 3.14
- FastAPI
- Uvicorn

### Base de Datos

- PostgreSQL
- SQLAlchemy ORM

### Inteligencia Artificial

- Azure AI Document Intelligence (OCR)

### Configuración

- Python Dotenv

### Validación

- Pydantic

### Documentación

- Swagger UI (OpenAPI)

---

## Arquitectura Azure

### Componentes

- Azure App Service
- Azure AI Document Intelligence
- Azure Database for PostgreSQL
- Azure Key Vault
- Azure Monitor

### Flujo de la Solución

1. El usuario carga un documento PDF o imagen.
2. FastAPI recibe el archivo.
3. Azure AI Document Intelligence realiza la extracción OCR.
4. El texto es procesado y normalizado.
5. La información se almacena en PostgreSQL.
6. La API devuelve una respuesta con el resultado procesado.
7. Los documentos pueden consultarse posteriormente mediante la API.

### Ambientes

#### QA

- Azure App Service (QA)
- PostgreSQL QA
- Variables de entorno específicas
- Recursos aislados

#### Producción

- Azure App Service (PROD)
- Azure Database for PostgreSQL
- Azure Key Vault
- Azure Monitor
- Auto Scaling

### Seguridad

- Variables sensibles almacenadas en Azure Key Vault.
- Comunicación mediante HTTPS.
- Control de acceso mediante Azure RBAC.
- Separación de ambientes QA y Producción.

### Escalabilidad

- Escalado horizontal mediante Azure App Service.
- PostgreSQL Flexible Server.
- Posibilidad de desacoplar el OCR mediante Azure Functions.

---

## Diagrama de Arquitectura

```markdown
![Arquitectura Azure](docs/images/azure-architecture.png)
```
---

## Estructura del Proyecto

```text
azure-ocr-postgresql-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   └── services/
│       ├── ocr_service.py
│       └── text_processor.py
│
├── docs/
│   ├── arquitectura.md
│   └── images/
│
├── sql/
│   └── schema.sql
│
├── .gitignore
├── requirements.txt
├── README.md
└── .env
```

---

## Configuración del Proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/KnNgZmN/azure-ocr-postgresql-api.git
cd azure-ocr-postgresql-api
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
```

---

### 3. Activar entorno virtual

#### Windows

```bash
.\venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Variables de Entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/ocr_db

AZURE_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_KEY=your-api-key
```

---

## Base de Datos

Crear una base de datos PostgreSQL llamada:

```text
ocr_db
```

Script SQL disponible en:

```text
sql/schema.sql
```

Contenido:

```sql
CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    extracted_text TEXT,
    processed_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

> Nota: La aplicación también utiliza SQLAlchemy ORM para la creación automática de tablas.

---

## Ejecución

Iniciar la aplicación:

```bash
uvicorn app.main:app --reload
```

La aplicación quedará disponible en:

```text
http://127.0.0.1:8000
```

---

## Documentación Swagger

Disponible en:

```text
http://127.0.0.1:8000/docs
```

---

## Endpoints

### GET /

Endpoint de bienvenida.

#### Respuesta

```json
{
  "message": "Azure OCR PostgreSQL API",
  "documentation": "/docs"
}
```

---

### POST /upload

Carga un documento PDF o imagen.

#### Proceso

- Recibe archivo.
- Ejecuta OCR con Azure AI Document Intelligence.
- Procesa el texto.
- Guarda la información en PostgreSQL.
- Devuelve el resultado procesado.

#### Ejemplo de Respuesta

```json
{
  "message": "Documento procesado correctamente",
  "id": 1,
  "filename": "Titanic.pdf",
  "text": "texto extraído y procesado..."
}
```

---

### GET /documents

Obtiene los documentos almacenados.

#### Ejemplo de Respuesta

```json
[
  {
    "id": 1,
    "filename": "Titanic.pdf",
    "created_at": "2026-05-29T19:57:43"
  }
]
```

---

## Buenas Prácticas Implementadas

- Arquitectura por capas.
- Separación de responsabilidades.
- Uso de variables de entorno.
- Integración con Azure AI.
- Persistencia mediante SQLAlchemy ORM.
- Validación y serialización con Pydantic.
- Manejo de errores mediante HTTPException.
- Gestión de sesiones de base de datos.
- Rollback de transacciones ante errores.
- Documentación automática con Swagger/OpenAPI.
- Código modular y mantenible.

---

## Mejoras Futuras

- Dockerización de la aplicación.
- CI/CD con GitHub Actions.
- Azure Blob Storage para almacenamiento de archivos.
- Azure Functions para procesamiento asíncrono.
- Autenticación JWT.
- Azure Application Insights.
- Pruebas unitarias y de integración.
- Migraciones con Alembic.

---

## Autor

**Kevin Guzman Acevedo**

Repositorio:

https://github.com/KnNgZmN/azure-ocr-postgresql-api