class Model():
    """Clase que representa un modelo de regresión lineal a partir de los parámetros proporcionados.

    Parámetros
    ----------
    intercept: int
        Término independiente
    slope: int
        Pendiente
    rsquare: int
        Coeficiente de determinación 
    mse: int
        Error cuadrado medio
    selectedColumns:
        Columnas seleccionadas del modelo
    columnx:
        Columna x de datos del modelo
    columnxName:
        Nombre de la columna x
    columny:
        Columna y de datos del modelo
    columnyName:
        Nombre de la columna y
    filepath:
        Ruta del archivo
    description:
        Descripción del modelo

    Métodos
    -------
    get_intercept(): Obtiene el valor del término independiente.
    set_intercept(intercept): Establece el valor del término independiente.
    get_slope(): Obtiene el valor de la pendiente.
    set_slope(slope): Establece el valor de la pendiente.
    get_rsquare(): Obtiene el valor del coeficiente de determinación.
    set_rsquare(rsquare): Establece el valor del coeficiente de determinación.
    get_mse(): Obtiene el valor del error cuadrado medio.
    set_mse(mse): Establece el valor del error cuadrado medio.
    get_selectedColumns(): Obtiene las columnas seleccionadas.
    set_selectedColumns(selectedColumns): Establece las columnas seleccionadas.
    get_columnx(): Obtiene el valor de la columna x.
    set_columnx(columnx): Establece el valor de la columna x.
    get_columnxName(): Obtiene el nombre de la columna x.
    set_columnxName(columnxName): Establece el nombre de la columna x.
    get_columny(): Obtiene el valor de la columna y.
    set_columny(columny): Establece el valor de la columna y.
    get_columnyName(): Obtiene el nombre de la columna y.
    set_columnyName(columnyName): Establece el nombre de la columna y.
    get_filepath(): Obtiene el valor de la ruta del archivo.
    set_filepath(filepath): Establece el valor de la ruta del archivo.
    get_description(): Obtiene la descripción del modelo.
    set_description(description): Establece la descripción del modelo.
    predict(inputValue) : Obtiene la predcción de y a partir de un valor de x.
    """

    def __init__(self, intercept, slope, rsquare, mse, selectedColumns, columnx, columnxName, columny, columnyName, filepath, description = None):
        self.intercept = intercept
        self.slope = slope
        self.rsquare = rsquare
        self.mse = mse
        self.selectedColumns = selectedColumns
        self.columnx = columnx
        self.columnxName = columnxName
        self.columny = columny
        self.columnyName = columnyName
        self.filepath = filepath
        self.description= description
    
    def get_intercept(self):
        return self.intercept
    
    def set_intercept(self, intercept):
        self.intercept = intercept

    def get_slope(self):
        return self.slope
    
    def set_slope(self, slope):
        self.slope = slope

    def get_rsquare(self):
        return self.rsquare
    
    def set_rsquare(self, rsquare):
        self.rsquare = rsquare
    
    def get_mse(self):
        return self.mse
    
    def set_mse(self, mse):
        self.mse = mse
    
    def get_selectedColumns(self):
        return self.selectedColumns
    
    def set_selectedColumns(self, selectedColumns):
        self.selectedColumns = selectedColumns

    def get_columnx(self):
        return self.columnx
    
    def set_columnx(self, columnx):
        self.columnx = columnx

    def get_columnxName(self):
        return self.columnxName
    
    def set_columnxName(self, columnxName):
        self.columnxName = columnxName

    def get_columny(self):
        return self.columny 

    def set_columny(self, columny):
        self.columny = columny

    def get_columnyName(self):
        return self.columnyName
    
    def set_columnyName(self, columnyName):
        self.columnyName = columnyName

    def get_filepath(self):
        return self.filepath
    
    def set_filepath(self, filepath):
        self.filepath = filepath

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
    
    def predict(self, inputValue):
        prediction = self.intercept + self.slope * inputValue
        return prediction