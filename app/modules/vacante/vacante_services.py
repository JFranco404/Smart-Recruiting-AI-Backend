from typing import List
from modules.vacante.vacante_database_model import Vacante
from modules.usuario.usuario_services import obtener_usuario_por_id


def obtener_vacantes_por_usuario_reclutador_id(usuario_reclutador_id: int, db) -> List[Vacante]:
    """
    Obtiene vacantes por ID de usuario reclutador.

    Raises:
        ValueError: Cuando el usuario no es encontrado.
    """

    usuario_reclutador = obtener_usuario_por_id(usuario_reclutador_id, db)
    if not usuario_reclutador:
        raise ValueError("El usuario reclutador no existe")

    return db.query(Vacante).filter(Vacante.usuario_reclutador == usuario_reclutador_id).all()
