from sqlalchemy import Column, Integer, String, Date, Sequence
from database.db import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, Sequence('usuario_id_seq'), primary_key=True, index=True, autoincrement=True)
    cedula = Column(Integer)
    nombres = Column(String(50))
    apellidos = Column(String(50))
    fecha_nacimiento = Column(Date)
    lugar_residencia = Column(Integer)
    correo = Column(String(30))
    rol = Column(Integer)
    passwd = Column(String(26))
