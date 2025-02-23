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
    column_mapper_1,
    shuffle_and_sort,
    parse_column,
    parse_to_one_column,
    reducer
)
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,'bbb': 16,'ccc': 23,'ddd': 23,'eee': 15,'fff': 20,'ggg': 13,'hhh': 16,'iii': 18,
    'jjj': 18}}

    """
    data = load_data()
    column = extract_column(4, data)
    parsed_column = parse_column(column, ",")
    stuck_column = parse_to_one_column(parsed_column)
    content = parse_column(stuck_column, ":")
    registers = extract_column(0, content)
    content = column_mapper_1(registers)
    content = shuffle_and_sort(content)
    content = reducer(content, return_dict= True)
    return content

print(pregunta_09())

