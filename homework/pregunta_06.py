"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores = {}
    with open("files\input\data.csv", "r") as file:
        for linea in file:
            columnas = linea.strip().split("\t")
            # Verifica que hay al menos 5 columnas
            if len(columnas) >= 5:
                items = columnas[4].split(",")
                for item in items:
                    if ":" in item:
                        clave, valor = item.strip().split(":")
                        valor = int(valor)
                        if clave in valores:
                            valores[clave].append(valor)
                        else:
                            valores[clave] = [valor]

    resultado = []
    for clave in sorted(valores.keys()):
        minimo = min(valores[clave])
        maximo = max(valores[clave])
        resultado.append((clave, minimo, maximo))

    return resultado