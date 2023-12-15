from typing import List
from sqlalchemy.orm import Session
from app.modules.experiencia.experiencia_database_model import Experiencia
from app.modules.experiencia.experiencia_models import DatosExperiencia, FiltrosExperiencia


def obtener_experiencia_por_id(experiencia_id: int, db: Session):
    experiencia = db.query(Experiencia).filter(
        Experiencia.id == experiencia_id).first()
    if not experiencia:
        raise ValueError("El perfil no existe")

    return experiencia


def crear_experiencia(experiencia: DatosExperiencia, db: Session) -> Experiencia:
    experiencia = Experiencia(
        nombre_empresa=experiencia.nombre_empresa,
        contacto=experiencia.contacto,
        tipo_cargo=experiencia.tipo_cargo,
        fecha_inicio=experiencia.fecha_inicio,
        fecha_finalizacion=experiencia.fecha_finalizacion,
        responsabilidades=experiencia.responsabilidades
    )
    db.add(experiencia)
    db.commit()
    db.refresh(experiencia)

    return experiencia


def actualizar_experiencia(experiencia: Experiencia, db: Session) -> Experiencia:
    experiencia_encontrada = db.query(Experiencia).filter(
        Experiencia.id == experiencia.id).first()
    if not experiencia_encontrada:
        raise ValueError("La experiencia no existe")

    if experiencia.nombre_empresa is not None and experiencia.nombre_empresa != "":
        experiencia_encontrada.nombre_empresa = experiencia.nombre_empresa

    if experiencia.contacto is not None and experiencia.contacto != "":
        experiencia_encontrada.contacto = experiencia.contacto

    if experiencia.tipo_cargo is not None and experiencia.tipo_cargo != "":
        experiencia_encontrada.tipo_cargo = experiencia.tipo_cargo

    if experiencia.fecha_inicio is not None and experiencia.fecha_inicio != "":
        experiencia_encontrada.fecha_inicio = experiencia.fecha_inicio

    if experiencia.fecha_finalizacion is not None and experiencia.fecha_finalizacion != "":
        experiencia_encontrada.fecha_finalizacion = experiencia.fecha_finalizacion

    if experiencia.responsabilidades is not None and experiencia.responsabilidades != "":
        experiencia_encontrada.responsabilidades = experiencia.responsabilidades

    db.commit()
    db.refresh(experiencia_encontrada)

    return experiencia_encontrada


def eliminar_experiencia(experiencia_id: int, db: Session) -> Experiencia:
    experiencia_encontrada = db.query(Experiencia).filter(
        Experiencia.id == experiencia_id).first()
    if not experiencia_encontrada:
        raise ValueError("La experiencia no existe")

    db.delete(experiencia_encontrada)
    db.commit()

    return experiencia_encontrada
