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

    def test_response_pokemon_exist(self):
        response = self.app.get('/pokedex',json={"id_nombre_pokemon":fake.name()})
        self.assertEqual(response.status_code, 404)

    # def test_response_auth_void_user_and_pwd(self):

    #     response = self.app.post('/users/auth',json={"usuario":"","contrasena":""})
    #     msg:dict = {
    #         "error 4040": "Falta informacion en la petición"
    #         }
    #     response_dict = json.loads(response.data)
    #     self.assertEqual(response_dict, msg)


    # def test_response_auth_unauthorized(self):

    #     response = self.app.post('/users/auth',json={"usuario":"123","contrasena":"123"})
    #     msg:dict = {
    #         "error 5050": "El usuario no pudo ser autenticado"
    #         }
    #     response_dict = json.loads(response.data)
    #     self.assertEqual(response_dict, msg)


if __name__ == '__main__':
    unittest.main()