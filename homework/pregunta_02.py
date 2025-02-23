"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    # Leer el archivo CSV
    with open("C:/Users/user/Documents/Analitica_de_datos/2024-2-LAB-01-python-basico-WeslyHuertas/files/input/data.csv", 'r') as archivo:
        lector = csv.reader(archivo, delimiter=' ')
        answer = {}
        for fila in lector:
            line = fila[0].split('\t')
            answer[line[0]] = answer.get(line[0], 0) + 1  
    return sorted(answer.items())



