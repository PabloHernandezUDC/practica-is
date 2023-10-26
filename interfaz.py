#de momento solo es una ventana con un botón que outputea una imagen.
#Hay qye installar el tkinter y el Pillow para que vaya.
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("a")
window.geometry("900x900")

def output():
    image = Image.open("fig.png")
    photo = ImageTk.PhotoImage(image)
    label = Label(window, image=photo)
    label.image = photo
    label.place(x=100,y=100)
    

button = Button(window,text = "display", command=output)
button.pack()
window.mainloop()