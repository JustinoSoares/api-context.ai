from fastapi import FastAPI
from app.modules.documents.routes import router as doc_router
from app.modules.rag.routes import router as rag_router
from app.core.errors import register_error_handlers

app = FastAPI()

app.include_router(doc_router)
app.include_router(rag_router)
register_error_handlers(app)