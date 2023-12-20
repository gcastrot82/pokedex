from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from view.pokedex_view import HealthCkeckView,PokedexGeneralView, PokedexFilteredView

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

cors = CORS(app)

api = Api(app)

"""
Los siguientes son los recursos que se exponen para el consumo de la API.
Si se esta ejecutando de manera local se puede acceder desde :
Api General:
- http://localhost:5000/pokedex

Api especifico:
- http://localhost:5000/pokedex/filter

Estado de salud del servicio:
- http://localhost:5000/pokedex/ping

"""
api.add_resource(PokedexGeneralView,'/pokedex')
api.add_resource(PokedexFilteredView,'/pokedex/filter')
api.add_resource(HealthCkeckView,'/pokedex/ping')

jwt = JWTManager(app)