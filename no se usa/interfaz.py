from tkinter import *
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as p
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from source import regression, extractDataFromFile

#Función para mostrar la imagen al hacer clic en el botón
#Crear una ventana principal
root = Tk()
root.title("Regresión lineal")
width, height = 800, 600
root.geometry(str(width) + 'x' + str(height))

def mostrarColumnas(data):
    i = 0
    for c in data.columns:
        print(f'Columna nº {i}: {c}')
        label = Label(root, text=f'Columna nº {i}: {c}').pack()
        i += 1

def leer():
    root.filename = filedialog.askopenfile(initialdir="/modelos")
    data = extractDataFromFile(root.filename)
    mostrarColumnas(data)

def mostrar_imagen(data, entry1, entry2):
    num1, num2 = int(entry1.get()), int(entry2.get())
    regression(data, num1, num2)

    imagen = Label(image = ImageTk.PhotoImage(Image.open("fig.png"))).place(x = 150, y = 500)

#Crear un botón
buttonl = Button(root, text = "leer archivo", command = leer).pack()

button = Button(root, text = "Mostrar Imagen", command = mostrar_imagen)
button.pack()

entry1= Entry(root, width = 40)
entry1.focus_set()
entry1.place(x = 330, y = 450)

entry2= Entry(root, width = 40)
entry2.focus_set()
entry2.place(x = 330, y = 480)
Button(root, text = "Quit", command = root.destroy).pack()

#Ejecutar el bucle principal
root.mainloop()