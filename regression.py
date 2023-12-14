import numpy as np
import classModel
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from tkinter import *

def plotLine(slope, intercept):
    """Genera una gráfica de línea a partir de la pendiente y el término independiente.

    Parameters
    ----------
    slope: float
        Pendiente de la línea.
    intercept: float
        Término independiente de la línea.
    """

    axes = plt.gca() 
    xValues = np.array(axes.get_xlim())
    yValues = intercept + slope * xValues
    plt.plot(xValues, yValues, '-r') # formato = '[marker][line][color]'


def regression(data, xVariable, yVariable, root):
    """Realiza una regresión lineal y devuelve un objeto de la clase Model.

    Parameters
    ----------
    data: pandas.DataFrame
        Conjunto de datos a partir del cuál se realiza la regresión.
    xVariable: int
        Indice de la columna x de los datos.
    yVariable: int
        Indice de la columna y de los datos.
    root: tkinter.Tk
        Objeto raíz de la interfaz gráfica.

    Returns
    -------
    Model: classModel.Model
        Objeto de la clase Model con los resultados de la regresión.
    """

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
    
    return classModel.Model(intercept, slope, rSquared, meanSquaredError, selectedColumns, xValues, xName, yValues, yName, root.filename.name)