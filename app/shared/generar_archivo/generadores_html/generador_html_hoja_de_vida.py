def generar_html_hoja_de_vida(datos_hoja_de_vida: dict):
    return f"""
    <body>
        <h1>Hoja de vida {datos_hoja_de_vida["usuario"]}</h1>
    </body>
    """
