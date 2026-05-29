from fastapi import FastAPI, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app.models import Base, Document
from app.schemas import DocumentResponse

from app.services.ocr_service import extract_text
from app.services.text_processor import clean_text


# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Azure OCR PostgreSQL API",
    description="API para procesamiento de documentos mediante Azure AI Document Intelligence",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Azure OCR PostgreSQL API",
        "documentation": "/docs"
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    db: Session = SessionLocal()

    try:
        file_bytes = await file.read()

        extracted_text = extract_text(file_bytes)

        processed_text = clean_text(extracted_text)

        document = Document(
            filename=file.filename,
            extracted_text=extracted_text,
            processed_text=processed_text
        )

        db.add(document)
        db.commit()
        db.refresh(document)

        return {
            "message": "Documento procesado correctamente",
            "id": document.id,
            "filename": document.filename,
            "text": processed_text
        }

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Error procesando documento: {str(e)}"
        )

    finally:
        db.close()


@app.get("/documents", response_model=list[DocumentResponse])
def get_documents():
    db: Session = SessionLocal()

    try:
        documents = db.query(Document).all()
        return documents

    finally:
        db.close()