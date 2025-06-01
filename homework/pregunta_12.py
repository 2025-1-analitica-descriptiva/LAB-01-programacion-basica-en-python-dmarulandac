"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = {}

    with open("files/input/data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            letra = columnas[0]
            pares = columnas[4].split(",") if len(columnas) > 4 else []

            suma_valores = 0
            for par in pares:
                if ":" in par:
                    _, valor = par.split(":")
                    suma_valores += int(valor)

            if letra not in suma_por_letra:
                suma_por_letra[letra] = 0
            suma_por_letra[letra] += suma_valores

    return dict(sorted(suma_por_letra.items()))
