from typing import List
from sqlalchemy.orm import Session
from app.modules.historial_academico.historial_academico_services import obtener_historial_academico_por_id
from app.modules.perfil_postulante.perfil_postulante_services import obtener_perfil_postulante_por_usuario_id
from .educacion_por_perfil_postulante_database_model import EducacionPorPerfilPostulante
from .educacion_por_perfil_postulante_services import obtener_perfil_postulante_por_usuario_id


def obtener_educacion_por_perfil_postulante_por_postulante_id(postulante_id: int, db: Session) -> List[EducacionPorPerfilPostulante]:
    postulante = obtener_perfil_postulante_por_usuario_id(postulante_id, db)
    if not postulante:
        raise ValueError("El usuario reclutador no existe")

    educacion_por_perfil = db.query(EducacionPorPerfilPostulante).filter(
        EducacionPorPerfilPostulante.id_perfil_postulante == postulante_id).all()

    historial_academico = []
    for i in educacion_por_perfil:
        historial_academico.append(
            obtener_historial_academico_por_id(i.id, db))

    return historial_academico
