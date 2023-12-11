from sqlalchemy import Column, Integer, String
from database.db import Base


class Ubicacion(Base):
    __tablename__ = "ubicacion"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ciudad = Column(String(30))
    estado = Column(String(30))
    pais = Column(String(30))
