import fitz  # PyMuPDF
from docx import Document
from app.core.errors import AppError

def parse_file(file_path: str) -> str:
    try: 
        if file_path.endswith(".pdf"):
            doc = fitz.open(file_path)
            return "".join(page.get_text() for page in doc)

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

    except Exception as e:
        raise AppError(f"Erro ao ler o arquivo: {e}", status_code=500)