import os
import base64
from xhtml2pdf import pisa
from .tipo_plantilla import TipoPlantilla
from .generadores_html.generador_html_hoja_de_vida import generar_html_hoja_de_vida


class FabricaDeArchivos:
    datos_del_archivo = None
    tipo_documento = None
    html = ""
    string_base64 = ""
    direccion_archivo = os.path.dirname(
        os.path.abspath(__file__)) + "/archivo_generado.pdf"

    def generar_pdf(self, datos_para_el_pdf: dict, tipo_pdf: int) -> str:
        '''Genera un archivo PDF en base64'''
        self.definir_datos(datos_para_el_pdf, tipo_pdf)
        self.__generar_html()
        self.__generar_pdf()
        self.__generar_base64()
        self.__borrar_archivo()
        return self.string_base64

    def definir_datos(self, datos_del_pdf: dict, tipo_del_pdf: int) -> None:
        self.datos_del_archivo = datos_del_pdf
        self.tipo_documento = tipo_del_pdf

    def __generar_html(self) -> None:
        '''Genera el HTML del PDF'''
        if self.tipo_documento == TipoPlantilla.HOJA_DE_VIDA:
            self.html = generar_html_hoja_de_vida(self.datos_del_archivo)
        else:
            raise Exception("Tipo de plantilla no soportada")

    def __generar_pdf(self) -> None:
        '''Crea el archivo PDF'''
        with open(self.direccion_archivo, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(self.html, dest=pdf_file)
        return not pisa_status.err

    def __generar_base64(self) -> None:
        '''Genera el string base64 del archivo'''
        with open(self.direccion_archivo, "rb") as archivo:
            self.string_base64 = base64.b64encode(archivo.read()).decode(
                "utf-8")

    def __borrar_archivo(self) -> None:
        return os.remove(self.direccion_archivo)
