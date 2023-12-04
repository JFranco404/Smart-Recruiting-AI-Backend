def generar_html_hoja_de_vida(datos_hoja_de_vida: dict):
    estilos = obtener_estilos()
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
        <h1>Hoja de vida {datos_hoja_de_vida["nombres"]}</h1>
        </header>

        <section>
        <h2>Información Personal</h2>
        <ul>
            <li><strong>Nombre:</strong> {datos_hoja_de_vida["nombres"]}</li>
            <li><strong>Lugar de Residencia:</strong> {datos_hoja_de_vida["lugar_residencia"]}</li>
            <li><strong>Correo:</strong> {datos_hoja_de_vida["correo"]}</li>
        </ul>
        </section>

        <section>
            <h2>Perfil Postulante</h2>
            <ul>
                <li><strong>Resumen:</strong> {datos_hoja_de_vida["resumen"]}</li>
                <li><strong>Habilidades:</strong> {datos_hoja_de_vida["habilidades"]}</li>
                <li><strong>Idiomas:</strong> {datos_hoja_de_vida["idiomas"]}</li>
                <li><strong>Enlace:</strong> {datos_hoja_de_vida["link"]}</li>
                <li><strong>Referencias:</strong> {datos_hoja_de_vida["referencias"]}</li>
            </ul>
        </section>
    </body>
    """

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

        li {
            margin-bottom: 5px;
        }

        a {
            color: #007BFF;
        }
    """


