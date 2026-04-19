from sqlalchemy import text
from app.core.database import SessionLocal
from app.modules.embeddings.service import embed_text
from app.modules.llm.groq_client import generate_answer
from app.core.errors import AppError

def search_similar(question: str, document_id: str):
    db = SessionLocal()

    embedding = embed_text(question)
    embedding_str = str(embedding)  # converte para "[0.1, 0.2, ...]"

    query = text("""
        SELECT content
        FROM document_chunks
        WHERE document_id = :document_id
        ORDER BY embedding <-> CAST(:embedding AS vector)
        LIMIT 5
    """)

    results = db.execute(query, {
        "embedding": embedding_str,
        "document_id": document_id
    }).fetchall()

    db.close()

    return [r[0] for r in results]


def answer(question: str, document_id: str):
    chunks = search_similar(question, document_id)

    if not chunks:
        raise AppError("Nenhum conteúdo relevante encontrado para a pergunta.", status_code=400)
        

    context = "\n".join(chunks)

    return generate_answer(context, question)