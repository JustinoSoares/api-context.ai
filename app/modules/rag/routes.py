from fastapi import APIRouter
from pydantic import BaseModel
from app.modules.rag.service import answer

router = APIRouter()


class AskRequest(BaseModel):
    question: str
    document_id: str


@router.post("/ask")
def ask(req: AskRequest):
    response = answer(req.question, req.document_id)
    return {"answer": response}