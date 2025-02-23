"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0

    # Leer el archivo CSV
    with open("C:/Users/user/Documents/Analitica_de_datos/2024-2-LAB-01-python-basico-WeslyHuertas/files/input/data.csv", 'r') as archivo:
        lector = csv.reader(archivo, delimiter=' ')
        for fila in lector:
            suma += float(fila[0].split('\t')[1])  # Convertir la segunda columna a float y sumar
    return suma
      

