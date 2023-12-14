import classModel
from tkinter import filedialog
from pickle import dump, dumps, load, loads 

# Librería más eficiente, se ajusta mejor a las necesidades del lenguaje  que los formatos comunes a todos los lenguajes: XML y JSON
# Esta librería utiliza siempre que es posible _pickle (renombrado de cPickle), implementado en C, porque es más eficiente

objPrueba = classModel.Model(1, 2, 3, 4, 5, 6, 7, 8) # creamos un objeto de nuestra clase modelo

def serialize(obj):

    fileName = filedialog.asksaveasfilename(defaultextension = ".pickle", filetypes = [("Pickle files", "*.pickle")])

    with open(fileName, "wb") as f: # serializar el objeto y guardarlo en el archivo
        dump(obj, f)

serialize(objPrueba)