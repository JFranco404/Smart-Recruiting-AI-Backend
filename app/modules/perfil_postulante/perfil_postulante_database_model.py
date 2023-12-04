from sqlalchemy import Column, Integer, String, Date, Boolean
from database.db import Base


class PerfilPostulante(Base):
    __tablename__ = "perfil_postulante"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_usuario = Column(Integer)
    resumen = Column(String(500))
    habilidades = Column(String (150))
    idiomas = Column(String(150))
    link = Column(String(150))
    referencias= Column(String(300))
    
