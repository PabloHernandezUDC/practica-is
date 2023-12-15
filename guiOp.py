import customtkinter
from tkinter import *
from dataOp import readFile 
from modelOp import loadModelFromPickleObject

def configure(root):
    """Configura la interfaz gráfica para la aplicación de regresión lineal.

    Parameters
    ----------
    root: Tk
        Raíz de la interfaz gráfica.
    """

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{screenWidth}x{screenHeight}")  # ajustar ventana al tamaño de la pantalla
    screenFrame = customtkinter.CTkScrollableFrame(root)
    screenFrame.pack(expand = True, fill = 'both')

    root.state('zoomed') # mostrar la ventana maximizada
    root.protocol('WM_DELETE_WINDOW', quit) # para cerrar bien la ventana cuando se presiona la x
    root.title("Regresión lineal")

    for i in range(11):
        screenFrame.grid_columnconfigure(i, weight = 1)

    for i in range(11):
        screenFrame.grid_rowconfigure(i, weight = 1)

    # CREAR LOS BOTONES
    chooseFileButton = customtkinter.CTkButton(screenFrame, text = "Elegir archivo", command = lambda: readFile(screenWidth, screenHeight, root, screenFrame)).grid(row = 1, column = 5, columnspan = 1)
    loadModelButton = customtkinter.CTkButton(screenFrame, text = "Cargar modelo", command = lambda: loadModelFromPickleObject(root, screenFrame, screenHeight, screenWidth)).grid(row = 2, column = 5, columnspan = 1)