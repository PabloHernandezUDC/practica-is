import sqlite3 as sql
import pandas as pd

def readSQL(dbName):
    SQLConnection = sql.connect(dbName)
    return pd.read_sql_query("SELECT * FROM california_housing_dataset", SQLConnection)

def createDB(dbName):
    SQLConnection = sql.connect(dbName)
    SQLConnection.commit()
    SQLConnection.close()

def tableName(dbName):
    SQLConnection = sql.connect(dbName)
    
    cursor = SQLConnection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchone()[0]

    SQLConnection.close()

    return table

def columnNames(dbName):
    table = tableName(dbName)
    SQLConnection = sql.connect(dbName)
    
    cursor = SQLConnection.cursor()
    cursor.execute(f"PRAGMA table_info({table});")
    columns = cursor.fetchall()

    for column in columns:
        print(column[1])

    SQLConnection.close()

def readRows(dbName):
    table = tableName(dbName)
    SQLConnection = sql.connect(dbName)
    
    cursor = SQLConnection.cursor()
    cursor.execute("SELECT * FROM {}".format(table))
    data = cursor.fetchall() # crea una lista de tuplas con la info de la tabla
    
    SQLConnection.commit()
    SQLConnection.close()
    
    return data

def readOrdered(dbName, field):
    SQLConnection = sql.connect(dbName)
    cursor = SQLConnection.cursor()

    table = tableName(dbName)

    cursor.execute("SELECT * FROM {} ORDER BY {}".format(table, field))
    
    data = cursor.fetchall() # crea una lista de tuplas con la info de la tabla
    
    SQLConnection.commit()
    SQLConnection.close()
    
    return data

if __name__ == '__main__':
    name = "modelos/housing.db"
    columns = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value', 'ocean_proximity']
    table = 'california_housing_dataset'