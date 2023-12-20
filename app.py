from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from datetime import timedelta
# from dotenv import load_dotenv

from view.pokedex_view import HealthCkeckView,PokedexGeneralView, PokedexFilteredView

# load_dotenv()

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

cors = CORS(app)

api = Api(app)

# Endpoints
api.add_resource(PokedexGeneralView,'/pokedex')
api.add_resource(PokedexFilteredView,'/pokedex/filter')
api.add_resource(HealthCkeckView,'/pokedex/ping')

jwt = JWTManager(app)