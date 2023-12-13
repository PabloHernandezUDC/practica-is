import customtkinter
from tkinter import *
from data_op import leer 
from model_op import cargar_modelo

def configurar(root):
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry(f"{width}x{height}")  # Ajustar ventana al tamaño de la pantalla
    screen = customtkinter.CTkScrollableFrame(root)
    screen.pack(expand=True, fill='both')

# Mostrar la ventana maximizada
    root.state('zoomed')

    root.protocol('WM_DELETE_WINDOW', quit) # para cerrar bien la ventana cuando se presiona la x
    root.title("Regresión lineal")
    for i in range(11):
        screen.grid_columnconfigure(i, weight = 1)
    for i in range(11):
        screen.grid_rowconfigure(i, weight = 1)
    #screen.grid_rowconfigure(10, weight = 50)

    # CREAR LOS BOTONES
    chooseButton = customtkinter.CTkButton(screen, text = "Elegir archivo", command = lambda: leer(width, height, root, screen)).grid(row = 1, column = 5, columnspan=1)
    loadButton = customtkinter.CTkButton(screen, text = "Cargar modelo", command = lambda: cargar_modelo(root, screen)).grid(row = 2, column = 5, columnspan=1)