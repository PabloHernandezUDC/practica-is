import customtkinter
from tkinter import *
from gui_op import configure

if __name__ == '__main__':
    # CREAR LA VENTANA PRINCIPAL
    root = customtkinter.CTk()
    configure(root)

    # EJECUTAR EL BUCLE PRINCIPAL
    root.mainloop()