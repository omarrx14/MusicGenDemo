#!/bin/bash

# Esperar a que la base de datos esté lista
echo "Esperando a que la base de datos esté lista..."
sleep 10

# Ejecutar las migraciones de Alembic
echo "Ejecutando migraciones de Alembic..."
alembic upgrade head

# Iniciar la aplicación
echo "Iniciando la aplicación..."
uvicorn main:app --host 0.0.0.0 --port 8000 