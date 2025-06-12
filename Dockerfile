# Imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Atualiza o pip e instala as dependências do projeto
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expõe a porta padrão usada pelo FastAPI/Uvicorn
EXPOSE 8070

# Comando para iniciar o microserviço
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8070"]
