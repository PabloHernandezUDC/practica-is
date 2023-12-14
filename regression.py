import numpy as np
import class_model
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tkinter import *

def abline(slope, intercept):
    axes = plt.gca() 
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-r') # formato = '[marker][line][color]'


def regression(data, i, j, root):
    plt.clf() # limpiamos la gráfica para no sobreescribir o pisar la anterior
    selectedColumns = data.iloc[:, [i, j]]

    name_x = data.columns[i]
    name_y = data.columns[j]

    x = np.array(selectedColumns.iloc[:, 0]).reshape((-1, 1)) # este es una columna con muchas filas
    y = np.array(selectedColumns.iloc[:, 1])                  # este es una fila con muchas columnas

    model = LinearRegression().fit(x, y)

    intercept = model.intercept_ # término independiente
    slope = model.coef_[0] 
    r_sq = round(model.score(x, y), 2)
    meanSquaredError = np.mean((model.predict(x) - y)**2)
    meanSquaredError = round(meanSquaredError, 2)
    
    modelo_obj = class_model.Model(intercept, slope, r_sq, meanSquaredError, selectedColumns, x, name_x, y, name_y, root.filename.name)
    return modelo_obj
