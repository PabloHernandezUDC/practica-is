import pandas as p
import customtkinter
import tkinter
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from leerBD import leer_sql
from model_op import makeModel

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
        if data[columna].dtype not in ('StringDtype', 'datetime64'): #Para descartar strings y fechas
            l.append(columna)
    return l


def createColumns(data, root, screen, height, width):
    #frameColumnas = customtkinter.CTkFrame(screen,width=width*0.9,height=height*0.20,corner_radius=10)
    frameColumnas = customtkinter.CTkFrame(screen, width=width*0.9, height=height*0.14)
    #frameColumnas.pack()  # Empaquetar el frame dentro de la ventana
    frameColumnas.grid(row = 5, column = 0, columnspan = 12)
    #frameColumnas.grid(column=0,row=7,columnspan=9)
    frameColumnas.grid_columnconfigure(0, minsize=100)
    customtkinter.CTkLabel(frameColumnas,text="X:").grid(row=0,column=0,sticky=E)
    customtkinter.CTkLabel(frameColumnas,text="Y:").grid(row=1,column=0,sticky=E)
    scrollx = customtkinter.CTkScrollableFrame(frameColumnas,orientation="horizontal",height=30,width=800)
    scrolly = customtkinter.CTkScrollableFrame(frameColumnas,orientation="horizontal",height=30,width=800)
    scrollx.grid(row=0,column=2,sticky=E)
    scrolly.grid(row=1,column=2,sticky=E)
    global v1
    global v2
    v1 = IntVar()
    v2 = IntVar()
    
    i = 0 
    for col in getColumns(data):
        scrollx.grid_columnconfigure(i, weight = 1)
        scrolly.grid_columnconfigure(i, weight = 1)
        i += 1
    
    i = 0
    for col in getColumns(data):
        
        customtkinter.CTkRadioButton(scrollx, variable = v1, value = i, text = col).grid(row = 0, column = 1+i, sticky = W)
        customtkinter.CTkRadioButton(scrolly, variable = v2, value = i, text = col).grid(row = 0, column = 1+i, sticky = W)
        i += 1
    frameColumnas.grid_columnconfigure(3, minsize=width*0.2) 
    customtkinter.CTkButton(frameColumnas, text = "Crear modelo y mostrar Imagen", command = lambda: makeModel(data, root, screen, height, width, v1, v2)).grid(row=0,column=3,rowspan=2)


def leer(width, height, root, screen):
    root.filename = filedialog.askopenfile(initialdir = "modelos/")
    data = extractDataFromFile(root.filename.name)
    
    filepath = customtkinter.CTkLabel(screen, text="Ruta:", wraplength = width*0.9)
    filepath.grid(row = 1, column = 3, columnspan = 2)
    
    frame = tkinter.Frame(screen, width = width, borderwidth=2, relief="solid")
    frame.grid(row=1, column=1, columnspan=10, padx=10, pady=10)
    
    # CREAR UNA ETIQUETA PARA MOSTRAR LA RUTA DEL ARCHIVO
    filepath = customtkinter.CTkLabel(frame, text="", wraplength = width*0.9)
    filepath.pack()

    # MOSTRAR LOS DATOS EN UNA TABLA
    dataTable = customtkinter.CTkScrollableFrame(master = screen,
                                                 width = width*0.9,
                                                 height = height*0.14,
                                                 corner_radius = 10,
                                                 orientation = 'horizontal')


    printableData = data.select_dtypes(include = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).head()
    
    for i in range(len(printableData.columns)):        
        customtkinter.CTkLabel(dataTable,
                               text = printableData.columns[i] + '\n' + printableData.iloc[:, i].to_string(index=False),
                               justify='right',
                               font=(None, 20) # le ponemos None a la fuente para que ponga la "por defecto"
                               ).grid(row=0, column=i, padx=10, sticky=W)
        dataTable.grid_columnconfigure(i, weight=1)
    dataTable.grid(row = 3, column = 0, columnspan = 20)
    
    createColumns(data, root, screen, height, width)
    filepath.configure(text = f"{root.filename.name}")