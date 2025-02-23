"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv
import Functions

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    data = Functions.load_data('../files/input/data.csv')
    column = Functions.extract_column(4, data)
    parsed_column = Functions.parse_column(column, ",")
    stuck_column = Functions.parse_to_one_column(parsed_column)
    content = Functions.parse_column(stuck_column, ":")
    registers = Functions.extract_column(0, content)
    content = Functions.column_mapper_1(registers)
    content = Functions.shuffle_and_sort(content)
    content = Functions.reducer(content, return_dict= True)
    return content
                


