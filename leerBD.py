import sqlite3 as sql
import pandas as pd



def leer_sql(nombre):

    cnx = sql.connect(nombre)
    df = pd.read_sql_query("SELECT * FROM california_housing_dataset", cnx)
    return df

def createDB(nombre_db):
    conexion = sql.connect(nombre_db)
    
    conexion.commit()
    conexion.close()

def nombre_tabla(nombre_db):
    conexion = sql.connect(nombre_db)
    cursor = conexion.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabla = cursor.fetchone()[0]

    conexion.close()

    return tabla

def nombre_columnas(nombre_db):
    tabla = nombre_tabla(nombre_db)

    conexion = sql.connect(nombre_db)
    cursor = conexion.cursor()

    cursor.execute(f"PRAGMA table_info({tabla});")

    columnas = cursor.fetchall()

    for columna in columnas:
        print(columna[1])

    conexion.close()

def readRows(nombre_db):
    conexion = sql.connect(nombre_db)
    cursor = conexion.cursor()

    tabla = nombre_tabla(nombre_db)

    instruccion = "SELECT * FROM {}".format(tabla)
    cursor.execute(instruccion)
    
    datos = cursor.fetchall() #crea una lista de tuplas con la info de la tabla
    
    conexion.commit()
    conexion.close()
    
    #for fila in datos:
        #print(fila)
    return datos

def readOrdered(nombre_db, field):
    conexion = sql.connect(nombre_db)
    cursor = conexion.cursor()

    tabla = nombre_tabla(nombre_db)

    instruccion = "SELECT * FROM {} ORDER BY {}".format(tabla, field)
    cursor.execute(instruccion)
    
    datos = cursor.fetchall() #crea una lista de tuplas con la info de la tabla
    
    conexion.commit()
    conexion.close()
    
    #for fila in datos:
    #    print(fila)
    return datos

if __name__ == '__main__':
    nombre = "modelos/housing.db"
    col = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value', 'ocean_proximity']
    tabla = 'california_housing_dataset'
   
 
    #readOrdered(nombre, col, tabla, 'longitude')