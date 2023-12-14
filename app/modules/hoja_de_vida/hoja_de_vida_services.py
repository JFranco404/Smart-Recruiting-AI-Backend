from sqlalchemy.orm import Session
from app.shared.generar_archivo.generar_archivo import FabricaDeArchivos
from app.shared.generar_archivo.tipo_plantilla import TipoPlantilla
from app.modules.usuario.usuario_services import obtener_usuario_por_id
from app.modules.perfil_postulante.perfil_postulante_services import obtener_perfil_postulante_por_usuario_id
from app.modules.educacion_por_perfil_postulante.educacion_por_perfil_postulante_services import obtener_educacion_por_perfil_postulante_por_postulante_id
from app.modules.experiencia_por_perfil_postulante.experiencia_por_perfil_postulante_services import obtener_experiencia_por_perfil_postulante_por_postulante_id


def generar_hoja_de_vida(id_usuario: int, db: Session) -> str:
    '''Genera una hoja de vida en formato PDF y la retorna en base64'''
    datos = __obtener_datos_hoja_de_vida(id_usuario, db)
    return FabricaDeArchivos().generar_pdf(datos, TipoPlantilla.HOJA_DE_VIDA)


def __obtener_datos_hoja_de_vida(id_usuario: int, db: Session) -> dict:
    '''Obtiene los datos necesarios para generar una hoja de vida'''
    usuario = obtener_usuario_por_id(id_usuario,db)
    postulante = obtener_perfil_postulante_por_usuario_id(id_usuario,db)
    educacion = obtener_educacion_por_perfil_postulante_por_postulante_id(id_usuario, db)
    experiencia = obtener_experiencia_por_perfil_postulante_por_postulante_id(id_usuario, db)

    return {
        "nombres": usuario.nombres,
        "apellidos": usuario.apellidos,
        "correo": usuario.correo,
        "lugar_residencia": usuario.lugar_residencia,
        "resumen": postulante.resumen,
        "habilidades": postulante.habilidades,
        "idiomas": postulante.idiomas,
        "link": postulante.link,
        "referencias": postulante.referencias,
        "educacion": educacion,
        "experiencia": experiencia
    }
