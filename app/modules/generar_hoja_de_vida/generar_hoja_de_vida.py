import jinja2
import pdfkit
import os

def crea_pdf(ruta_template,info,rutacss=''):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template,'')

    env = jinja2.Environment(loader=jinja2.FileSystemLoader (ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)

    options = {'page-size':'Letter',
              'margin-top':'0.05in',
              'margin-right':'0.05in',
              'margin-bottom':'0.05in',
              'margin-left':'0.05in', 
              'encoding':'UTF-8'}
    
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    ruta_salida = 'D:/Users/Usuario/Documents/Programacion/IngSoftware2/Smart-Recruiting-AI-Backend/app/modules/generar_hoja_de_vida/hoja_de_vida_generada/hoja_de_vida.pdf'
    pdfkit.from_string(html,ruta_salida,options=options,configuration=config)

if __name__ == "__main__":
    ruta_template = 'D:/Users/Usuario/Documents/Programacion/IngSoftware2/Smart-Recruiting-AI-Backend/app/modules/generar_hoja_de_vida/plantilla.html'
    info = {
    "nombres": "Juan",
    "apellidos": "Gómez",
    "lugar_Residencia": "Ciudad A",
    "correo": "juan.gomez@example.com",
    "resumen": "Profesional con experiencia en el desarrollo de software.",
    "habilidades": "Desarrollo web, gestión de proyectos",
    "idiomas": "Inglés (Avanzado), Español (Nativo)",
    "link": "https://linkedin.com/in/juangomez",
    "referencias": "Disponibles a petición",
    "nombre_Empresa": "ABC Solutions",
    "contacto": "Maria Rodriguez",
    "titulo_Cargo": "Desarrollador Senior",
    "fecha_Inicio": "2019-03-01",
    "fecha_Finalizacion": "2022-12-31",
    "responsabilidades": "Desarrollo y mantenimiento de aplicaciones web.",
    "titulo_Obtenido": "Ingeniero en Informática",
    "institucion": "Universidad Nacional",
    "area_de_Estudio": "Ingeniería de Sistemas",
    "promedio_Ponderado": "9.0",
    "reconocimientos": "Mejor Proyecto de Grado"
}
    crea_pdf(ruta_template, info)
