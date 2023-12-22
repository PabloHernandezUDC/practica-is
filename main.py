from customtkinter import CTk
from guiOp import configure


if __name__ == '__main__':
    # CREAR LA VENTANA PRINCIPAL
    root = CTk()
    configure(root)

    # EJECUTAR EL BUCLE PRINCIPAL
    root.mainloop()