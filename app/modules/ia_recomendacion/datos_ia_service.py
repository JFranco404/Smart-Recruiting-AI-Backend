from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.modules.vacante.vacante_database_model import Vacante
from app.modules.experiencia.experiencia_database_model import Experiencia
from app.modules.experiencia_por_perfil_postulante.experiencia_por_perfil_postulante_database_model import ExperienciaPorPerfilPostulante
from app.modules.historial_academico.historial_academico_database_model import HistorialAcademico
from app.modules.perfil_postulante.perfil_postulante_database_model import PerfilPostulante
from app.modules.educacion_por_perfil_postulante.educacion_por_perfil_postulante_database_model import EducacionPorPerfilPostulante
from app.modules.ubicacion.ubicacion_database_model import Ubicacion
from app.modules.usuario.usuario_database_model import Usuario
from app.shared.recomdacion_vacantes.recomendacion_vacantes import pruebas


def obtener_usuario_id(usuario_id: int, db: Session) -> Usuario:
    """
    Obtiene un usuario por ID de usuario.

    Args:
        usuario_id (int): ID del usuario.

    Returns:
        Usuario: Información del usuario con el id de su ubicación.
    """
    return (
        db.query(Usuario)
        .filter(Usuario.id == usuario_id)
        .first()
    )

def obtener_ubicacion_usuario(usuario_id: int, db: Session) -> Ubicacion:
    """
    Obtiene la ubicacion en que se encuentra el usuario dado el Id del usuario.

    Args:
        usuario_id (int): ID del usuario.

    Returns:
        Usuario: Información del usuario encontrada dado el id de su ubicación.
    """
    usuario = obtener_usuario_id(usuario_id, db)
    ubicacion = db.query(Ubicacion).filter(Ubicacion.id == usuario.lugar_residencia).first()

    if usuario.lugar_residencia is not None:
        return ubicacion if ubicacion else {}


def obtener_ubicaciones(db:Session) -> List[Ubicacion]:
    """
    obtener el listado de ubicacines que se encuentran registrados
    Returns:
        Ubicacioines: lista con todas las ubicaciones que se encuetran en la base de datos.
    """
    return(
        db.query(Ubicacion)
        .all()
    )

def obtener_vacantes(db:Session) -> List[Vacante]:
    """
    obtener el listado de vacantes que se encuentran abiertas
    Returns:
        Vacantes: lista con todas las vacantes que se encuetran activas en la base de datos.
    """
    return(
        db.query(Vacante)
        .all()
    )

def obtener_perfil_postulante_id(usuario_id: int, db: Session) -> PerfilPostulante:
    """
    Obtiene el perfil perfil del postulante por ID de usuario.

    Args:
        usuario_id (int): ID del usuario.

    Returns:
        Usuario: Información del perfil del usuario.
    """
    perfil = (
        db.query(PerfilPostulante)
        .filter(PerfilPostulante.id_usuario == usuario_id)
        .first()
    )
    return perfil if perfil else {}


def obtener_experiencia_usuario(usuario_id: int,db: Session) -> list[ExperienciaPorPerfilPostulante]:
    """
    Obtiene la ubicación por ID de usuario.

    Args:
        usuario_id (int): ID del usuario.

    Returns:
        Usuario: Información del usuario con su ubicación.
    """  
    perfil_postulante = obtener_perfil_postulante_id(usuario_id,db)

    if perfil_postulante:
        result = (db.query(ExperienciaPorPerfilPostulante)
            .filter( ExperienciaPorPerfilPostulante.id_perfil_postulante==perfil_postulante.id)
            .all())
        if result:
            return result
        else:
            return []
    else:
        return []
        
    

def obtener_especifica_experiencia(usuario_id: int, db: Session):
    """
    Obtiene la ubicación por ID de usuario.

    Args:
        usuario_id (int): ID del usuario.

    Returns:
        Usuario: Información del usuario con su ubicación.
    """    
    experiencias_usuario = obtener_experiencia_usuario(usuario_id,db)
    tipos_experiencias = db.query(Experiencia).all()

    # Obtener los IDs de las experiencias asociadas al usuario
    ids_experiencias_usuario = []

    if experiencias_usuario:
        # Recorrer el diccionario y agregar los valores de 'id_experiencia'
        for experiencia in experiencias_usuario:
            id_experiencia = experiencia.id_experiencia
            ids_experiencias_usuario.append(id_experiencia)

        experiencias_filtradas = []

        for i in tipos_experiencias:
            if i.id in ids_experiencias_usuario:
                experiencias_filtradas.append(i)

        return experiencias_filtradas
    else:
        return []

def obtener_historial_usuario(usuario_id: int,db: Session) -> list[EducacionPorPerfilPostulante]:
    """
    Obtiene la ubicación por ID de usuario.

    Args:
        usuario_id (int): ID del usuario.

    Returns:
        Usuario: Información del usuario con su ubicación.
    """  
    perfil_postulante = obtener_perfil_postulante_id(usuario_id,db)

    if perfil_postulante:
        educacion = (
            db.query(EducacionPorPerfilPostulante)
            .filter( EducacionPorPerfilPostulante.id_perfil_postulante==perfil_postulante.id)
            .all()
        )
        if educacion:
            return educacion
        else:
            return []
    else:
        return []

def obtener_especifico_historial(usuario_id: int, db: Session)-> list[HistorialAcademico]:
    """
    Obtiene la ubicación por ID de usuario.

    Args:
        usuario_id (int): ID del usuario.

    Returns:
        Usuario: Información del usuario con su ubicación.
    """    
    historial_usuario = obtener_historial_usuario(usuario_id,db)
    tipos_historial = db.query(HistorialAcademico).all()

    # Obtener los IDs de las experiencias asociadas al usuario
    ids_historial_usuario = []

    if historial_usuario:

        # Recorrer el diccionario e imprimir los valores de 'id_experiencia'
        for historial in historial_usuario:
            id_historial = historial.id_historial_academico
            ids_historial_usuario.append(id_historial)

        historials_filtradas = []

        for i in tipos_historial:
            if i.id in ids_historial_usuario:
                historials_filtradas.append(i)
        
        return historials_filtradas

    else:
        return []

def informacion_ia(usuario_id: int,db:Session) -> dict:

    UbicacionUsuario = obtener_ubicacion_usuario(usuario_id, db)
    Perfil= obtener_perfil_postulante_id(usuario_id, db)      
    Experiencias= obtener_especifica_experiencia(usuario_id, db)
    #Experiencias= obtener_experiencia_usuario(usuario_id, db)

    Vacantes= obtener_vacantes(db)
    Ubicaciones= obtener_ubicaciones(db)
    Historial = obtener_especifico_historial(usuario_id, db)
    return pruebas(
        UbicacionUsuario,
        Perfil,
        Experiencias,
        Vacantes,
        Ubicaciones,
        Historial
    )

