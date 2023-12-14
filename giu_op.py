import customtkinter
from tkinter import *
from data_op import readFile 
from model_op import loadModelFromPickleObject

def configure(root):
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry(f"{screenWidth}x{screenHeight}")  # Ajustar ventana al tamaño de la pantalla
    screenFrame = customtkinter.CTkScrollableFrame(root)
    screenFrame.pack(expand=True, fill='both')

    # Mostrar la ventana maximizada
    root.state('zoomed')

    root.protocol('WM_DELETE_WINDOW', quit) # para cerrar bien la ventana cuando se presiona la x
    root.title("Regresión lineal")
    for i in range(11):
        screenFrame.grid_columnconfigure(i, weight = 1)
    for i in range(11):
        screenFrame.grid_rowconfigure(i, weight = 1)
    #screen.grid_rowconfigure(10, weight = 50)

    # CREAR LOS BOTONES
    chooseFileButton = customtkinter.CTkButton(screenFrame, text = "Elegir archivo", command = lambda: readFile(screenWidth, screenHeight, root, screenFrame)).grid(row = 1, column = 5, columnspan=1)
    loadModelButton = customtkinter.CTkButton(screenFrame, text = "Cargar modelo", command = lambda: loadModelFromPickleObject(root, screenFrame)).grid(row = 2, column = 5, columnspan=1)