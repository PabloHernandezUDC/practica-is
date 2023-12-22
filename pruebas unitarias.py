import unittest
from unittest.mock import Mock

from prediction import makePrediction


class TestMakePrediction(unittest.TestCase):

    def test_makePrediction(self):
        # Mock del modelo y el marco
        model = Mock()
        frame = Mock()

        # Configurando comportamientos simulados para el modelo
        model.predict.return_value = 42.0
        model.get_slope.return_value = 2.5
        model.get_intercept.return_value = 10.0
        model.get_columnyName.return_value = 'Y'

        # Llamando a la función
        makePrediction(model, '5', frame)

        # Verificando llamadas a los métodos de Tkinter
        frame.grid.assert_any_call(row=2, column=0, columnspan=1)
        frame.grid.assert_any_call(row=1, column=4, columnspan=5)
        frame.grid.assert_any_call(row=2, column=2, columnspan=2)
        frame.grid.assert_any_call(row=2, column=4, columnspan=5)

if __name__ == '__main__':
    unittest.main()