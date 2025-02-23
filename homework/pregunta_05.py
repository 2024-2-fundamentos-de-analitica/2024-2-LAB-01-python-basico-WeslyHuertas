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
    max_min_reducer
)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data = load_data()
    column_1 = extract_column(0, data)
    column_2 = extract_column(1, data)

    content = column_mapper_2(column_1, column_2)
    content = shuffle_and_sort(content)
    return max_min_reducer(content)



print(pregunta_05())

