import matplotlib.pyplot as plt

from tkinter import simpledialog, filedialog, E
from customtkinter import CTkButton, CTkFrame, CTkLabel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pickle import dump, load
from dataOp import readFile 
from regression import plotLine, regression
from prediction import createPredictionFrame


def makeModel(data, root, screen, height, width, v1, v2):
    """Genera y muestra el gráfico del modelo.

    Parameters
    ----------
    data: pandas.DataFrame
        Datos utilizados para generar el modelo.
    root: Tkinter.Tk
        Raíz de la interfaz gráfica.
    screen: Tkinter.Frame
        Marco de la interfaz donde se mostrará la gráfica.
    height: int
        Altura de la pantalla.
    width: int
        Ancho de la pantalla.
    v1: Tkinter.IntVar
        Variable asociada a la variable x seleccionada.
    v2: TkinterIntVar
        Variable asociada a la variable y seleccionada.
    """

    makeAndShowGraph(regression(data, int(v1.get()), int(v2.get()), root), screen, height, width)


def makeAndShowGraph(model, screen, height, width):
    """Genera y muestra un gráfico basado en el modelo proporcionado.

    Parameters
    ----------
    model: Model
        Modelo generado a partir de los datos.
    screen: Tkinter.Frame
        Marco de la interfaz donde se mostrará la gráfica.
    height: int
        Altura de la pantalla.
    width: int
        Ancho de la pantalla.
    """

    xColumn, yColumn = model.get_columnx(), model.get_columny()
    selectedColumns = model.get_selectedColumns()

    figure, axis = plt.subplots()
    axis.plot(xColumn, yColumn, '.k')
    axis.set_ylabel(selectedColumns.columns[1])
    axis.set_xlabel(selectedColumns.columns[0])
    plotLine(model.get_slope(), model.get_intercept())
    equation = f'{round(model.get_slope(), 2)}x ' + ('+' if model.get_intercept() > 0 else '-') + f' {round(abs(model.get_intercept()), 2)}'
    axis.set_title(f'y= {equation} / R²: {model.get_rsquare()} / MSE: {model.get_mse()}')
    axis.grid()

    graphFrame = CTkFrame(screen, width = width*0.9, height = height*0.14)
    graphFrame.grid(row = 6, columnspan = 12)

    graphCanvas = FigureCanvasTkAgg(figure, graphFrame)
    graphCanvas.draw()
    graphCanvas.get_tk_widget().grid(row = 0, column = 0)

    plt.savefig('fig.png') # para guardarlo en un archivo

    graphFrame.grid_columnconfigure(1, minsize = width*0.10)
    CTkButton(graphFrame, text = "Guardar modelo", command = lambda: saveModelToPickleObject(model)).grid(row = 0, column = 2)

    createPredictionFrame(model, screen, height, width)


def saveModelToPickleObject(obj):
    """Guarda el modelo serializado en un archivo.

    Parameters
    ----------
    obj: obj
        El objeto del modelo que se va a guardar.
    """

    modelDescription = simpledialog.askstring("Input", "Añade una descripción al modelo:")
    obj.set_description(modelDescription)
    fileName = filedialog.asksaveasfilename(defaultextension = ".pickle", filetypes = [("Pickle files", "*.pickle")])
    # Serializar el objeto y guardarlo en el archivo
    with open(fileName, "wb") as f:
        dump(obj, f)


def loadModelFromPickleObject(root, screen, height, width):
    """Carga un modelo serializado desde un archivo.

    Parameters
    ----------
    root: Tkinter.Tk
        Raíz de la interfaz gráfica.
    screen: Tkinter.Frame
        Marco de la interfaz donde se mostrará el modelo y la imagen.
    """



    def clear_frame(screen):
        for widgets in screen.winfo_children():
            widgets.destroy()


    clear_frame(screen)

    chooseFileButton = CTkButton(screen,
                                               text = "Elegir archivo",
                                               command = lambda: readFile(width,
                                                                          height,
                                                                          root,
                                                                          screen)).grid(row = 1,
                                                                                             column = 5)
    loadModelButton = CTkButton(screen,
                                              text = "Cargar modelo",
                                              command = lambda: loadModelFromPickleObject(root,
                                                                                          screen,
                                                                                          height,
                                                                                          width)).grid(row = 2,
                                                                                                             column = 5)
    
    root.filename = filedialog.askopenfile(initialdir="modelos/")
    with open(root.filename.name, "rb") as f:
        unpickedModel = load(f)
    routeText = CTkLabel(screen, text="Ruta:")
    routeText.grid(row = 1, column = 3)
    
    # CREAR UNA ETIQUETA PARA MOSTRAR LA RUTA DEL ARCHIVO
    filePath = CTkLabel(screen, text = root.filename.name)
    filePath.grid(row = 1, column = 4)


    slope = unpickedModel.get_slope()
    intercept = unpickedModel.get_intercept()
    squareR = unpickedModel.get_rsquare()
    mse = unpickedModel.get_mse()

    modelFrame = CTkFrame(screen, width = width*0.9, height = height*0.14)
    modelFrame.grid(row = 4, columnspan = 30)
    modelFrame.grid_rowconfigure(0, minsize = height*0.1)

    equationLabel = CTkLabel(modelFrame, text = f"y = {round(slope, 2)} x + {round(intercept, 2)}") 
    equationLabel.grid(row = 1, column = 4, columnspan = 5)

    rSquareLabel = CTkLabel(modelFrame, text = f" R^2 : {squareR}   MSE : {mse}")
    rSquareLabel.grid(row = 2, column = 5)

    #mseLabel = CTkLabel(modelFrame, text = f" MSE: {mse}")
    #mseLabel.grid(row = 2, column = 5, columnspan = 1)

    descriptionLabel = CTkLabel(modelFrame, text = f'Descripción del modelo: {unpickedModel.get_description()}')
    descriptionLabel.grid(row = 3, column = 5)

    createPredictionFrame(unpickedModel, screen, height, width)

    #CTkButton(screen, text = "Mostrar Modelo e Imagen", command = lambda: cositas(screen, unpickedModel)).grid(row = 6, column = 6)
