def generar_html_hoja_de_vida(datos_hoja_de_vida: dict):
    estilos = obtener_estilos()
    educacion = obtener_educacion(datos_hoja_de_vida["educacion"])
    experiencia = obtener_experiencia(datos_hoja_de_vida["experiencia"])
    return f"""
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hoja de Vida</title>
    <style>
       {estilos} 
    </style>
    </head>
    <body>
        <header>
        <h1>Hoja de vida de {datos_hoja_de_vida["nombres"]}</h1>
        </header>

        <section>
        <h2>Información Personal</h2>
        <ul>
            <div><strong>Nombre:</strong> {datos_hoja_de_vida["nombres"]}</div>
            <div><strong>Lugar de Residencia:</strong> {datos_hoja_de_vida["lugar_residencia"]}</div>
            <div><strong>Correo:</strong> {datos_hoja_de_vida["correo"]}</div>
        </ul>
        </section>

        <section>
            <h2>Perfil Postulante</h2>
            <ul>
                <div><strong>Resumen:</strong> {datos_hoja_de_vida["resumen"]}</div>
                <div><strong>Habilidades:</strong> {datos_hoja_de_vida["habilidades"]}</div>
                <div><strong>Idiomas:</strong> {datos_hoja_de_vida["idiomas"]}</div>
                <div><strong>Enlace:</strong> {datos_hoja_de_vida["link"]}</div>
                <div><strong>Referencias:</strong> {datos_hoja_de_vida["referencias"]}</div>
            </ul>
        </section>

        <section>
            <h2>Historial Académico</h2>
                {educacion}
        </section>

        <section>
            <h2>Experiencia Laboral</h2>
                {experiencia}
            
        </section>
    </body>
    """

def obtener_educacion(lista_educacion):
    lista_html = ""
    for educacion in lista_educacion:
        lista_html+=f"""

            <ul>
                <div><strong>Título obtenido:</strong> {educacion.titulo_obtenido}</div>
                <div><strong>Institución:</strong> {educacion.institucion}</div>
                <div><strong>Área de estudio:</strong> {educacion.area_de_estudio}</div>
                <div><strong>Fecha de inicio:</strong> {educacion.fecha_inicio}</div>
                <div><strong>Fecha de finalización:</strong> {educacion.fecha_finalizacion}</div>
                <div><strong>Promedio ponderado:</strong> {educacion.promedio_ponderado}</div>
                <div><strong>Reconocimientos:</strong> {educacion.reconocimientos}</div>
            </ul>
            <br>

        """
    return lista_html

def obtener_experiencia(lista_experiencia):
    lista_html = ""
    for experiencia in lista_experiencia:
        lista_html+=f"""

            <ul>
                <div><strong>Nombre de la empresa:</strong> {experiencia.nombre_empresa}</div>
                <div><strong>Contacto:</strong> {experiencia.contacto}</div>
                <div><strong>Tipo de cargo:</strong> {experiencia.tipo_cargo}</div>
                <div><strong>Fecha de inicio:</strong> {experiencia.fecha_inicio}</div>
                <div><strong>Fecha de finalización:</strong> {experiencia.fecha_finalizacion}</div>
                <div><strong>Responsabilidades:</strong> {experiencia.responsabilidades}</div>
            </ul>
            <br>

        """
    return lista_html

def obtener_estilos():
    return """
    body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            text-align: center;
        }

        section {
            margin-bottom: 20px;
        }

        h2 {
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }

        p {
            margin: 0;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        div {
            margin-bottom: 0;
            line-height: 1;
        }

        a {
            color: #007BFF;
        }
    """