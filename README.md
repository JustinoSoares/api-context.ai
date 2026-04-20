# 🚀 API Context AI

API backend para processamento de documentos e perguntas com **RAG (Retrieval-Augmented Generation)**.

## 📌 Sobre o Projeto

Esta API permite:

* Upload de documentos
* Processamento e divisão em chunks
* Geração de embeddings
* Busca semântica com pgvector
* Respostas inteligentes usando LLM

---

## 🧠 Arquitetura

```text
Client → FastAPI → RAG Service → Embeddings → PostgreSQL (pgvector)
                                 ↓
                               LLM
```

---

## ⚙️ Tecnologias

* FastAPI
* PostgreSQL
* pgvector
* SQLAlchemy
* Alembic
* Sentence Transformers / Groq (LLM)

---

## 📁 Estrutura do Projeto

```bash
app/
 ├── core/
 │   ├── config.py
 │   └── database.py
 │
 ├── modules/
 │   ├── documents/
 │   ├── rag/
 │   └── llm/
 │
 └── main.py
```

---

## 🚀 Como rodar o projeto

### 1. Clonar

```bash
git clone https://github.com/JustinoSoares/api-context.ai
cd api-context-ai
```

---

### 2. Criar ambiente virtual

- Eu usei o Anaconda com a versão `3.11` do python, mas pode fazer desse jeito.

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Configurar variáveis de ambiente

Crie um `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/db
GROQ_API_KEY=your_key_here
GROQ_MODEL=modelo
```

---

### 5. Rodar migrações

```bash
alembic upgrade head
```

---

### 6. Iniciar servidor

```bash
uvicorn app.main:app --reload
```

---

## 📡 Endpoints

### 📄 Upload de documento

```http
POST /upload
```
---

### ❓ Perguntar ao documento

```http
POST /ask
```

Body:

```json
{
  "question": "Qual é o assunto do documento?",
  "document_id": "uuid"
}
```

---

## 🧪 Testes

```bash
pytest
```

---

## ⚠️ Problemas conhecidos

* Dimensão de embeddings deve ser consistente (ex: 384)
* Necessário PostgreSQL com extensão pgvector

---

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch (`feature/minha-feature`)
3. Commit suas mudanças
4. Push
5. Abra um Pull Request

---

## 📄 Licença

MIT License
