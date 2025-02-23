"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import Functions

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    data = Functions.load_data('../files/input/data.csv')
    column_1, column_4 = Functions.extract_multiple_columns([1, 3], data)
    parsed_column_4 = Functions.parse_column(column_4, ",")

    content = Functions.parse_to_one_column_with_value(parsed_column_4, column_1)
    content = Functions.shuffle_and_sort(content)
    content = Functions.reducer(content, return_dict= True)
    return content