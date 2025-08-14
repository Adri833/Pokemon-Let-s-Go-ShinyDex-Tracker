# Dockerfile
FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED=1

# Dependencias nativas para Pillow + zona horaria
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential libjpeg-dev zlib1g-dev libfreetype6-dev libpng-dev tzdata  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instala dependencias de Python primero (mejor cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

CMD ["python", "-u", "bot.py"]
