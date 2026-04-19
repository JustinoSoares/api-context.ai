FROM python:3.11-slim

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia o requirements e limpa referências locais
COPY requirements.txt .

RUN pip install --upgrade pip && \
    # Instala torch CPU antes de tudo (evita baixar versão CUDA)
    pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cpu && \
    # Filtra linhas com referências locais (file://) e instala o resto
    grep -v "^torch" requirements.txt | \
    grep -v "file://" | \
    grep -v "@ file" \
    > requirements_clean.txt && \
    pip install -r requirements_clean.txt

# Copia o código
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]