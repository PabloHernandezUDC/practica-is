import pandas as p
import customtkinter
import tkinter
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog
from leerBD import leer_sql
from model_op import makeModel

def extractDataFromFile(fileRoute):
    '''
    Esta función se ocupa de sacar los datos según el tipo de archivo, que se deduce de la extensión
    '''
    VALID_EXTENSIONS = ('.csv', '.xlsx', '.db')
    fileRoute = str(fileRoute)
            
    if fileRoute.endswith(VALID_EXTENSIONS) is False:
        print(f'El archivo en la ruta {fileRoute} no es válido.')
        data = None
    else:
        if fileRoute.endswith('.csv'):
            data = p.read_csv(fileRoute)
        elif fileRoute.endswith('.xlsx'):
            data = p.read_excel(fileRoute)
        elif fileRoute.endswith('.db'):
            data = leer_sql(fileRoute) 
    return data


def getColumns(data):
    validColumns =  []
    for column in data.columns:
        if data[column].dtype not in ('StringDtype', 'datetime64'): #Para descartar strings y fechas
            validColumns.append(column)
    return validColumns


def createColumns(data, root, screen, height, width):
    choosingVariablesFrame = customtkinter.CTkFrame(screen, width=width*0.9, height=height*0.14)
    choosingVariablesFrame.grid(row = 5, column = 0, columnspan = 12)
    choosingVariablesFrame.grid_columnconfigure(0, minsize=100)
    customtkinter.CTkLabel(choosingVariablesFrame,text="X:").grid(row=0,column=0,sticky=E)
    customtkinter.CTkLabel(choosingVariablesFrame,text="Y:").grid(row=1,column=0,sticky=E)
    xVariableScrollableFrame = customtkinter.CTkScrollableFrame(choosingVariablesFrame,orientation="horizontal",height=30,width=800)
    yVariableScrollableFrame = customtkinter.CTkScrollableFrame(choosingVariablesFrame,orientation="horizontal",height=30,width=800)
    xVariableScrollableFrame.grid(row=0,column=2,sticky=E)
    yVariableScrollableFrame.grid(row=1,column=2,sticky=E)
    global v1
    global v2
    v1 = IntVar()
    v2 = IntVar()
    
    i = 0 
    for column in getColumns(data):
        xVariableScrollableFrame.grid_columnconfigure(i, weight = 1)
        yVariableScrollableFrame.grid_columnconfigure(i, weight = 1)
        i += 1
    
    i = 0
    for column in getColumns(data): 
        customtkinter.CTkRadioButton(xVariableScrollableFrame, variable = v1, value = i, text = column).grid(row = 0, column = 1+i, sticky = W)
        customtkinter.CTkRadioButton(yVariableScrollableFrame, variable = v2, value = i, text = column).grid(row = 0, column = 1+i, sticky = W)
        i += 1
    choosingVariablesFrame.grid_columnconfigure(3, minsize=width*0.2) 
    customtkinter.CTkButton(choosingVariablesFrame, text = "Crear modelo y mostrar Imagen", command = lambda: makeModel(data, root, screen, height, width, v1, v2)).grid(row=0,column=3,rowspan=2)


def readFile(width, height, root, screen):
    root.filename = filedialog.askopenfile(initialdir = "modelos/")
    data = extractDataFromFile(root.filename.name)
    
    filePath = customtkinter.CTkLabel(screen, text="Ruta:", wraplength = width*0.9)
    filePath.grid(row = 1, column = 3, columnspan = 2)
    
    fileRouteFrame = tkinter.Frame(screen, width = width, borderwidth=2, relief="solid")
    fileRouteFrame.grid(row=1, column=1, columnspan=10, padx=10, pady=10)
    
    # CREAR UNA ETIQUETA PARA MOSTRAR LA RUTA DEL ARCHIVO
    filePath = customtkinter.CTkLabel(fileRouteFrame, text="", wraplength = width*0.9)
    filePath.pack()

    # MOSTRAR LOS DATOS EN UNA TABLA
    dataTableScrollableFrame = customtkinter.CTkScrollableFrame(master = screen,
                                                 width = width*0.9,
                                                 height = height*0.14,
                                                 corner_radius = 10,
                                                 orientation = 'horizontal')


    numericData = data.select_dtypes(include = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).head()
    
    for i in range(len(numericData.columns)):        
        customtkinter.CTkLabel(dataTableScrollableFrame,
                               text = numericData.columns[i] + '\n' + numericData.iloc[:, i].to_string(index=False),
                               justify='right',
                               font=(None, 20) # le ponemos None a la fuente para que ponga la "por defecto"
                               ).grid(row=0, column=i, padx=10, sticky=W)
        dataTableScrollableFrame.grid_columnconfigure(i, weight=1)
    dataTableScrollableFrame.grid(row = 3, column = 0, columnspan = 20)
    
    createColumns(data, root, screen, height, width)
    filePath.configure(text = f"{root.filename.name}")