"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    min_max={}
    with open("files/input/data.csv","r") as file:
        for linea in file:
            columnas=linea.strip().split("\t")
            letra=columnas[0]
            numero=int(columnas[1])
            if letra in min_max:
                min_max[letra].append(numero)
            else:
                min_max[letra]=[numero]
    
    resultado=[]
    for letra in sorted(min_max.keys()):
        max_=max(min_max[letra])
        min_=min(min_max[letra])
        resultado.append((letra,max_,min_))

    return resultado