from sqlalchemy import Column, Integer, String, Date, Boolean
from database.db import Base


class Experiencia(Base):
    __tablename__ = "experiencia"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre_empresa = Column(String(100))
    contacto = Column(String(50))
    titulo_Cargo = Column(String(50))
    fecha_Inicio = Column(Date)
    fecha_Finalizacion = Column(Date)
    responsabilidades = Column(String(400))