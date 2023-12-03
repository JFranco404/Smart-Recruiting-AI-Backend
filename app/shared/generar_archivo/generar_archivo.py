import os
import base64
from xhtml2pdf import pisa
from .tipo_plantilla import TipoPlantilla
from .generadores_html.generador_html_hoja_de_vida import generar_html_hoja_de_vida


class FabricaDeArchivos:
    datos_del_pdf = None
    tipo_pdf = None
    html = ""
    string_base64 = ""
    direccion_pdf = os.path.dirname(
        os.path.abspath(__file__)) + "/archivo_pdf.pdf"

    def generar_pdf(self, datos_para_el_pdf: dict, tipo_pdf: int) -> str:
        self.definir_datos(datos_para_el_pdf, tipo_pdf)
        self.__generar_html()
        self.__generar_pdf()
        self.__generar_base64()
        # self.__borrar_pdf()
        return self.string_base64

    def definir_datos(self, datos_del_pdf: dict, tipo_del_pdf: int) -> None:
        self.datos_del_pdf = datos_del_pdf
        self.tipo_pdf = tipo_del_pdf

    def __generar_html(self) -> None:
        if self.tipo_pdf == TipoPlantilla.HOJA_DE_VIDA:
            self.html = generar_html_hoja_de_vida(self.datos_del_pdf)
        else:
            raise Exception("Tipo de plantilla no soportada")

    def __generar_pdf(self) -> None:
        with open(self.direccion_pdf, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(self.html, dest=pdf_file)
        return not pisa_status.err

    def __generar_base64(self) -> None:
        with open(self.direccion_pdf, "rb") as pdf_file:
            self.string_base64 = base64.b64encode(pdf_file.read()).decode(
                "utf-8")

    def __borrar_pdf(self) -> None:
        return os.remove(self.direccion_pdf)
