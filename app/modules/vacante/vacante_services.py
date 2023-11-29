from typing import List
from sqlalchemy.orm import Session
from app.modules.vacante.vacante_database_model import Vacante
from app.modules.vacante.vacante_models import DatosVacante, ActualizarVacante, FiltrosVacante
from app.modules.usuario.usuario_services import obtener_usuario_por_id
from sqlalchemy import or_, and_, func, extract

def obtener_vacante_por_filtro(filtros: FiltrosVacante, db: Session) -> List[Vacante]:
    """
    Busqueda de una vacante por interseccion de los filtros seleccionados.

    Raises:
        ValueError: Cuando el criterio de busqueda es ivalido o no exite.
    """
    
    query = db.query(Vacante)

    if filtros.titulo:
        query = query.filter(func.lower(Vacante.titulo).contains(func.lower(filtros.titulo)))
        
    if filtros.fecha_publicacion:
        query = query.filter(Vacante.fecha_publicacion == filtros.fecha_publicacion)

    if filtros.fecha_cierre:
        query = query.filter(Vacante.fecha_cierre == filtros.fecha_cierre)
    
    if filtros.salario:
        query = query.filter(Vacante.salario.between(filtros.salario * 0.9, filtros.salario * 1.1))
        
    if filtros.remoto is not None:
        if filtros.remoto:
            query = query.filter(Vacante.remoto == True)
        else:
            query = query.filter(Vacante.remoto == False)
    
    if filtros.modalidad:
        query = query.filter(func.lower(Vacante.modalidad).contains(func.lower(filtros.modalidad)))
        
    if filtros.ubicacion:
        query = query.filter(Vacante.ubicacion == filtros.ubicacion)
        
    if filtros.area_trabajo:
        query = query.filter(func.lower(Vacante.area_trabajo).contains(func.lower(filtros.area_trabajo)))
        
    if filtros.annos_experiencia:
        query = query.filter(Vacante.annos_experiencia == filtros.annos_experiencia)

    if not query:
        raise ValueError("No se proporcionaron filtros")

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
