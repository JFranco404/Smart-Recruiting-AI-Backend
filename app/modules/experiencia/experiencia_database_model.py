from sqlalchemy import Column, Integer, String, Date, Boolean
from database.db import Base


class Experiencia(Base):
    __tablename__ = "experiencia"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_empresa = Column(String(100))
    contacto = Column(String(50))
    tipo_cargo = Column(String(50))
    fecha_inicio = Column(Date)
    fecha_finalizacion = Column(Date)
    responsabilidades = Column(String(400))