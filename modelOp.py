import matplotlib.pyplot as plt

from tkinter import *
from tkinter import filedialog
from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkEntry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pickle import dump

from regression import SimpleLinearRegression
from prediction import createPredictionFrame


def makeModel(data, root, screen, height, width, v1, v2):
    """Genera y muestra el gráfico del modelo.

    Parameters
    ----------
    data: pandas.DataFrame
        Datos utilizados para generar el modelo
    root: tkinter.Tk
        Raíz de la interfaz gráfica
    screen: customtkinter.CTkFrame
        Marco de la interfaz donde se mostrará la gráfica
    height: int
        Altura de la pantalla
    width: int
        Ancho de la pantalla
    v1: Tkinter.IntVar
        Variable asociada a la variable x seleccionada
    v2: Tkinter.IntVar
        Variable asociada a la variable y seleccionada
    """
    aux = SimpleLinearRegression()
    makeAndShowGraph(aux.regression(data, int(v1.get()),
                     int(v2.get()), root), screen, height, width)


def makeAndShowGraph(model, screen, height, width):
    """Genera y muestra un gráfico basado en el modelo proporcionado.

    Parameters
    ----------
    model: classModel.Model
        Modelo generado a partir de los datos
    screen: customtkinter.CTkFrame
        Marco de la interfaz donde se mostrará la gráfica
    height: int
        Altura de la pantalla
    width: int
        Ancho de la pantalla
    """

    aux = SimpleLinearRegression()
    xColumn, yColumn = model.get_columnx(), model.get_columny()
    selectedColumns = model.get_selectedColumns()

    figure, axis = plt.subplots()
    axis.plot(xColumn, yColumn, '.k')
    axis.set_ylabel(selectedColumns.columns[1])
    axis.set_xlabel(selectedColumns.columns[0])
    aux.plotLine(model.get_slope(), model.get_intercept())
    equation = f'{round(model.get_slope(), 2)}x ' + ('+' if model.get_intercept()
                                                     > 0 else '-') + f' {round(abs(model.get_intercept()), 2)}'
    axis.set_title(
        f'y= {equation} / R²: {model.get_rsquare()} / MSE: {model.get_mse()}')
    axis.grid()

    graphFrame = CTkFrame(screen, width=width*0.9, height=height*0.14)
    graphFrame.grid(row=6, columnspan=12)

    graphCanvas = FigureCanvasTkAgg(figure, graphFrame)
    graphCanvas.draw()
    graphCanvas.get_tk_widget().grid(row=0, column=0, rowspan=9)

    plt.savefig('fig.png')  # para guardarlo en un archivo

    graphFrame.grid_columnconfigure(1, minsize=width*0.10)
    text = CTkLabel(graphFrame, text="Añade una descripción:").grid(
        row=3, column=2, sticky=S)
    modelDescription = CTkEntry(graphFrame)
    modelDescription.grid(row=4, column=2, sticky=N)

    CTkButton(graphFrame, text="Guardar modelo", command=lambda: chooseFileNameSaveModel(
        model, modelDescription.get())).grid(row=5, column=2, sticky=N)

    createPredictionFrame(model, screen, height, width)


def chooseFileNameSaveModel(object, modelDescription):
    """Abre una ventana de diálogo para que el usuario elija la ruta y nombre del archivo.

    Parameters
    ----------
    object: obj
        El modelo que se va a guardar
    modelDescription: str
        Descripción del modelo que se va a guardar
    """
    while True:
        try:
            fileName = filedialog.asksaveasfilename(defaultextension=".pickle", filetypes=[
                                                    ("Pickle files", "*.pickle")])
            saveModelToPickleObject(object, modelDescription, fileName)
            break
        except FileNotFoundError:
            print('Por favor, introduce un nombre para el archivo archivo.')


def saveModelToPickleObject(object, modelDescription, name):
    """Guarda el modelo serializado en un archivo.

    Parameters
    ----------
    object: obj
        El objeto del modelo que se va a guardar
    modelDescription: str
         Descripción del modelo que se va a guardar
    name: str
        Nombre del archivo que se va a guardar
    """

    object.set_description(modelDescription)

    # Serializar el objeto y guardarlo en el archivo
    with open(name, "wb") as f:
        dump(object, f)
