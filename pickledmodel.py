from pickle import dump, dumps, load, loads #Librería más eficiente,
import class_model

#Se ajusta mejor a las necesidades del lenguaje  que los formatos comunes a todos los lenguajes: XML y JSON
#Esta librería utiliza siempre que es posible _pickle (renombrado de cPickle), implementado en C, porque es más eficiente

#Serializamos con los comandos dumps() y se recupera el objeto a partir de la secuencia de bytes con loads()


obj_prueba=class_model.Model(1,2,3,4,5,6,7,8) #Creamos un objeto de nuestra clase modelo.

#dump y load, serializan y escriben o leen en un archivo determinado
# with open("pickled_obj","wb") as f:
#     dump(obj_prueba, f)

# with  open("pickled_obj","rb") as f:
#     unpicked_obj_prueba=load(f)
# print(unpicked_obj_prueba)
from tkinter import filedialog

# def serialize(obj, name_file):
#     with open(str(name_file), "wb") as f:
#         dump(obj, f)

#import os

def serialize(obj):
    # folder_path = filedialog.askdirectory()

    # # Si el usuario no selecciona ninguna carpeta, no hacer nada
    # if not folder_path:
    #     return

    # Nombre del archivo
    #file_name = "datos_serializados.pickle"

    # Crear la ruta completa para el archivo
    #file_path = os.path.join(folder_path, file_name)

    file_name = filedialog.asksaveasfilename(defaultextension=".pickle", filetypes=[("Pickle files", "*.pickle")])

    # Serializar el objeto y guardarlo en el archivo
    with open(file_name, "wb") as f:
        dump(obj, f)



serialize(obj_prueba)

