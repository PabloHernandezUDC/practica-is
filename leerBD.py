import sqlite3 as sql

def createDB(nombre_db):
    conexion = sql.connect(nombre_db)
    
    conexion.commit()
    conexion.close()

def readRows(nombre_db, lista_columnas, nombre_tabla):
    conexion = sql.connect(nombre_db)
    cursor = conexion.cursor()

    columnas = ', '.join(lista_columnas)
    instruccion = "SELECT {} FROM {}".format(columnas, nombre_tabla)
    cursor.execute(instruccion)
    
    datos = cursor.fetchall() #crea una lista de tuplas con la info de la tabla
    
    conexion.commit()
    conexion.close()
    
    for fila in datos:
        print(fila)

def readOrdered(nombre_db, lista_columnas, nombre_tabla,  field):
    conexion = sql.connect(nombre_db)
    cursor = conexion.cursor()

    columnas = ', '.join(lista_columnas)
    instruccion = "SELECT {} FROM {} ORDER BY {}".format(columnas, nombre_tabla, field)
    cursor.execute(instruccion)
    
    datos = cursor.fetchall() #crea una lista de tuplas con la info de la tabla
    
    conexion.commit()
    conexion.close()
    
    for fila in datos:
        print(fila)

if __name__ == '__main__':

    nombre = 'housing.db'
    col = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value', 'ocean_proximity']
    tabla = 'california_housing_dataset'
   
    readRows(nombre, col, tabla)
    #readOrdered(nombre, col, tabla, 'longitude')