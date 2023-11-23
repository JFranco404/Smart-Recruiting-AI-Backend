from typing import List
from sqlalchemy.orm import Session
from app.modules.vacante.vacante_database_model import Vacante
from app.modules.vacante.vacante_models import DatosVacante, ActualizarVacante, FiltrosVacante
from app.modules.usuario.usuario_services import obtener_usuario_por_id
from sqlalchemy import or_, func, extract

def obtener_vacante_por_filtro(filtros: FiltrosVacante, db: Session) -> List[Vacante]:
    """
    Obtiene vacantes filtradas según diferentes campos de la vacante.

    Raises:
        ValueError: Cuando el campo para filtrar no existe.
    """
    query = db.query(Vacante)
    criterios = []

    if filtros.titulo is not None:
        criterios.append(func.lower(Vacante.titulo).contains(func.lower(filtros.titulo)))
        
    if filtros.fecha_publicacion is not None:
        fecha_publicacion = filtros.fecha_publicacion
        if fecha_publicacion.year and not fecha_publicacion.month and not fecha_publicacion.day:
            criterios.append(extract('year', Vacante.fecha_publicacion) == fecha_publicacion.year)
        elif not fecha_publicacion.year and fecha_publicacion.month and not fecha_publicacion.day:
            criterios.append(extract('month', Vacante.fecha_publicacion) == fecha_publicacion.month)
        elif fecha_publicacion.year and fecha_publicacion.month and not fecha_publicacion.day:
            criterios.extend([
                extract('year', Vacante.fecha_publicacion) == fecha_publicacion.year,
                extract('month', Vacante.fecha_publicacion) == fecha_publicacion.month
            ])
        else:
            criterios.append(Vacante.fecha_publicacion == fecha_publicacion)
    
    if filtros.fecha_cierre is not None:
        fecha_cierre = filtros.fecha_cierre
        if fecha_cierre.year and not fecha_cierre.month and not fecha_cierre.day:
            criterios.append(extract('year', Vacante.fecha_cierre) == fecha_cierre.year)
        elif not fecha_cierre.year and fecha_cierre.month and not fecha_cierre.day:
            criterios.append(extract('month', Vacante.fecha_cierre) == fecha_cierre.month)
        elif fecha_cierre.year and fecha_cierre.month and not fecha_cierre.day:
            criterios.extend([
                extract('year', Vacante.fecha_cierre) == fecha_cierre.year,
                extract('month', Vacante.fecha_cierre) == fecha_cierre.month
            ])
        else:
            criterios.append(Vacante.fecha_cierre == fecha_cierre)
    
    if filtros.salario is not None:
        criterios.append(Vacante.salario.between(filtros.salario * 0.9, filtros.salario * 1.1))
        
    if filtros.remoto is not None:
        criterios.append(Vacante.remoto == filtros.remoto)
        
    if filtros.modalidad is not None:
        criterios.append(func.lower(Vacante.modalidad).contains(func.lower(filtros.modalidad)))
        
    if filtros.ubicacion is not None:
        criterios.append(Vacante.ubicacion == filtros.ubicacion)
        
    if filtros.area_trabajo is not None:
        criterios.append(func.lower(Vacante.area_trabajo).contains(func.lower(filtros.area_trabajo)))
        
    if filtros.annos_experiencia is not None:
        criterios.append(Vacante.annos_experiencia == filtros.annos_experiencia)

    if not criterios:
        raise ValueError("No se proporcionaron filtros")

    # Crear una lista de condiciones para el filtro OR
    query = query.filter(or_(*criterios))

    vacantes_filtradas = query.all()
    return vacantes_filtradas

    

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


def crear_vacante(vacante: DatosVacante, db: Session) -> Vacante:
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


def actualizar_vacante(vacante: ActualizarVacante, db: Session) -> Vacante:
    """
    Actualiza una vacante.

    Raises:
        ValueError: Cuando la vacante no es encontrada.
        ValueError: Cuando el usuario no es encontrado.
        ValueError: Cuando existe una vacante con el mismo titulo.
        ValueError: Cuando existe una vacante con la misma descripcion.
    """

    vacante_encontrada = db.query(Vacante).filter(
        Vacante.id == vacante.id).first()
    if not vacante_encontrada:
        raise ValueError("La vacante no existe")

    usuario_reclutador = obtener_usuario_por_id(vacante.usuario_reclutador, db)
    if not usuario_reclutador:
        raise ValueError("El usuario reclutador no existe")

    vacantes_del_reclutador = obtener_vacantes_por_usuario_reclutador_id(
        vacante.usuario_reclutador, db)

    for vacante_del_reclutador in vacantes_del_reclutador:
        if vacante_del_reclutador.titulo == vacante.titulo and vacante_del_reclutador.id != vacante.id:
            raise ValueError("Ya existe una vacante con el mismo titulo")
        if vacante_del_reclutador.descripcion == vacante.descripcion and vacante_del_reclutador.id != vacante.id:
            raise ValueError("Ya existe una vacante con la misma descripcion")

    vacante_encontrada.titulo = vacante.titulo
    vacante_encontrada.descripcion = vacante.descripcion
    vacante_encontrada.usuario_reclutador = vacante.usuario_reclutador
    vacante_encontrada.fecha_publicacion = vacante.fecha_publicacion
    vacante_encontrada.fecha_cierre = vacante.fecha_cierre
    vacante_encontrada.salario = vacante.salario
    vacante_encontrada.remoto = vacante.remoto
    vacante_encontrada.modalidad = vacante.modalidad
    vacante_encontrada.ubicacion = vacante.ubicacion
    vacante_encontrada.area_trabajo = vacante.area_trabajo
    vacante_encontrada.annos_experiencia = vacante.annos_experiencia

    db.commit()
    db.refresh(vacante_encontrada)

    return vacante_encontrada
