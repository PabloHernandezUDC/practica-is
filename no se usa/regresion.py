import pandas as p
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def abline(slope, intercept):
    """
    robado de: https://stackoverflow.com/questions/7941226/how-to-add-line-based-on-slope-and-intercept
    """
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-r') # fmt = '[marker][line][color]'

def regresionF(data,i,j):
    selectedColumns = data.iloc[:, [i, j]]
    x = np.array(selectedColumns.iloc[:, 0]).reshape((-1, 1)) # este es una columna con muchas filas
    y = np.array(selectedColumns.iloc[:, 1])

    model = LinearRegression().fit(x, y)

    intercept = model.intercept # término independiente
    slope = model.coef_[0]
    eq = f'{round(slope, 2)}x ' + ('+' if intercept > 0 else '-') + f' {round(abs(intercept), 2)}'

    r_sq = round(model.score(x, y), 2)
    plt.plot(x, y, '.k')
    plt.ylabel(selectedColumns.columns[1])
    plt.xlabel(selectedColumns.columns[0])
    abline(slope, intercept)
    plt.title(eq + f',   r^2: {r_sq}')
    plt.grid()
    plt.savefig("fig.png") # guarda la imagen para luego poder outputearla
