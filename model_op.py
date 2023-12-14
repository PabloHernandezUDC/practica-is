import customtkinter
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import simpledialog, filedialog
from pickle import dump, load
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from regression import abline, regression
from prediction import predcitionFrame


def makeModel(data, root, screen, height, width, v1, v2): 
    num1, num2 = int(v1.get()), int(v2.get())

    model = regression(data, num1, num2, root)
    makeAndShowGraph(model, screen, height, width)

def makeAndShowGraph(model, screen, height, width):
    x, y = model.get_columnx(), model.get_columny()
    selectedColumns = model.get_selectedColumns()

    fig, ax = plt.subplots()
    ax.plot(x, y, '.k')
    ax.set_ylabel(selectedColumns.columns[1])
    ax.set_xlabel(selectedColumns.columns[0])
    abline(model.get_slope(), model.get_intercept())
    eq = f'{round(model.get_slope(), 2)}x ' + ('+' if model.get_intercept() > 0 else '-') + f' {round(abs(model.get_intercept()), 2)}'
    ax.set_title(f'y= {eq} / R²: {model.get_rsquare()} / MSE: {model.get_mse()}')
    ax.grid()

    frameGraph = customtkinter.CTkFrame(screen, width=width*0.9, height=height*0.14)
    frameGraph.grid(row = 6, columnspan=12)

    canvas = FigureCanvasTkAgg(fig, frameGraph)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 0, column = 0)

    filename = 'fig.png'
    plt.savefig(filename) # para guardarlo en un archivo

    frameGraph.grid_columnconfigure(1, minsize=width*0.10)
    customtkinter.CTkButton(frameGraph, text = "Guardar modelo", command = lambda: guardar_modelo(model)).grid(row = 0, column = 2)

    predcitionFrame(model, screen, height, width)

def guardar_modelo(obj):
    description = simpledialog.askstring("Input", "Añade una descripción al modelo:")
    obj.set_description(description)
    file_name = filedialog.asksaveasfilename(defaultextension = ".pickle", filetypes = [("Pickle files", "*.pickle")])
    # Serializar el objeto y guardarlo en el archivo
    with open(file_name, "wb") as f:
        dump(obj, f)


def cargar_modelo(root, screen):
    root.filename = filedialog.askopenfile(initialdir="modelos/")
    with open(root.filename.name, "rb") as f:
        unpicked_model = load(f)
    customtkinter.CTkButton(screen, text = "Mostrar Modelo e Imagen", 
                            command = lambda: makeAndShowGraph(unpicked_model, screen)).grid(row = 6, column = 6)