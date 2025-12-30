FROM python:3.11-slim

# Evita buffers y mejora logs en Cloud Run
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo
WORKDIR /app

# Dependencias del sistema (necesarias para algunas libs)
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero (mejor cacheo)
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar el código de la app
COPY app/ app/

# Cloud Run expone el puerto 8080
ENV PORT=8080
EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
