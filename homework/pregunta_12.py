"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import Functions

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    data = Functions.load_data()
    column_1, column_5 = Functions.extract_multiple_columns([0, 4], data)
    parsed_column_5 = Functions.parse_column(column_5, ",")

    content = Functions.parse_to_one_column_with_value(parsed_column_5, column_1, (lambda x: x))
    content = Functions.format_for_question_12(content)
    content = Functions.shuffle_and_sort(content)
    content = Functions.reducer(content, return_dict=True)
    return content