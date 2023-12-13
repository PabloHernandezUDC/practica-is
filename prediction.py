import customtkinter
from tkinter import *


def realizar_prediccion(model, frame):

    try:
        namex = model.get_columnx_name()

        x_name = customtkinter.CTkLabel(frame, text = f"{namex}") 
        x_name.grid(row = 1, column = 1, columnspan = 3, sticky = W)
        x_entry = customtkinter.CTkEntry(frame)
        x_entry.grid(row = 2, column = 1, columnspan = 1)

        pred_button = customtkinter.CTkButton(frame, text="Realizar Predicción", command=lambda: showPrediction(model, x_entry.get(), frame))
        pred_button.grid(row = 3, column = 1, columnspan = 4)

    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no válido
        customtkinter.CTkLabel(frame, text = "Error: Ingresa un valor numérico válido para x", 
                               foreground = "red").grid(row = 3, column = 2, columnspan = 8)


def showPrediction(model, x_user, frame):
        # Convertir el valor ingresado por el usuario a un número
        x_user = float(x_user)

        y_predicho = model.predict(x_user)

        # Mostrar la predicción en la interfaz
        predicciones_label1 = customtkinter.CTkLabel(frame, text=f"{round(model.get_slope(), 2)} *")
        predicciones_label1.grid(row = 2, column = 0, columnspan = 1)
        
        namey = model.get_columny_name()
        y_name = customtkinter.CTkLabel(frame, text = f"{namey}") 
        y_name.grid(row = 1, column = 4, columnspan = 5)

        predicciones_label2 = customtkinter.CTkLabel(frame, text = f"+ {round(model.get_intercept(), 2)}  =")
        predicciones_label2.grid(row = 2, column = 2, columnspan = 2)

        predicciones_label3 = customtkinter.CTkLabel(frame, text = f"{round(y_predicho, 2)}")
        predicciones_label3.grid(row = 2, column = 4, columnspan = 5)

def predcitionFrame(model, screen, height, width):
    framePrediction = customtkinter.CTkFrame(screen, width=width*0.9, height=height*0.14)
    #frameColumnas.pack()  # Empaquetar el frame dentro de la ventana
    framePrediction.grid(row = 11, columnspan = 30)
    #frameColumnas.grid(column=0,row=7,columnspan=9)
    framePrediction.grid_rowconfigure(0, minsize=height*0.1)

    realizar_prediccion(model, framePrediction)