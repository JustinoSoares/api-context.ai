import os
from fastapi import APIRouter, UploadFile
import shutil
from app.core.errors import AppError

from app.modules.documents.service import process_document

router = APIRouter()

ALLOWED_EXTENSIONS = {".pdf", ".txt", ".docx", ".md"}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2MB

@router.post("/upload")
async def upload(file: UploadFile):
    # Valida extensão
    ext = os.path.splitext(file.filename)[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise AppError(f"Extensão '{ext}' não permitida. Use: {', '.join(ALLOWED_EXTENSIONS)}", status_code=415)

    # Valida tamanho
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise AppError(f"Arquivo muito grande. Máximo permitido: 2MB", status_code=400)

    try:
        path = f"/tmp/{file.filename}"

        with open(path, "wb") as buffer:
            buffer.write(contents)

        doc_id = process_document(path)
    except AppError:
        raise
    except Exception as e:
        raise AppError(f"Erro ao fazer upload do arquivo: {e}", status_code=400)

    return {"document_id": str(doc_id)}