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
    load_data,
    extract_column,
    column_mapper_2,
    shuffle_and_sort,
    reducer
)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    data = load_data()
    column_1 = extract_column(0, data)
    column_2 = extract_column(1, data)

    content = column_mapper_2(column_1, column_2)
    content = shuffle_and_sort(content)
    content = reducer(content)

    return content

print(pregunta_03())


