# Usa una imagen base de Python
FROM python:3.10-slim-buster

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Cambia al directorio de la aplicación
WORKDIR /app

RUN apt-get install sox ffmpeg libcairo2 libcairo2-dev

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que utilizará FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
