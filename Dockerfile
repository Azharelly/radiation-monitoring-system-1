# Imagen base oficial de Python
FROM python:3.11-slim

# Evita que Python genere archivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Evita buffering de logs (muy importante para Cloud)
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos requirements primero (mejora caching)
COPY app/requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de la aplicación
COPY app/ .

# Exponemos el puerto que usa la app
EXPOSE 8080

# Comando de arranque (producción)
CMD ["gunicorn", "--workers", "1","--blind=0.0.0.0:8080", "app.main:app"]
