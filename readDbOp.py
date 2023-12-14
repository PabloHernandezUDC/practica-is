import sqlite3 as sql
import pandas as pd


def readSQL(dbName):
    """Lee datos desde una base de datos SQLite y devuelve un DataFrame de pandas.

    Parameters
    ----------
    dbName: str
        Nombre del archivo de la base de datos SQLite.

    Returns
    -------
    DataFrame: pandas.DataFrame
        DataFrame que contiene los datos extraídos de la base de datos.
    """

    SQLConnection = sql.connect(dbName)
    return pd.read_sql_query("SELECT * FROM california_housing_dataset", SQLConnection)


def createDB(dbName):
    """Crea una base de datos vacía.

    Parameters
    ----------
    dbName: str
        Nombre del archivo de la base de datos SQLite.
    """

    SQLConnection = sql.connect(dbName)
    SQLConnection.commit()
    SQLConnection.close()


def tableName(dbName):
    """Obtiene el nombre de la tabla de la base de datos.

    Parameters
    ----------
    dbName: str
        Nombre del archivo de la base de datos SQLite.

    Returns
    -------
    table: str
    Nombre de la tabla de la base de datos.
    """

    SQLConnection = sql.connect(dbName)
    
    cursor = SQLConnection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = cursor.fetchone()[0]

    SQLConnection.close()

    return table


def columnNames(dbName):
    """Imprime los nombres de las columnas de la tabla de la base de datos.

    Parameters
    ----------
    dbName: str
        Nombre del archivo de la base de datos SQLite.
    """

    table = tableName(dbName)
    SQLConnection = sql.connect(dbName)
    
    cursor = SQLConnection.cursor()
    cursor.execute(f"PRAGMA table_info({table});")
    columns = cursor.fetchall()

    for column in columns:
        print(column[1])

    SQLConnection.close()


def readRows(dbName):
    """Lee todas las filas de la tabla de la base de datos y las devuelve como una lista de tuplas.

    Parameters
    ----------
    dbName: str
        Nombre del archivo de la base de datos SQLite.

    Returns
    -------
    data: list
        Lista de tuplas que contienen los datos de las filas de la tabla.
    """

    table = tableName(dbName)
    SQLConnection = sql.connect(dbName)
    
    cursor = SQLConnection.cursor()
    cursor.execute("SELECT * FROM {}".format(table))
    data = cursor.fetchall() # crea una lista de tuplas con la info de la tabla
    
    SQLConnection.commit()
    SQLConnection.close()
    
    return data


def readOrdered(dbName, field):
    """Lee todas las filas de la tabla ordenadas por el campo especificado y las devuelve como una lista de tuplas.

    Parameters
    ----------
    dbName: str
        Nombre del archivo de la base de datos SQLite.
    field: str
        Campo por el que se ordenan las filas.
    
    Returns
    -------
    data: list
        Lista de tuplas que contienen los datos de las filas de la tabla, ordenados por el campo especificado.
    """

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