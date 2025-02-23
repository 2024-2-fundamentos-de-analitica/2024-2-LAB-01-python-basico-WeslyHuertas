"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_06():
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

    # Leer el archivo CSV
    with open("C:/Users/user/Documents/Analitica_de_datos/2024-2-LAB-01-python-basico-WeslyHuertas/files/input/data.csv", 'r') as archivo:
        lector = csv.reader(archivo, delimiter=' ')
        valores = {}
        for fila in lector:
            line = fila[0].split('\t')[4]
            # Convertir a diccionario
            line_dict = {clave: int(valor) for clave, valor in (item.split(":") for item in line.split(","))}
            for letra in line_dict.keys():
                valor = line_dict[letra] 
                # Si la letra no está en el diccionario, inicializar con (valor, valor)
                if letra not in valores:
                    valores[letra] = (valor, valor)
                else:
                    # Actualizar los valores mínimo y máximo
                    min_val, max_val = valores[letra]
                    valores[letra] = (min(min_val, valor), max(max_val, valor))
                
    return sorted([(letra, min_val, max_val) for letra, (min_val, max_val) in valores.items()])
