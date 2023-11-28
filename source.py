# librerías a instalar:
# numpy
# pandas
# openpyxl
# matplotlib
# scikit-learn
# statsmodels
# tkinter
# customtkinter

# cosas útiles:
# -> cómo hacer la regresión lineal y mostrarla:
#   -> https://realpython.com/linear-regression-in-python/
#   -> https://medium.com/analytics-vidhya/simple-linear-regression-with-example-using-numpy-e7b984f0d15e
# -> documentación de plot(): https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html


import time
import pandas as p
import numpy as np
import customtkinter
import tkinter
import class_model
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from tkinter import *
from tkinter import PhotoImage
from tkinter import simpledialog, filedialog
from PIL import Image, ImageTk
from leerBD import createDB, readRows, readOrdered,leer_sql
import class_model
from pickle import dump, dumps, load, loads
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




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
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-r') # formato = '[marker][line][color]'


def regression(d, i, j):
    plt.clf() # limpiamos la gráfica para no sobreescribir o pisar la anterior
    selectedColumns = d.iloc[:, [i, j]]

    x = np.array(selectedColumns.iloc[:, 0]).reshape((-1, 1)) # este es una columna con muchas filas
    y = np.array(selectedColumns.iloc[:, 1])                  # este es una fila con muchas columnas
    #np.set_printoptions(threshold=np.inf)

    model = LinearRegression().fit(x, y)

    intercept = model.intercept_ # término independiente
    slope = model.coef_[0] 
    r_sq = round(model.score(x, y), 2)
    meanSquaredError = np.mean((model.predict(x) - y)**2)
    meanSquaredError = round(meanSquaredError, 2)
    
    modelo_obj = class_model.Model(intercept, slope, r_sq, meanSquaredError, selectedColumns, x, y, root.filename.name, None)
    return modelo_obj


def guardar_modelo(obj):
    description= simpledialog.askstring("Input", "Añade una descripción al modelo:")
    obj.set_description(description)
    file_name = filedialog.asksaveasfilename(defaultextension=".pickle", filetypes=[("Pickle files", "*.pickle")])
    # Serializar el objeto y guardarlo en el archivo
    with open(file_name, "wb") as f:
        dump(obj, f)



def deserialize(name_file):
    with open(str(name_file), "rb") as f:
        unpicked_model = load(f)
    return unpicked_model


def extractDataFromFile(route):
    '''
    Esta función se ocupa de sacar los datos según el tipo de archivo, que se deduce de la extensión
    '''
    validExtensions = ('.csv', '.xlsx', '.db')
    route = str(route)
            
    if route.endswith(validExtensions) is False:
        print(f'El archivo en la ruta {route} no es válido.')
        data = None
    else:
        if route.endswith('.csv'):
            data = p.read_csv(route)
        elif route.endswith('.xlsx'):
            data = p.read_excel(route)
        elif route.endswith('.db'):
            data = leer_sql(route) 
    return data


def getColumns(data):
    l =  []
    for columna in data.columns:
        k = data[columna].dtype
        if k != 'object':
            l.append(columna)
        else:
            pass
    return l


def createColumns(data):
    scrollx = customtkinter.CTkScrollableFrame(screen,orientation="horizontal",height=30,width=800)
    scrolly = customtkinter.CTkScrollableFrame(screen,orientation="horizontal",height=30,width=800)
    scrollx.grid(row=4,column=1,sticky=W)
    scrolly.grid(row=6,column=1,sticky=W)
    global v1
    global v2
    v1 = IntVar()
    v2 = IntVar()
    i = 0
    customtkinter.CTkLabel(screen,text="X:").grid(row=4,column=0)
    customtkinter.CTkLabel(screen,text="Y:").grid(row=6,column=0)
    
    for col in getColumns(data):
        scrollx.grid_columnconfigure(i,weight=1)
        scrolly.grid_columnconfigure(i,weight=1)
        i+=1
    i = 0
    for col in getColumns(data):
        
        customtkinter.CTkRadioButton(scrollx, variable = v1, value = i, text = col).grid(row = 0, column = 1+i,sticky=W)
        customtkinter.CTkRadioButton(scrolly, variable = v2, value = i, text = col).grid(row = 0, column = 1+i,sticky=W)
        i += 1
    customtkinter.CTkButton(screen, text = "Crear modelo y mostrar Imagen", command = makeAndShowGraph).grid(row = 5, column = 7)


def leer():
    global data, width, height
    root.filename = filedialog.askopenfile(initialdir="modelos/")
    data = extractDataFromFile(root.filename.name)
    
    # MOSTRAR LOS DATOS EN UNA TABLA
    dataTable = customtkinter.CTkScrollableFrame(master=screen,
                                                 width=width*0.75,
                                                 height=height*0.14,
                                                 corner_radius=10,
                                                 orientation='horizontal')

    printableData = data.select_dtypes(include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).head()
    
    for i in range(len(printableData.columns)):        
        customtkinter.CTkLabel(dataTable,
                               text = printableData.columns[i] + '\n' + printableData.iloc[:, i].to_string(index=False),
                               justify='right',
                               font=(None, 20) # le ponemos None a la fuente para que ponga la "por defecto"
                               ).grid(row=0, column=i, padx=10, sticky=W)
    dataTable.grid(row = 3, column = 0, columnspan = 20)
    
    createColumns(data)
    filepath.configure(text = f"{root.filename.name}")


def makeAndShowGraph():
    #top= Toplevel(root)
    #top.geometry("800x600")
    #top.title("Graph Display")
    global data
    global root 
    num1, num2 = int(v1.get()), int(v2.get())

    model = regression(data, num1, num2)

    x, y = model.get_columnx(), model.get_columny()
    selectedColumns = model.get_selectedColumns()

    fig, ax = plt.subplots()
    ax.plot(x, y, '.k')
    ax.set_ylabel(selectedColumns.columns[1])
    ax.set_xlabel(selectedColumns.columns[0])
    abline(model.get_slope(), model.get_intercept())
    eq = f'{round(model.get_slope(), 2)}x ' + ('+' if model.get_intercept() > 0 else '-') + f' {round(abs(model.get_intercept()), 2)}'
    ax.set_title(f'{eq} / R²: {model.get_rsquare()} / MSE: {model.get_mse()}')
    ax.grid()

    canvas = FigureCanvasTkAgg(fig, screen)
    canvas.draw()
    canvas.get_tk_widget().grid(row = 10, column = 0, columnspan = 8)

    filename = 'fig.png'
    plt.savefig(filename) # para guardarlo en un archivo

    customtkinter.CTkButton(screen, text = "Guardar modelo", command = lambda: guardar_modelo(model)).grid(row = 10, column = 9)
    
    #imagen = customtkinter.CTkImage(light_image = Image.open(filename), size=(640, 480))
    #imageLabel = customtkinter.CTkLabel(top, image = imagen)
    #imageLabel.grid(row = 20, column = 0, columnspan = 10)
    #imageLabel.pack()
    #imageLabel.image = imagen
    #top.mainloop()
    #top.attributes('-topmost', True)


if __name__ == '__main__':

    # CREAR LA VENTANA PRINCIPAL
    root = customtkinter.CTk()
    screen = customtkinter.CTkScrollableFrame(root)
    screen.pack(expand=True, fill='both')
    # Obtener el ancho y alto de la pantalla
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

# Definir el tamaño de la ventana
    root.geometry(f"{width}x{height}")  # Ajustar ventana al tamaño de la pantalla

# Mostrar la ventana maximizada
    root.state('zoomed')

    #root.attributes('-fullscreen',True)
    root.protocol('WM_DELETE_WINDOW', quit) # para cerrar bien la ventana cuando se presiona la x
    root.title("Regresión lineal")
    for i in range(12):
        screen.grid_columnconfigure(i, weight = 1)
    for i in range(11):
        screen.grid_rowconfigure(i, weight = 1)
    screen.grid_rowconfigure(10, weight = 50)
    
    # width, height = 1920, 1080
    # root.geometry(str(width) + 'x' + str(height))
    
    # CREAR LOS BOTONES
    chooseButton = customtkinter.CTkButton(screen, text = "Elegir archivo", command = leer).grid(row = 1, column = 10, columnspan=2)
    #showButton = customtkinter.CTkButton(root, text = "Crear modelo y mostrar Imagen", command = makeAndShowGraph).grid(row = 2, column = 4,columnspan=2)
    #quitButton = customtkinter.CTkButton(root, text = "Quit", command = quit).grid(row = 3, column = 4,columnspan=2)


    filepath = customtkinter.CTkLabel(screen, text="Ruta:", wraplength = width*0.9)
    filepath.grid(row = 1, column = 0, columnspan = 1)

    frame = tkinter.Frame(screen, width = width, borderwidth=2, relief="solid")
    frame.grid(row=1, column=1, columnspan=10, padx=10, pady=10)
    
    # CREAR UNA ETIQUETA PARA MOSTRAR LA RUTA DEL ARCHIVO
    filepath = customtkinter.CTkLabel(frame, text="", wraplength = width*0.9)
    filepath.pack()
    
    # EJECUTAR EL BUCLE PRINCIPAL
    root.mainloop()