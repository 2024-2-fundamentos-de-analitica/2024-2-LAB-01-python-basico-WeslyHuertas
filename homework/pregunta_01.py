"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function.functions import (
    load_data
)
def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    data = load_data()
    colSum = 0
    for row in data:
        colSum += int(row[1])

    return colSum

print(pregunta_01())