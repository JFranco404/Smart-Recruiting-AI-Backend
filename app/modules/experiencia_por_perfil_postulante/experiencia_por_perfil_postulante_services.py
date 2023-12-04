from typing import List
from sqlalchemy.orm import Session
from app.modules.historial_academico.historial_academico_services import obtener_historial_academico_por_id
from app.modules.perfil_postulante.perfil_postulante_services import obtener_perfil_postulante_por_usuario_id
from app.modules.experiencia_por_perfil_postulante.experiencia_por_perfil_postulante_database_model import ExperienciaPorPerfilPostulante
from app.modules.educacion_por_perfil_postulante.educacion_por_perfil_postulante_services import obtener_perfil_postulante_por_usuario_id
from app.modules.experiencia.experiencia_services import obtener_experiencia_por_id

def obtener_experiencia_por_perfil_postulante_por_postulante_id(postulante_id:int, db: Session) -> List[ExperienciaPorPerfilPostulante]:
    postulante = obtener_perfil_postulante_por_usuario_id(postulante_id, db)
    if not postulante:
        raise ValueError("El usuario reclutador no existe")

    experiencias_por_perfil = db.query(ExperienciaPorPerfilPostulante).filter(
        ExperienciaPorPerfilPostulante.id_perfil_postulante == postulante_id).all()
    
    experiencias = []
    for i in experiencias_por_perfil:
        experiencias.append(obtener_experiencia_por_id(i.id, db))

    return experiencias



