from groq import Groq
from app.core.config import settings
from app.core.errors import AppError

if not settings.GROQ_API_KEY:
    raise AppError("IA não configurada", status_code=500)

client = Groq(api_key=settings.GROQ_API_KEY)


def generate_answer(context: str, question: str):
    prompt = f"""
    Devolva as respostas sempre com a formatação de markdown, deforma bem organizada, do mesmo jeitos que as IA devolvem a resposta.
    Responda apenas com base no contexto:

    {context}

    Pergunta:
    {question}
    """
    
    try:
        response = client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content
    except Exception as e:
        raise AppError(f"Erro ao gerar resposta com o GROQ: {e}", status_code=500)
 