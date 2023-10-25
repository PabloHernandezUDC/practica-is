# librerías a instalar:
# numpy
# pandas
# openpyxl
# matplotlib
# scikit-learn
# statsmodels

# cosas útiles:
# https://realpython.com/linear-regression-in-python/

import sys
import pandas as p
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

def r(e, n):
    return round(e, n)

print('hola gilberto')

data = p.read_csv('modelos/housing.csv')
#data = p.read_excel('modelos/housing.xlsx')

nOfColumns = len(data.columns)
i = 0
for c in data.columns:
    print(f'Columna número {i}: {c}')
    i += 1

column1Index = ask('Selecciona la primera columna: ', 10)
column2Index = ask('Selecciona la segunda columna: ', 10)
while column2Index == column1Index:
    column2Index = ask('Selecciona la segunda columna: ', 10)

selectedColumns = data.iloc[:, [column1Index, column2Index]]

x = np.array(selectedColumns.iloc[:, 0]).reshape((-1, 1)) # este es una columna con muchas filas
y = np.array(selectedColumns.iloc[:, 1])                  # este es una fila con muchas columnas

model = LinearRegression().fit(x, y)

intercept = model.intercept_ # término independiente
slope = model.coef_[0]

print(f'la recta de regresión es {r(slope, 2)}x + {r(intercept, 2)}')

r_sq = model.score(x, y)
print(f"r cuadrado: {r(r_sq, 2)}")