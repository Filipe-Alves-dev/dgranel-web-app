# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define a pasta de trabalho dentro do container
WORKDIR /app

# Instala o Flask (o framework que o Otávio sugeriu para APIs)
RUN pip install flask pytz requests

# Copia os arquivos da sua pasta 'app' local para dentro do container
COPY ./app .

# Comando que liga o motor do sistema
CMD ["python", "main.py"]
