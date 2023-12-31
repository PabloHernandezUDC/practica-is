import unittest
import pandas as pd
from io import StringIO
from unittest.mock import MagicMock, patch
from regression import SimpleLinearRegression
from classModel import Model


class TestSimpleLinearRegression(unittest.TestCase):

    def setUp(self):
        self.regression_instance = SimpleLinearRegression()

    def test_regression_with_valid_data(self):
        # Creamos datos de prueba
        data = pd.DataFrame({
            'X': [1, 2, 3, 4, 5],
            'Y': [2, 4, 5, 4, 5]
        })
        x_var = 0
        y_var = 1
        mock_root = MagicMock()

        # Ejecutamos la función de regresión
        result = self.regression_instance.regression(
            data, x_var, y_var, mock_root)

        # Comprobamos que la regresión devuelve un objeto de tipo Model
        self.assertIsInstance(result, Model)

        # Comprobamos algunos valores esperados
        self.assertAlmostEqual(result.intercept, 2.2, places=2)
        self.assertAlmostEqual(result.slope, 0.6, places=2)
        # Puedes agregar más comprobaciones según los datos de prueba que generes

    def test_regression_with_empty_dataframe(self):
        # Probamos cuando se pasa un DataFrame vacío
        data = pd.DataFrame()
        x_var = 0
        y_var = 1
        mock_root = MagicMock()

        # Verificamos que se levante un ValueError
        with self.assertRaises(ValueError):
            self.regression_instance.regression(data, x_var, y_var, mock_root)

    def test_regression_with_invalid_column_indices(self):
        # Probamos cuando se pasan índices de columna inválidos
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        x_var = 2
        y_var = 3
        mock_root = MagicMock()

        # Verificamos que se levante un IndexError
        with self.assertRaises(IndexError):
            self.regression_instance.regression(data, x_var, y_var, mock_root)


if __name__ == '__main__':
    unittest.main()
