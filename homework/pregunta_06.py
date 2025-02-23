"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
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

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function.functions import (
    load_data,
    extract_column,
    column_mapper_2,
    shuffle_and_sort,
    max_min_reducer,
    parse_column,
    parse_to_one_column,
    extract_multiple_columns
)

def pregunta_06():
    data = load_data()
    column = extract_column(4, data)
    parsed_column = parse_column(column, ",")
    stuck_column = parse_to_one_column(parsed_column)
    content = parse_column(stuck_column, ":")
    key, values= extract_multiple_columns(range(2), content)
    content = column_mapper_2(key, values)
    content = shuffle_and_sort(content)
  
    return max_min_reducer(content, reversed= True)

print(pregunta_06())