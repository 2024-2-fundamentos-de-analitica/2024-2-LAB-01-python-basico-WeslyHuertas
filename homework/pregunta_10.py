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
        extract_multiple_columns,
        parse_column
)
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    data = load_data()
    column_1, column_4, column_5 = extract_multiple_columns([0, 3, 4], data)
    parsed_column_4 = parse_column(column_4, ",")
    parsed_column_5 = parse_column(column_5, ",")

    return [(column_1[indx], len(parsed_column_4[indx]), len(parsed_column_5[indx])) for indx in range(len(column_1))]

