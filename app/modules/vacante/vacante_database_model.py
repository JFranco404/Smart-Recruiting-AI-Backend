from sqlalchemy import Column, Integer, String, Date, Boolean
from database.db import Base


class Vacante(Base):
    __tablename__ = "vacante"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(30))
    descripcion = Column(String(200))
    usuario_reclutador = Column(Integer)
    fecha_publicacion = Column(Date)
    fecha_cierre = Column(Date)
    salario = Column(Integer)
    remoto = Column(Boolean)
    modalidad = Column(String(100))
    ubicacion = Column(Integer)
    area_trabajo = Column(String(100))
    annos_experiencia = Column(Integer)
