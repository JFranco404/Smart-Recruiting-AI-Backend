from typing import List
from sqlalchemy.orm import Session
from app.modules.vacante.vacante_database_model import Vacante
from app.modules.vacante.vacante_models import CrearVacante
from app.modules.usuario.usuario_services import obtener_usuario_por_id


def obtener_vacantes_por_usuario_reclutador_id(usuario_reclutador_id: int, db: Session) -> List[Vacante]:
    """
    Obtiene vacantes por ID de usuario reclutador.

    Raises:
        ValueError: Cuando el usuario no es encontrado.
    """

    usuario_reclutador = obtener_usuario_por_id(usuario_reclutador_id, db)
    if not usuario_reclutador:
        raise ValueError("El usuario reclutador no existe")

    return db.query(Vacante).filter(Vacante.usuario_reclutador == usuario_reclutador_id).all()


def crear_vacante(vacante: CrearVacante, db: Session) -> Vacante:
    """
    Crea una vacante.

    Raises:
        ValueError: Cuando el usuario no es encontrado.
        ValueError: Cuando existe una vacante con el mismo titulo.
        ValueError: Cuando existe una vacante con la misma descripcion.
    """

    usuario_reclutador = obtener_usuario_por_id(vacante.usuario_reclutador, db)
    if not usuario_reclutador:
        raise ValueError("El usuario reclutador no existe")

    vacantes_del_reclutador = obtener_vacantes_por_usuario_reclutador_id(
        vacante.usuario_reclutador, db)
    
    for vacante_del_reclutador in vacantes_del_reclutador:
        if vacante_del_reclutador.titulo == vacante.titulo:
            raise ValueError("Ya existe una vacante con el mismo titulo")
        if vacante_del_reclutador.descripcion == vacante.descripcion:
            raise ValueError("Ya existe una vacante con la misma descripcion")

    vacante = Vacante(
        titulo=vacante.titulo,
        descripcion=vacante.descripcion,
        usuario_reclutador=vacante.usuario_reclutador,
        fecha_publicacion=vacante.fecha_publicacion,
        fecha_cierre=vacante.fecha_cierre,
        salario=vacante.salario,
        remoto=vacante.remoto,
        modalidad=vacante.modalidad,
        ubicacion=vacante.ubicacion,
        area_trabajo=vacante.area_trabajo,
        annos_experiencia=vacante.annos_experiencia
    )

    db.add(vacante)
    db.commit()
    db.refresh(vacante)

    return vacante
