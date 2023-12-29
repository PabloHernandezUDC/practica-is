import pandas

from tkinter import *
from tkinter import filedialog
from pickle import load
from customtkinter import CTkButton, CTkFrame, CTkLabel, CTkRadioButton, CTkScrollableFrame

from readDbOp import readSQL
from modelOp import makeModel, createPredictionFrame


def clearAndInitButtons(screen, height, width, root):
    '''Quita todos los widgets de la pantalla.

    Parameters
    ----------
    screen: customtkinter.CTkFrame
        Pantalla a limpiar

    Returns
    -------
    None
    '''
    
    for widgets in screen.winfo_children():
        widgets.destroy()
    
    chooseFileButton = CTkButton(screen,
                                               text = "Elegir archivo",
                                               command = lambda: obtainFileForRead(width,
                                                                          height,
                                                                          root,
                                                                          screen)).grid(row = 1,
                                                                                             column = 5)
    loadModelButton = CTkButton(screen,
                                              text = "Cargar modelo",
                                              command = lambda: obtainFileForLoad(root,
                                                                                screen,
                                                                                height,
                                                                                width)).grid(row = 1,
                                                                                                    column = 6)




def extractDataFromFile(fileRoute):
    """Saca los datos según el tipo de archivo, que se deduce de la extensión.

    Parameters
    ----------
    fileRoute: str
        Ruta del archivo a procesar

    Returns
    -------
    data: pandas.DataFrame or None
        DataFrame con los datos del archivo si éste es válido
    """
    
    validExtensions = ('.csv', '.xlsx', '.db')
    fileRoute = str(fileRoute)
            
    if fileRoute.endswith(validExtensions) is False:
        print(f'El archivo en la ruta {fileRoute} no es válido.')
        data = None
    else:
        if fileRoute.endswith('.csv'):
            data = pandas.read_csv(fileRoute)
        elif fileRoute.endswith('.xlsx'):
            data = pandas.read_excel(fileRoute)
        elif fileRoute.endswith('.db'):
            data = readSQL(fileRoute) 
    return data


def getColumns(data):
    """Obtiene las columnas válidas de un DataFrame.

    Parameters
    ----------
    data: pandas.DataFrame
        DataFrame del cual se extraen las columnas
    
    Returns
    -------
    validColumns: list
        Lista de nombres de las columnas válidas
    """

    validColumns =  []
    for column in data.columns:
        if data[column].dtype not in ('StringDtype', 'datetime64'): # para descartar strings y fechas
            validColumns.append(column)
    return validColumns


def createColumns(data, root, screen, height, width):
    """Crea las columnas x e y para seleccionar en la interfaz.

    Parameters
    ----------
    data: pandas.DataFrame
        DataFrame del cual se obtienen las columnas
    root: tkinter.Tk
        Raíz de la interfaz gráfica
    screen: customtkinter.CTkFrame
        Marco de la interfaz gráfica donde se mostrarán las columnas
    height: int
        Altura de la pantalla
    width: int
        Ancho de la pantalla
    """

    choosingVariablesFrame = CTkFrame(screen, width = width*0.9, height = height*0.14)
    choosingVariablesFrame.grid(row = 5, column = 0, columnspan = 12)
    choosingVariablesFrame.grid_columnconfigure(0, minsize = 100)

    CTkLabel(choosingVariablesFrame, text = "X:").grid(row = 0, column = 0, sticky = E)
    CTkLabel(choosingVariablesFrame, text = "Y:").grid(row = 1, column = 0, sticky = E)

    xVariableScrollableFrame = CTkScrollableFrame(choosingVariablesFrame, orientation = "horizontal", height = 30, width = 800)
    yVariableScrollableFrame = CTkScrollableFrame(choosingVariablesFrame, orientation = "horizontal", height = 30, width = 800)

    xVariableScrollableFrame.grid(row = 0, column = 2, sticky = E)
    yVariableScrollableFrame.grid(row = 1, column = 2, sticky = E)
    
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
        CTkRadioButton(xVariableScrollableFrame, variable = v1, value = i, text = column).grid(row = 0, column = 1+i, sticky = W)
        CTkRadioButton(yVariableScrollableFrame, variable = v2, value = i, text = column).grid(row = 0, column = 1+i, sticky = W)
        i += 1
    
    choosingVariablesFrame.grid_columnconfigure(3, minsize = width*0.2) 
    CTkButton(choosingVariablesFrame, text = "Crear modelo y mostrar Imagen", command = lambda: makeModel(data, root, screen, height, width, v1, v2)).grid(row = 0, column = 3, rowspan = 2)


def obtainFileForRead(width, height, root, screen):
    """Obtiene el nombre del archivo elegido por el usuario mediante una ventana de diálogo.
    
    Parameters
    ----------
    width: int
        Ancho de la pantalla
    height: int
        Altura de la pantalla
    root: tkinter.Tk
        Raíz de la interfaz gráfica
    screen: customtkinter.CTkFrame
        Marco de la interfaz gráfica donde se mostrará la información
    """

    tiposArchivo = [
    ("Archivos CSV", "*.csv"),
    ("Archivos de base de datos", "*.db"),
    ("Archivos Excel", "*.xlsx")
    ]
    root.filename = filedialog.askopenfile(initialdir = "modelos/", filetypes = tiposArchivo)
    file = root.filename.name

    readFile(width, height, root, screen, file)
    

def readFile(width, height, root, screen, name):
    """Lee un archivo y muestra la información en la interfaz gráfica.

    Parameters
    ----------
    width: int
        Ancho de la pantalla
    height: int
        Altura de la pantalla
    root: tkinter.Tk
        Raíz de la interfaz gráfica
    screen: customtkinter.CTkFrame
        Marco de la interfaz gráfica donde se mostrará la información
    name: str
        Nombre del archivo seleccionado
    """

    print(name)
    clearAndInitButtons(screen,height,width,root)
    
    data = extractDataFromFile(name)
    routeText = CTkLabel(screen, text="Ruta:")
    routeText.grid(row = 1, column = 3)
    
    # CREAR UNA ETIQUETA PARA MOSTRAR LA RUTA DEL ARCHIVO
    filePath = CTkLabel(screen, text = root.filename.name)
    filePath.grid(row = 1, column = 4)

    # MOSTRAR LOS DATOS EN UNA TABLA
    dataTableScrollableFrame = CTkScrollableFrame(master = screen,
                                                 width = width*0.9,
                                                 height = height*0.14,
                                                 corner_radius = 10,
                                                 orientation = 'horizontal')

    numericData = data.select_dtypes(include = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']).head()
    
    for i in range(len(numericData.columns)):        
        CTkLabel(dataTableScrollableFrame,
                               text = numericData.columns[i] + '\n' + numericData.iloc[:, i].to_string(index=False),
                               justify = 'right',
                               font = (None, 20) # le ponemos None a la fuente para que ponga la "por defecto"
                               ).grid(row = 0, column = i, padx = 10, sticky = W)
        dataTableScrollableFrame.grid_columnconfigure(i, weight = 1)
    dataTableScrollableFrame.grid(row = 3, column = 0, columnspan = 20)
    
    createColumns(data, root, screen, height, width)
    filePath.configure(text = f"{root.filename.name}")


def obtainFileForLoad(root, screen, height, width):
    """Obtiene el nombre del archivo elegido por el usuario mediante una ventana de diálogo.
    
    Parameters
    ----------
    root: tkinter.Tk
        Raíz de la interfaz gráfica
    screen: customtkinter.CTkFrame
        Marco de la interfaz gráfica donde se mostrará la información
    height: int
        Altura de la pantalla
    width: int
        Ancho de la pantalla
    """

    root.filename = filedialog.askopenfile(initialdir = "modelos/")
    file = root.filename.name
    
    loadModelFromPickleObject(root, screen, height, width, file)


def loadModelFromPickleObject(root, screen, height, width, name):
    """Carga un modelo serializado desde un archivo.

    Parameters
    ----------
    root: tkinter.Tk
        Raíz de la interfaz gráfica
    screen: customtkinter.CTkFrame
        Marco de la interfaz donde se mostrará el modelo y la imagen
    height: int
        Altura de la pantalla
    width: int
        Ancho de la pantalla
    name: str
        Nombre del archivo seleccionado
    """

    clearAndInitButtons(screen, height, width, root)

    with open(name, "rb") as f:
        unpickedModel = load(f)

    routeText = CTkLabel(screen, text="Ruta:")
    routeText.grid(row = 1, column = 3)
    
    # CREAR UNA ETIQUETA PARA MOSTRAR LA RUTA DEL ARCHIVO
    filePath = CTkLabel(screen, text = root.filename.name)
    filePath.grid(row = 1, column = 4)

    xName = unpickedModel.get_columnxName()
    yName = unpickedModel.get_columnyName()
    slope = unpickedModel.get_slope()
    intercept = unpickedModel.get_intercept()
    squareR = unpickedModel.get_rsquare()
    mse = unpickedModel.get_mse()

    modelFrame = CTkFrame(screen, width = width*0.9, height = height*0.14)
    modelFrame.grid(row = 4, columnspan = 30)
    modelFrame.grid_rowconfigure(0, minsize = height*0.1)

    xNameLabel = CTkLabel(modelFrame, text = f"x: {xName}")
    xNameLabel.grid(row = 1, column = 5)

    yNameLabel = CTkLabel(modelFrame, text = f"y: {yName}")
    yNameLabel.grid(row = 2, column = 5)

    equationLabel = CTkLabel(modelFrame, text = f"y = {round(slope, 2)} x + {round(intercept, 2)}") 
    equationLabel.grid(row = 3, column = 4, columnspan = 5)

    rSquareLabel = CTkLabel(modelFrame, text = f" R^2 : {squareR}   MSE : {mse}")
    rSquareLabel.grid(row = 4, column = 5)

    descriptionLabel = CTkLabel(modelFrame, text = f'Descripción: {unpickedModel.get_description()}')
    descriptionLabel.grid(row = 5, column = 5)

    createPredictionFrame(unpickedModel, screen, height, width)