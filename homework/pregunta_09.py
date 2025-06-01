"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

     
    """
    conteo_claves = {}
    with open("files\input\data.csv", "r") as file:
        for linea in file:
            partes = linea.strip().split("\t")

            if len(partes) < 5:
                continue  # la línea no tiene una columna 5

            columna_5 = partes[4].strip()
            if columna_5 == "":
                continue  # la columna 5 está vacía

            pares = columna_5.split(",")
            for par in pares:
                if ":" in par:
                    clave, _ = par.split(":")
                    if clave not in conteo_claves:
                        conteo_claves[clave] = 0
                    conteo_claves[clave] += 1

    return conteo_claves