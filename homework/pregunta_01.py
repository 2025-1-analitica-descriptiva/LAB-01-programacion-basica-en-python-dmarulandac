"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""




def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    #interpretar la info como un data set
    suma= 0
    with open("files\input\data.csv","r") as file:
        for i in file:
            columnas=i.strip().split("\t")
            suma +=int(columnas[1])
    return suma
    
