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
    parse_column,
    parse_to_one_column_with_value,
    shuffle_and_sort,
    reducer
)

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    data = load_data()
    column_1, column_4 = extract_multiple_columns([1, 3], data)
    parsed_column_4 = parse_column(column_4, ",")

    content = parse_to_one_column_with_value(parsed_column_4, column_1)
    content = shuffle_and_sort(content)
    content = reducer(content, return_dict= True)
    return content
    
print(pregunta_11())
