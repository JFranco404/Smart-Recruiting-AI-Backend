from sqlalchemy import Column, Integer
from database.db import Base


class Postulacion(Base):
    __tablename__ = "postulacion_por_perfil_postulante"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_vacante = Column(Integer)
    id_perfil_postulante = Column(Integer)
