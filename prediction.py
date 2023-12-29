import customtkinter
from tkinter import *


def showPrediction(model, frame):
    """Genera la interfaz de usuario para realizar una predicción.

    Parameters
    ----------
    model: classModel.Model
        Objeto de la clase Model utilizado para realizar la predicción
    frame: customtkinter.CTkFrame
        Marco donde se mostrarán los elementos para realizar la predicción
    """

    try:
        xName = model.get_columnxName()

        xNameLabel = customtkinter.CTkLabel(frame, text = f"{xName}") 
        xNameLabel.grid(row = 1, column = 1, columnspan = 3, sticky = W)
        
        xEntryField = customtkinter.CTkEntry(frame)
        xEntryField.grid(row = 2, column = 1, columnspan = 1)

        predictButton = customtkinter.CTkButton(frame, text="Realizar Predicción", command = lambda: makePrediction(model, xEntryField.get(), frame))
        predictButton.grid(row = 3, column = 1, columnspan = 4)

        # Mostrar la predicción en la interfaz
        predictionsLabel1 = customtkinter.CTkLabel(frame, text=f"{round(model.get_slope(), 2)} *")
        predictionsLabel1.grid(row = 2, column = 0, columnspan = 1)
        
        yName = model.get_columnyName()
        yNameLabel = customtkinter.CTkLabel(frame, text = f"{yName}") 
        yNameLabel.grid(row = 1, column = 4, columnspan = 5)

        predictionsLabel2 = customtkinter.CTkLabel(frame, text = f"+ {round(model.get_intercept(), 2)}  =")
        predictionsLabel2.grid(row = 2, column = 2, columnspan = 2)

    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no válido
        customtkinter.CTkLabel(frame, text = "Error: Ingresa un valor numérico válido para x", 
                               foreground = "red").grid(row = 3, column = 2, columnspan = 8)


def makePrediction(model, xInput, frame):
    """Muestra el resultado de la predicción.

    Parameters
    ----------
    model: classModel.Model
        Objeto de la clase Model utilizado para realizar la predicción
    xInput: str
        Valor de entrada para la predicción
    frame: customtkinter.CTkFrame
        Marco donde se mostrarán los elementos para realizar la predicción
    """

    # Convertir el valor ingresado por el usuario a un número
    xInput = float(xInput)

    yPredicted = model.predict(xInput)

    # Mostrar la predicción en la interfaz
    predictionsLabel3 = customtkinter.CTkLabel(frame, text = f"{round(yPredicted, 2)}")
    predictionsLabel3.grid(row = 2, column = 4, columnspan = 5)


def createPredictionFrame(model, screen, height, width):
    """Crea un marco para la interfaz de usuario de predicción.

    Parameters
    ----------
    model: classModel.Model
        Objeto de la clase Model utilizado para realizar la predicción
    screen: customtkinter.CTkFrame
        Ventana principal de la interfaz
    height: int
        Altura de la pantalla
    width: int
        Ancho de la pantalla
    """

    predictionFrame = customtkinter.CTkFrame(screen, width = width*0.9, height = height*0.14)
    predictionFrame.grid(row = 11, columnspan = 30)
    predictionFrame.grid_rowconfigure(0, minsize = height*0.1)

    showPrediction(model, predictionFrame)