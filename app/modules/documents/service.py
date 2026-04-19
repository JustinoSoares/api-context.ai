from app.utils.chunker import chunk_text
from app.utils.file_parser import parse_file
from app.modules.embeddings.service import embed_text
from app.modules.documents.models import DocumentChunk
from app.core.database import SessionLocal
from app.core.errors import AppError
import uuid

def process_document(file_path: str):
    try: 
        db = SessionLocal()

        text = parse_file(file_path)
        chunks = chunk_text(text)

        document_id = uuid.uuid4()

        for chunk in chunks:
            embedding = embed_text(chunk)

            db_chunk = DocumentChunk(
                document_id=document_id,
                content=chunk,
                embedding=embedding
            )

            db.add(db_chunk)

        db.commit()
        db.close()

        return document_id
    except Exception as e:
        raise AppError(f"Erro ao processar o documento: {e}", status_code=400)