import customtkinter
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import simpledialog, filedialog
from pickle import dump, load
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from regression import plotLine, regression
from prediction import createPredictionFrame

def makeModel(data, root, screen, height, width, v1, v2): 
    makeAndShowGraph(regression(data, int(v1.get()), int(v2.get()), root), screen, height, width)


def makeAndShowGraph(model, screen, height, width):
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

    graphFrame = customtkinter.CTkFrame(screen, width = width*0.9, height = height*0.14)
    graphFrame.grid(row = 6, columnspan = 12)

    graphCanvas = FigureCanvasTkAgg(figure, graphFrame)
    graphCanvas.draw()
    graphCanvas.get_tk_widget().grid(row = 0, column = 0)

    plt.savefig('fig.png') # para guardarlo en un archivo

    graphFrame.grid_columnconfigure(1, minsize = width*0.10)
    customtkinter.CTkButton(graphFrame, text = "Guardar modelo", command = lambda: saveModelToPickleObject(model)).grid(row = 0, column = 2)

    createPredictionFrame(model, screen, height, width)


def saveModelToPickleObject(obj):
    modelDescription = simpledialog.askstring("Input", "Añade una descripción al modelo:")
    obj.set_description(modelDescription)
    fileName = filedialog.asksaveasfilename(defaultextension = ".pickle", filetypes = [("Pickle files", "*.pickle")])
    # Serializar el objeto y guardarlo en el archivo
    with open(fileName, "wb") as f:
        dump(obj, f)


def loadModelFromPickleObject(root, screen):
    root.filename = filedialog.askopenfile(initialdir="modelos/")
    with open(root.filename.name, "rb") as f:
        unpickedModel = load(f)
    customtkinter.CTkButton(screen, text = "Mostrar Modelo e Imagen", 
                            command = lambda: makeAndShowGraph(unpickedModel, screen)).grid(row = 6, column = 6)