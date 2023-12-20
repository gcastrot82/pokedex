from flask_restful import Resource
import requests
from flask import jsonify,request


def get_pokemon_data_by_name_or_id(pokemon):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}'
        response = requests.get(url)

        if response.status_code == 200:
            datos_pokemon = response.json()
            return jsonify(datos_pokemon)
        else:
            mensaje: dict = {
                "mensaje":"Pokemon no existe"
            }
            respuesta = jsonify(mensaje)
            respuesta.status_code = 404
            return respuesta
    except:
        mensaje: dict = {
                "mensaje":"Servicio no disponible"
            }
        respuesta = jsonify(mensaje)
        respuesta.status_code = 500
        return respuesta

class PokedexView(Resource):
    def get(self):
        try:
            pokemon_data = get_pokemon_data_by_name_or_id(request.json["id_nombre_pokemon"])
            return pokemon_data
        except:
            mensaje: dict = {
                "mensaje":"Se requiere el nombre del pokemon (id_nombre_pokemon) en el body de la petición"
            }
            respuesta = jsonify(mensaje)
            respuesta.status_code = 400
            return respuesta


class HealthCkeckView(Resource):
    def get(self):
        return "pong",200