# app/core/errors.py

from fastapi import Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


def register_error_handlers(app):
    @app.exception_handler(AppError)
    async def app_error_handler(request: Request, exc: AppError):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.message}
        )

    @app.exception_handler(Exception)
    async def generic_error_handler(request: Request, exc: Exception):
        print(f"[ERRO NÃO ESPERADO] {exc}")  # ou usa logging
        return JSONResponse(
            status_code=500,
            content={"message": "Erro interno do servidor."}
        )