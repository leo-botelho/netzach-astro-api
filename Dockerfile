FROM python:3.9-slim

WORKDIR /app

# Instala dependências do sistema necessárias para compilação (se houver)
RUN apt-get update && apt-get install -y gcc

# Copia e instala pacotes Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY main.py .

# Roda o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
