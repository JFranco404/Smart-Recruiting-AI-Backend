from sqlalchemy.orm import Session
from app.modules.postulacion.postulacion_database_model import Postulacion
from app.modules.perfil_postulante.perfil_postulante_services import obtener_perfil_postulante_por_usuario_id
from app.modules.usuario.usuario_database_model import Usuario
from app.modules.vacante.vacante_database_model import Vacante


def eliminar_postulacion(postulacion_id: int, db: Session) -> Postulacion:
    """
    Elimina una postulacion.

    Raises:
        ValueError: Cuando la postulacion no es encontrada.
    """

    postulacion = db.query(Postulacion).filter(
        Postulacion.id == postulacion_id).first()
    if not postulacion:
        raise ValueError("La postulacion no existe")

    db.delete(postulacion)


def obtener_postulacion_por_usuario_id(usuario_id: int, db: Session) -> Postulacion:
    """
    Obtener Postulacion por usuario id.

    Raises:
        ValueError: Si no existe perfil postulante, retorna error.

    """
    perfil_postulante = obtener_perfil_postulante_por_usuario_id(
        usuario_id, db)
    if perfil_postulante:
        
        postulaciones = db.query(Postulacion).filter(Postulacion.id_perfil_postulante == perfil_postulante.id).all()
    
        vacantes_postuladas = []
        for postulacion in postulaciones:
            vacante = db.query(Vacante).filter(Vacante.id == postulacion.id_vacante).first()
            if vacante:
                vacantes_postuladas.append(vacante)

        return vacantes_postuladas
    else:
        raise ValueError("No existe la postulacion")


def seleccionar_postulacion(usuario_id: int, vacante_id: int, db: Session):
    """
    Verificar si la vacante y el usuario existen
    Obtener Perfil_Postulante por usuario id
    Verificar que registro nuevo no exista  
    Seleccionar postulacion

    Raises:
        ValueError: Si el registro de postulacion ya existe, no se ejecuta la postulacion.
        ValueError: Que la vacante o el usuario no existan.
    """

    vacante = db.query(Vacante).filter(Vacante.id == vacante_id).first()
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

    if vacante and usuario:
        perfil_postulante = obtener_perfil_postulante_por_usuario_id(
            usuario_id, db)

        postulacion_existente = db.query(Postulacion).filter(
            Postulacion.id_vacante == vacante_id,
            Postulacion.id_perfil_postulante == perfil_postulante.id
        ).first()

        if postulacion_existente:
            raise ValueError(
                "Ya existe una postulación para esta vacante y usuario")

        # Guardar la postulación
        postular_vacante(vacante_id, perfil_postulante.id, db)
    else:
        raise ValueError("La vacante o el usuario no existen")


def postular_vacante(vacante_id: int, perfil_postulante_id: int, db: Session):
    """
    Crear postulacion con id vacante y id postulante
    Guardar postulacion en base de datos

    """

    postulacion = Postulacion(id_vacante=vacante_id,
                              id_perfil_postulante=perfil_postulante_id)

    db.add(postulacion)
    db.commit()
    db.refresh(postulacion)

    return postulacion


def obtener_postulacion_por_vacante_id(vacante_id: int, db: Session) -> Postulacion:
    """
    Obtiene una postulacion por vacante_id.
    """

    postulacion = db.query(Postulacion).filter(
        Postulacion.id_vacante == vacante_id).first()
    if not postulacion:
        return None

    return postulacion


def eliminar_postulacion_por_vacante_id(vacante_id: int, db: Session) -> Postulacion:
    """
    Elimina una postulacion.
    """

    postulacion = obtener_postulacion_por_vacante_id(vacante_id, db)

    if postulacion:
        db.delete(postulacion)
        db.commit()
        db.refresh(postulacion)
        return postulacion
    else:
        return None
