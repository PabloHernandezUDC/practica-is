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
    columnx:
        Columna x de datos del modelo
    columny:
        Columna y de datos del modelo
    filepath:
        Ruta del archivo

    Métodos
    -------
    get_interceipt(): Obtiene el valor del término independiente.
    set_interceipt(interceipt): Establece el valor del término independiente.
    get_slope(): Obtiene el valor de la pendiente.
    set_slope(slope): Establece el valor de la pendiente.
    get_rsquare(): Obtiene el valor del coeficiente de determinación.
    set_rsquare(rsquare): Establece el valor del coeficiente de determinación.
    get_columnx(): Obtiene el valor de la columna x.
    set_columnx(columnx): Establece el valor de la columna x.
    get_columny(): Obtiene el valor de la columna y.
    set_columny(columny): Establece el valor de la columna y.
    get_filepath(): Obtiene el valor de la ruta del archivo.
    set_filepath(filepath): Establece el valor de la ruta del archivo.
    """

    def __init__(self, intercept, slope, rsquare, mse, selectedColumns, columnx, columny, filepath):
        self.intercept = intercept
        self.slope = slope
        self.rsquare = rsquare
        self.mse = mse
        self.selectedColumns=selectedColumns
        self.columnx = columnx
        self.columny = columny
        self.filepath = filepath # para este parámetro habría que crear una variable en el código principal que llame a la ruta del archivo,
                                 # y luego al crear el modelo poner esa variable como este parámetro

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
    
    def get_columny(self):
        return self.columny 

    def set_columny(self, columny):
        self.columny = columny

    def get_filepath(self):
        return self.filepath
    
    def set_filepath(self, filepath):
        self.filepath = filepath

# Formas de mostrar el docstring
# help(Model)
# print(Model.__doc__)