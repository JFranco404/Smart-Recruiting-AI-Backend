from typing import List
from sqlalchemy.orm import Session
from app.modules.perfil_postulante.perfil_postulante_database_model import PerfilPostulante
from app.modules.usuario.usuario_services import obtener_usuario_por_id
from app.modules.perfil_postulante.perfil_postulante_models import DatosPostulante, ActualizarPerfilPostulante


def obtener_perfil_postulante_por_usuario_id(usuario_id: int, db: Session) -> PerfilPostulante:
    usuario = obtener_usuario_por_id(usuario_id, db)
    if not usuario:
        raise ValueError("El usuario no existe")

    perfil_postulante = db.query(PerfilPostulante).filter(
        PerfilPostulante.id_usuario == usuario_id).first()
    if not perfil_postulante:
        raise ValueError("El perfil no existe")

    return perfil_postulante


def crear_postulante(postulante: DatosPostulante, db:Session) -> PerfilPostulante:
    usuario_id = obtener_usuario_por_id(postulante.id_usuario,db)
    if not usuario_id:
        raise ValueError("El usuario no existe")

    postulante = PerfilPostulante(
        id_usuario=postulante.id_usuario,
        resumen=postulante.resumen,
        habilidades=postulante.habilidades,
        idiomas=postulante.idiomas,
        link=postulante.link,
        referencias=postulante.referencias
    )

    db.add(postulante)
    db.commit()
    db.refresh(postulante)

    return postulante

def actualizar_postulante(postulante: ActualizarPerfilPostulante, db:Session) ->PerfilPostulante:
    postulante_encontrado = db.query(PerfilPostulante).filter(
        PerfilPostulante.id == postulante.id).first()
    if not postulante_encontrado:
        raise ValueError("El perfil del postulante no existe")
    
    if postulante.id_usuario is not None and postulante.id != 0:
        postulante_encontrado.id_usuario=postulante.id_usuario

    if postulante.resumen is not None and postulante.resumen != "":
        postulante_encontrado.resumen=postulante.resumen

    if postulante.habilidades is not None and postulante.habilidades != "":
        postulante_encontrado.habilidades=postulante.habilidades

    if postulante.idiomas is not None and postulante.idiomas != "":
        postulante_encontrado.idiomas=postulante.idiomas

    if postulante.link is not None and postulante.link != "":
        postulante_encontrado.link=postulante.link

    if postulante.referencias is not None and postulante.referencias != "":
        postulante_encontrado.referencias=postulante.referencias

    db.commit()
    db.refresh(postulante_encontrado)

    return postulante_encontrado

def eliminar_postulante(postulante_id: int, db: Session) -> PerfilPostulante:
    postulante = obtener_perfil_postulante_por_usuario_id(postulante_id, db)

    postulante_encontrado = db.query(PerfilPostulante).filter(
        PerfilPostulante.id == postulante_id).first()
    if not postulante_encontrado:
        raise ValueError("La vacante no existe")

    db.delete(postulante_encontrado)
    db.commit()

    return postulante_encontrado