import unittest
import os
from tempfile import NamedTemporaryFile
from pickle import dump, load
from modelOp import saveModelToPickleObject


class MockObject:
    def __init__(self):
        self.description = None

    def set_description(self, description):
        self.description = description


class TestSaveModelToPickleObject(unittest.TestCase):
    def setUp(self):
        # Crear un objeto para usar en las pruebas

        self.mock_obj = MockObject()
        self.model_description = "Este es un modelo de prueba"
        self.file_name = None

    def test_saveModelToPickleObject(self):
        # Crear un archivo temporal para la prueba
        with NamedTemporaryFile(delete=False) as temp_file:
            self.file_name = temp_file.name

        # Guardar el objeto en el archivo temporal
        saveModelToPickleObject(
            self.mock_obj, self.model_description, self.file_name)

        # Comprobar si el archivo se creó
        self.assertTrue(os.path.exists(self.file_name))

        # Cargar el objeto desde el archivo
        with open(self.file_name, "rb") as f:
            loaded_obj = load(f)

        # Comprobar si la descripción del objeto cargado es correcta
        self.assertEqual(loaded_obj.description, self.model_description)

    def tearDown(self):
        # Eliminar el archivo temporal creado durante la prueba
        if self.file_name and os.path.exists(self.file_name):
            os.remove(self.file_name)


if __name__ == '__main__':
    unittest.main()
