# Usa una imagen base de Python
FROM python:3.10-slim-buster

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Cambia al directorio de la aplicación
WORKDIR /app

# Actualiza la lista de paquetes
RUN apt-get update

# Instala las dependencias del sistema para pycairo y otras bibliotecas
RUN apt-get install -y sox ffmpeg libcairo2 libcairo2-dev gcc

# Limpia archivos temporales
RUN apt-get clean

# Actualiza pip y setuptools
RUN pip install --upgrade pip setuptools

# Instala las dependencias de tu aplicación
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Expone el puerto que utilizará FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
