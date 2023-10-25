# librerías a instalar:
# numpy
# pandas
# openpyxl
# matplotlib
# scikit-learn
# statsmodels

# cosas útiles:
# -> cómo hacer la refresión lineal y mostrarla:
#   -> https://realpython.com/linear-regression-in-python/
#   -> https://medium.com/analytics-vidhya/simple-linear-regression-with-example-using-numpy-e7b984f0d15e
# -> documentación de plot(): https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

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

def abline(slope, intercept):
    """
    robado de: https://stackoverflow.com/questions/7941226/how-to-add-line-based-on-slope-and-intercept
    """
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-r') # fmt = '[marker][line][color]'

data = p.read_csv('modelos/housing.csv')
#data = p.read_excel('modelos/housing.xlsx')

nOfColumns = len(data.columns)
i = 0
for c in data.columns:
    print(f'Columna número {i}: {c}')
    i += 1

column1Index = ask('Selecciona la primera columna: ', nOfColumns)
column2Index = ask('Selecciona la segunda columna: ', nOfColumns)
while column2Index == column1Index:
    column2Index = ask('Selecciona la segunda columna: ', nOfColumns)

selectedColumns = data.iloc[:, [column1Index, column2Index]]

x = np.array(selectedColumns.iloc[:, 0]).reshape((-1, 1)) # este es una columna con muchas filas
y = np.array(selectedColumns.iloc[:, 1])                  # este es una fila con muchas columnas

model = LinearRegression().fit(x, y)

intercept = model.intercept_ # término independiente
slope = model.coef_[0]
eq = f'{round(slope, 2)}x ' + ('+' if intercept > 0 else '-') + f' {round(abs(intercept), 2)}'

print(f'la recta de regresión es', eq)

r_sq = round(model.score(x, y), 2)
print(f"r cuadrado: {r_sq}")

plt.plot(x, y, '.k')
plt.ylabel(selectedColumns.columns[1])
plt.xlabel(selectedColumns.columns[0])
abline(slope, intercept)
plt.title(eq + f',   r^2: {r_sq}')
plt.grid()
plt.savefig("fig.png") #guarda la imagen para luego poder outputearla
plt.show()
