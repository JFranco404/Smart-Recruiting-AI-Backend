# Usa una imagen base de Python
FROM python:3.10-slim-buster

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Cambia al directorio de la aplicación
WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # Pour authentification via LDAP
  python3-dev python2.7-dev libldap2-dev libsasl2-dev ldap-utils tox lcov valgrind libcairo2-dev\
  # psycopg2 dependencies
  libpq-dev \
  # OpenCV dependencies \
  ffmpeg libsm6 libxext6 \
  # miniconda 3
  wget bash \
  # To allow python to use zlib
  zlib1g-dev \
  # To build local conda dependencies
  git \
  # For pypx
  dcmtk sudo \


# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto que utilizará FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
