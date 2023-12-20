from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from datetime import timedelta
# from dotenv import load_dotenv

from view.pokedex_view import HealthCkeckView,PokedexView
# from modelo import db

# load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pokedex.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
# app.config["JWT_ALGORITHM"] = "HS256"
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
app.config['PROPAGATE_EXEPTIONS'] = True

app_context = app.app_context()
app_context.push()

# db.init_app(app)
# db.create_all()

cors = CORS(app)

api = Api(app)

# Endpoints
# api.add_resource(PokedexView,'/pokedex/<pokeNameOrId>')
api.add_resource(PokedexView,'/pokedex')
api.add_resource(HealthCkeckView,'/pokedex/ping')

jwt = JWTManager(app)