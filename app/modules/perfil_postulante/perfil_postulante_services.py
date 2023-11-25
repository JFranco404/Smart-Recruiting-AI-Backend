from typing import List
from sqlalchemy.orm import Session
from app.modules.perfil_postulante.perfil_postulante_database_model import PerfilPostulante
from app.modules.usuario.usuario_services import obtener_usuario_por_id


def obtener_perfil_postulante_por_usuario_id(usuario_id: int, db: Session) -> PerfilPostulante:
    usuario = obtener_usuario_por_id(usuario_id, db)
    if not usuario:
        raise ValueError("El usuario no existe")

    perfil_postulante = db.query(PerfilPostulante).filter(
        PerfilPostulante.id_usuario == usuario_id)
    if not perfil_postulante:
        raise ValueError("El perfil no existe")

    return perfil_postulante
