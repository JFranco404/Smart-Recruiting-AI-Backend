from typing import List
from sqlalchemy.orm import Session
from app.modules.historial_academico.historial_academico_database_model import HistorialAcademico
from app.modules.historial_academico.historial_academico_models import *

def obtener_historial_academico_por_id(historial_id: int, db: Session):
    historial = db.query(HistorialAcademico).filter(
        HistorialAcademico.id == historial_id).first()
    if not historial:
        raise ValueError("El historial académico no existe")
    
    return historial

def crear_historial_academico(historial: DatosHistorialAcademico, db:Session) -> HistorialAcademico:
    historial = HistorialAcademico(
        titulo_obtenido = historial.titulo_obtenido,
        institucion = historial.institucion,
        area_de_estudio = historial.area_de_estudio,
        fecha_inicio = historial.fecha_inicio,
        fecha_finalizacion = historial.fecha_finalizacion,
        promedio_ponderado = historial.promedio_ponderado,
        reconocimientos = historial.reconocimientos
    )

    db.add(historial)
    db.commit()
    db.refresh(historial)

    return historial

def actualizar_historial_academico(historial: HistorialAcademico, db:Session) -> HistorialAcademico:
    historial_encontrado = db.query(HistorialAcademico).filter(
        HistorialAcademico.id == historial.id).first()
    if not historial_encontrado:
        raise ValueError("El historial académico no existe")
    
    historial_encontrado.titulo_obtenido = historial.titulo_obtenido
    historial_encontrado.institucion = historial.institucion
    historial_encontrado.area_de_estudio = historial.area_de_estudio
    historial_encontrado.fecha_inicio = historial.fecha_inicio
    historial_encontrado.fecha_finalizacion = historial.fecha_finalizacion
    historial_encontrado.promedio_ponderado = historial.promedio_ponderado
    historial_encontrado.reconocimientos = historial.reconocimientos

    db.commit()
    db.refresh(historial_encontrado)

    return historial_encontrado


def eliminar_historial_academico(historial_id: int, db:Session) -> HistorialAcademico:
    historial_encontrado = db.query(HistorialAcademico).filter(
        HistorialAcademico.id == historial_id).first()
    if not historial_encontrado:
        raise ValueError("El historial académico no existe")
    
    db.delete(historial_encontrado)
    db.commit()

    return historial_encontrado