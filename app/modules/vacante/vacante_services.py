from typing import List
from app.modules.vacante.vacante_database_model import Vacante
from app.modules.usuario.usuario_services import obtener_usuario_por_id


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


def crear_vacante(vacante, db):
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
    
    vacante_existente = obtener_vacante_por_titulo(vacante.titulo, db)
    if vacante_existente:
        raise ValueError("Ya existe una vacante con el mismo titulo")
    
    vacante_existente = obtener_vacante_por_descripcion(vacante.descripcion, db)
    if vacante_existente:
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


def obtener_vacante_por_titulo(titulo: str, db) -> Vacante:
    """
    Obtiene una vacante por titulo.
    """

    vacante = db.query(Vacante).filter(Vacante.titulo == titulo).first()
    if not vacante:
        return None

    return vacante

def obtener_vacante_por_descripcion(descripcion: str, db) -> Vacante:
    """
    Obtiene una vacante por descripcion.
    """

    vacante = db.query(Vacante).filter(Vacante.descripcion == descripcion).first()
    if not vacante:
        return None

    return vacante
