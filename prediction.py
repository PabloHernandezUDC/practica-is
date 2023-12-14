import customtkinter
from tkinter import *

def makePrediction(model, frame):
    try:
        xName = model.get_columnxName()

        xNameLabel = customtkinter.CTkLabel(frame, text = f"{xName}") 
        xNameLabel.grid(row = 1, column = 1, columnspan = 3, sticky = W)
        
        xEntryField = customtkinter.CTkEntry(frame)
        xEntryField.grid(row = 2, column = 1, columnspan = 1)

        predictButton = customtkinter.CTkButton(frame, text="Realizar Predicción", command=lambda: showPrediction(model, xEntryField.get(), frame))
        predictButton.grid(row = 3, column = 1, columnspan = 4)

    except ValueError:
        # Manejar el caso en que el usuario ingrese un valor no válido
        customtkinter.CTkLabel(frame, text = "Error: Ingresa un valor numérico válido para x", 
                               foreground = "red").grid(row = 3, column = 2, columnspan = 8)


def showPrediction(model, xInput, frame):
        # Convertir el valor ingresado por el usuario a un número
        xInput = float(xInput)

        yPredicted = model.predict(xInput)

        # Mostrar la predicción en la interfaz
        predictionsLabel1 = customtkinter.CTkLabel(frame, text=f"{round(model.get_slope(), 2)} *")
        predictionsLabel1.grid(row = 2, column = 0, columnspan = 1)
        
        yName = model.get_columnyName()
        yNameLabel = customtkinter.CTkLabel(frame, text = f"{yName}") 
        yNameLabel.grid(row = 1, column = 4, columnspan = 5)

        predictionsLabel2 = customtkinter.CTkLabel(frame, text = f"+ {round(model.get_intercept(), 2)}  =")
        predictionsLabel2.grid(row = 2, column = 2, columnspan = 2)

        predictionsLabel3 = customtkinter.CTkLabel(frame, text = f"{round(yPredicted, 2)}")
        predictionsLabel3.grid(row = 2, column = 4, columnspan = 5)

def createPredictionFrame(model, screen, height, width):
    predictionFrame = customtkinter.CTkFrame(screen, width = width*0.9, height = height*0.14)
    predictionFrame.grid(row = 11, columnspan = 30)
    predictionFrame.grid_rowconfigure(0, minsize = height*0.1)

    makePrediction(model, predictionFrame)