FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Hacer el script de inicialización ejecutable
RUN chmod +x init.sh

# Exponer el puerto
EXPOSE 8000

# Usar el script de inicialización como punto de entrada
CMD ["./init.sh"] 