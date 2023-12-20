import unittest, json
from faker import Faker
from app import app

fake = Faker()
class TestApp(unittest.TestCase):
    def setUp(self):       
        self.app = app.test_client()
    
    def test_response_healthcheck_status_200(self):
        response = self.app.get('/pokedex/ping')
        self.assertEqual(response.status_code, 200)

    def test_response_without_body(self):
        response = self.app.get('/pokedex')
        msg:dict = {
            "mensaje":"Se requiere el nombre del pokemon (id_nombre_pokemon) en el body de la petición"
            }
        response_dict = json.loads(response.data)
        self.assertEqual(response_dict, msg)

    def test_response_pokemon_exist(self):
        response = self.app.get('/pokedex',json={"id_nombre_pokemon":"pikachu"})
        self.assertEqual(response.status_code, 200)

    def test_response_pokemon_not_exist(self):
        response = self.app.get('/pokedex',json={"id_nombre_pokemon":fake.name()})
        self.assertEqual(response.status_code, 404)


    def test_response_without_body_with_filtred_pokemon(self):
        response = self.app.get('/pokedex/filter')
        msg:dict = {
            "mensaje":"Se requiere el nombre del pokemon (id_nombre_pokemon) en el body de la petición"
            }
        response_dict = json.loads(response.data)
        self.assertEqual(response_dict, msg)

    def test_response_pokemon_exist_with_filtred_pokemon(self):
        response = self.app.get('/pokedex/filter',json={"id_nombre_pokemon":"pikachu"})
        self.assertEqual(response.status_code, 200)


    def test_response_filtred_pokemon_not_exist(self):
        response = self.app.get('/pokedex/filter',json={"id_nombre_pokemon":fake.name()})
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()