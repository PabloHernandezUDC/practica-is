from pickle import dump, dumps, load, loads #Librería más eficiente,
import class_model

#Se ajusta mejor a las necesidades del lenguaje  que los formatos comunes a todos los lenguajes: XML y JSON
#Esta librería utiliza siempre que es posible _pickle (renombrado de cPickle), implementado en C, porque es más eficiente

#Serializamos con los comandos dumps() y se recupera el objeto a partir de la secuencia de bytes con loads()


obj_prueba=class_model.Model(1,2,3,4,5) #Creamos un objeto de nuestra clase modelo.

#dump y load, serializan y escriben o leen en un archivo determinado
with open("pickled_obj","wb") as f:
    dump(obj_prueba, f)

with  open("pickled_obj","rb") as f:
    unpicked_obj_prueba=load(f)
print(unpicked_obj_prueba)