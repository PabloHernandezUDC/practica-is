import customtkinter
from tkinter import *
from giu_op import configurar

if __name__ == '__main__':

    x = 20

    # CREAR LA VENTANA PRINCIPAL
    root = customtkinter.CTk()
    configurar(root)

    # EJECUTAR EL BUCLE PRINCIPAL
    root.mainloop()