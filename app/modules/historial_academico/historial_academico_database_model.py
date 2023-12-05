from sqlalchemy import Column, Integer, String, Date, Boolean
from database.db import Base


class HistorialAcademico(Base):
    __tablename__ = "historial_academico"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo_obtenido = Column(String(100))
    institucion = Column(String(150))
    area_de_estudio = Column(String(100))
    fecha_inicio = Column(Date)
    fecha_finalizacion = Column(Date)
    promedio_ponderado = Column(Integer)
    reconocimientos = Column(String(400))