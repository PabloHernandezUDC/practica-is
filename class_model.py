class Model():

    def __init__(self, intercept, slope, rsquare, columnx, columny):
        self.intercept = intercept
        self.slope = slope
        self.rsquare = rsquare
        self.columnx = columnx
        self.columny = columny

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

    def get_columnx(self):
        return self.columnx
    
    def set_columnx(self, columnx):
        self.columnx = columnx
    
    def get_columny(self):
        return self.columny 

    def set_columny(self, columny):
        self.columny = columny