# librerías a instalar:
# numpy
# pandas
# openpyxl
# pyqt6 (https://zetcode.com/pyqt6/)

import sys
import pandas as p
import numpy as np

def ask(text, range):
    while True:
        try:
            result = int(input(text))
            if result < 0:
                print('Introduce un número positivo.')
                continue
            if result > range and range != 0:
                print(f'Introduce un número menor que {range}.')
                continue
            break
        except ValueError:
            print('Eso no es un número válido.')

    return result

print('hola gilberto')

modelo_csv = p.read_csv('modelos/housing.csv')
#modelo_excel = p.read_excel('modelos/housing.xlsx')

n_de_columnas = len(modelo_csv.columns)
i = 0
for c in modelo_csv.columns:
    print(f'Columna número {i}: {c}')
    i += 1

columna1Index = ask('Selecciona la primera columna', 10)
columna2Index = ask('Selecciona la segunda columna', 10)

while columna2Index == columna1Index:
    columna2Index = ask('Selecciona la segunda columna', 10)

print(f'La primera columna es {modelo_csv.columns[columna1Index]} y la segunda es {modelo_csv.columns[columna2Index]}')


