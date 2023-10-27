from tkinter import *
from tkinter import PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as p
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from regresion import *
# Función para mostrar la imagen al hacer clic en el botón

# Crear una ventana principal
root = Tk()
root.title("Mostrar Imagen")
root.geometry("900x1000")

def mostrar(data):
    i = 0
    for c in data.columns:
        print(f'Columna número {i}: {c}')
        label = Label(root,text=f'Columna nº {i}: {c}').pack()
        i += 1
    
def leer():
    global data
    root.filename = filedialog.askopenfile(initialdir="/modelos")
    data = p.read_csv(root.filename)
    mostrar(data)

def mostrar_imagen():
    global entry1
    global entry2
    global imagen
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    regresionF(data,num1,num2)

    imagen = ImageTk.PhotoImage(Image.open("fig.png"))
    imagen1 = Label(image=imagen).place(x =150, y = 500)

# Crear un botón
buttonl = Button(root,text="leer archivo",command = leer).pack()

button = Button(root, text="Mostrar Imagen", command=mostrar_imagen)
button.pack()

entry1= Entry(root, width= 40)
entry1.focus_set()
entry1.place(x =330, y= 450)

entry2= Entry(root, width= 40)
entry2.focus_set()
entry2.place(x=330, y =480)
Button(root, text="Quit", command=root.destroy).pack()
# Ejecutar el bucle principal
root.mainloop()