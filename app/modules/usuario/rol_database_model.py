from sqlalchemy import Column, Integer, String, Date
from database.db import Base


class Rol(Base):
    __tablename__ = "rol"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50))
    rol = Column(String(50))
