"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    # Leer el archivo CSV
    with open("C:/Users/user/Documents/Analitica_de_datos/2024-2-LAB-01-python-basico-WeslyHuertas/files/input/data.csv", 'r') as archivo:
        lector = csv.reader(archivo, delimiter=' ')
        valores = {}
        for fila in lector:
            line = fila[0].split('\t')
            letra = line[0]
            valor = line[1]
            # Si la letra no está en el diccionario, inicializar con (valor, valor)
            if letra not in valores:
                valores[letra] = (valor, valor)
            else:
                # Actualizar los valores mínimo y máximo
                min_val, max_val = valores[letra]
                valores[letra] = (min(min_val, valor), max(max_val, valor))
                
    return sorted([(letra, max_val, min_val) for letra, (min_val, max_val) in valores.items()])

print(pregunta_05())