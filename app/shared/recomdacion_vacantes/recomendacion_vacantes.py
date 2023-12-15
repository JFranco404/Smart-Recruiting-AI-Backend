import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.modules.ia_recomendacion.datos_ia_models import *
from datetime import datetime

def pruebas(UbicacionUsuario,
        Perfil,
        Experiencias,
        Vacantes,
        Ubicaciones,
        Historial):
    if not Perfil:
        return {"message":"Es necesario completar el perfil para poder usar la IA"}
    return obtener_recomendacion(UbicacionUsuario,Perfil,Experiencias,Vacantes,Ubicaciones,Historial)
    #return {"message": Historial}


def obtener_recomendacion(UbicacionUsuario,Perfil,Experiencias,Vacantes,Ubicaciones,Historial):
    # datos usuario
    usuario_combinacion = procesamiento_data_usuario(UbicacionUsuario,Perfil,Experiencias,Historial)
    #NOTA: reemplazar los nullos por espacios.

    # datos vacante
    vac,combinacion = procesamiento_data_vacantes(Vacantes,Ubicaciones)

    # Obtenemos la columna de interes tanto para el usuario como para las vacantes.
    vacantes_combinacion = combinacion

    # hacemos uso de la funcion que deveulve los indices de las recomendaciones.
    indices = obtener_recomendacion_vacantes(usuario_combinacion, vacantes_combinacion)

    # filtramos el array con las vacantes recomendadas
    array_filtrado = [vac[i] for i in indices]

    return array_filtrado



def calcular_tiempo_en_anios(fecha_inicio, fecha_finalizacion):
    fecha_inicio = datetime.strptime(str(fecha_inicio), "%Y-%m-%d")
    fecha_finalizacion = datetime.strptime(str(fecha_finalizacion), "%Y-%m-%d")
    diferencia = fecha_finalizacion - fecha_inicio
    return diferencia.days / 365.25  # dividido por 365.25 para tener en cuenta los años bisiestos


def calculo_experiencia_usuario(Experiencias):
    total_anos = 0
    for exp in Experiencias:
        tiempo_en_anios = calcular_tiempo_en_anios(exp.fecha_inicio, exp.fecha_finalizacion)
        total_anos += tiempo_en_anios          
    return round(total_anos)

def obtener_titulos(Historial):
    titulos = ""
    area = ""

    for i in Historial:
        titulos = titulos+i.titulo_obtenido+" "

    for j in Historial:
        area = area+j.area_de_estudio+" "

    return titulos,area

def procesamiento_data_usuario(UbicacionUsuario,Perfil,Experiencias,Historial):
    anos_exp = calculo_experiencia_usuario(Experiencias) if Experiencias else 0
    if Historial:
        titulos, areas = obtener_titulos(Historial)
    else:
        titulos = " "
        areas = " "
    cuidad = UbicacionUsuario.ciudad if UbicacionUsuario else " "
    return f"cuidad:{cuidad};titulo:{titulos};area:{areas};experiencia:{anos_exp}"


def procesamiento_data_vacantes(Vacantes, Ubicaciones):

    vac = cambio_ubicacion(Vacantes, Ubicaciones)

    combinacion = []

    for i in vac:
        combinacion.append(f'ciudad:{i.ubicacion};titulo:{i.titulo};area:{i.area_trabajo};experiencia:{i.annos_experiencia}')

    return vac,combinacion

def cambio_ubicacion(Vacantes, Ubicaciones):


    # Crear un diccionario de ubicaciones para facilitar la búsqueda
    diccionario_ubicaciones = {ubicacion.id: ubicacion.ciudad for ubicacion in Ubicaciones}

    # Sustituir el ID de ubicación por el nombre de la ciudad en el array de Vacantes
    for vacante in Vacantes:
        id_ubicacion = vacante.ubicacion
        ciudad = diccionario_ubicaciones.get(id_ubicacion, " ")
        vacante.ubicacion = ciudad

    return Vacantes

def obtener_recomendacion_vacantes(perfil_candidato, datos_vacantes, num_recomendaciones=5):
    # ponemos el perfil del candidato al inicio del array
    corpus = [perfil_candidato] + datos_vacantes 
    # instanciamos el vectorizador
    vectorizador = TfidfVectorizer()
    # entrenamiento y transformacion de los datos
    vectores = vectorizador.fit_transform(corpus)
    # usando la metrica de los cosenos encontramos las mejores similitudes comparando el perfil
    # del usuario con cada una de las vacantes.
    similitudes = [cosine_similarity(vectores[0], vector)[0][0] for vector in vectores[1:]]
    # obtenemos los indices de las vacantes recomendadas
    indices_recomendados = sorted(range(len(similitudes)), key=lambda i: similitudes[i], reverse=True)[:num_recomendaciones]
    print("\nRecomendación de vacantes:")
    for indice in indices_recomendados:
        similitud = similitudes[indice]
        print(f"Índice: {indice}, Similitud Coseno: {similitud}")
        print(datos_vacantes[indice])
    
    return indices_recomendados