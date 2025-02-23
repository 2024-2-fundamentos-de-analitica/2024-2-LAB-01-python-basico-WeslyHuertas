"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    # Leer el archivo CSV
    with open("C:/Users/user/Documents/Analitica_de_datos/2024-2-LAB-01-python-basico-WeslyHuertas/files/input/data.csv", 'r') as archivo:
        lector = csv.reader(archivo, delimiter=' ')
        answer = {}
        for fila in lector:
            line = fila[0].split('\t')
            answer[line[0]] = answer.get(line[0], 0) + int(line[1])  
    return sorted(answer.items())

print(pregunta_03())

