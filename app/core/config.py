import os
from dotenv import load_dotenv
from app.core.errors import AppError

load_dotenv()


class Settings:
    try:
        DATABASE_URL = os.getenv("DATABASE_URL")
    except Exception as e:
        raise AppError(f"Não existe um banco de dados configurado", status_code=500)

    try:
        GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    except Exception as e:
        raise AppError(f"Não existe uma chave de API do GROQ configurada", status_code=500)

    try:
        GROQ_MODEL = os.getenv("GROQ_MODEL")
    except Exception as e:
        raise AppError(f"Não existe um modelo do GROQ configurado", status_code=500)

settings = Settings()