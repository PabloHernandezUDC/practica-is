from pickle import dump, dumps, load, loads # Librería más eficiente,
from tkinter import filedialog
import class_model

# Se ajusta mejor a las necesidades del lenguaje  que los formatos comunes a todos los lenguajes: XML y JSON
# Esta librería utiliza siempre que es posible _pickle (renombrado de cPickle), implementado en C, porque es más eficiente

obj_prueba=class_model.Model(1,2,3,4,5,6,7,8) # Creamos un objeto de nuestra clase modelo.

def serialize(obj):

    file_name = filedialog.asksaveasfilename(defaultextension=".pickle", filetypes=[("Pickle files", "*.pickle")])

    # Serializar el objeto y guardarlo en el archivo
    with open(file_name, "wb") as f:
        dump(obj, f)

serialize(obj_prueba)