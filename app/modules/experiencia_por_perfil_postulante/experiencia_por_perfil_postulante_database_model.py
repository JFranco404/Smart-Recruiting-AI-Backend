from sqlalchemy import Column, Integer
from database.db import Base


class ExperienciaPorPerfilPostulante(Base):
    __tablename__ = "experiencia_por_perfil_postulante"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_perfil_postulante = Column(Integer)
    id_experiencia = Column(Integer)
