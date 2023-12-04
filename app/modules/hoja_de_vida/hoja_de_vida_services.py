from sqlalchemy.orm import Session
from app.shared.generar_archivo.generar_archivo import FabricaDeArchivos
from app.shared.generar_archivo.tipo_plantilla import TipoPlantilla
from app.modules.usuario.usuario_services import obtener_usuario_por_id
from app.modules.perfil_postulante.perfil_postulante_services import obtener_perfil_postulante_por_usuario_id


def generar_hoja_de_vida(id_usuario: int, db: Session) -> str:
    '''Genera una hoja de vida en formato PDF y la retorna en base64'''
    datos = __obtener_datos_hoja_de_vida(id_usuario, db)
    return FabricaDeArchivos().generar_pdf(datos, TipoPlantilla.HOJA_DE_VIDA)


def __obtener_datos_hoja_de_vida(id_usuario: int, db: Session) -> dict:
    '''Obtiene los datos necesarios para generar una hoja de vida'''
    usuario = obtener_usuario_por_id(id_usuario,db)
    postulante = obtener_perfil_postulante_por_usuario_id(id_usuario,db)
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

    }
