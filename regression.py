import numpy as np
import class_model
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tkinter import *

def plotLine(slope, intercept):
    axes = plt.gca() 
    xValues = np.array(axes.get_xlim())
    yValues = intercept + slope * xValues
    plt.plot(xValues, yValues, '-r') # formato = '[marker][line][color]'


def regression(data, xVariable, yVariable, root):
    plt.clf() # limpiamos la gráfica para no sobreescribir o pisar la anterior
    selectedColumns = data.iloc[:, [xVariable, yVariable]]

    xName = data.columns[xVariable]
    yName = data.columns[yVariable]

    xValues = np.array(selectedColumns.iloc[:, 0]).reshape((-1, 1)) # este es una columna con muchas filas
    yValues = np.array(selectedColumns.iloc[:, 1])                  # este es una fila con muchas columnas

    model = LinearRegression().fit(xValues, yValues)

    intercept = model.intercept_ # término independiente
    slope = model.coef_[0] 
    rSquared = round(model.score(xValues, yValues), 2)
    meanSquaredError = np.mean((model.predict(xValues) - yValues)**2)
    meanSquaredError = round(meanSquaredError, 2)
    
    return class_model.Model(intercept, slope, rSquared, meanSquaredError, selectedColumns, xValues, xName, yValues, yName, root.filename.name)