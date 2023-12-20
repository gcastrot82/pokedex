from flask_restful import Resource
import requests
from flask import jsonify,request


def get_pokemon_data_by_name_or_id(pokemon):
    """
    Funcíon: get_pokemon_data_by_name_or_id(pokemon)
    Este middelware, comunica con la API de pokeapi, y se le envía el id o nombre del pokemon a consultar.
    La función valida:
    - Si el pokemon exite.
    - Si el servicio de pokeapi esta o no disponible.
    """
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


def get_pokemon_with_filtered_data(pokemon):

    """
    Funcíon: get_pokemon_with_filtered_data(pokemon)
    Este middelware, comunica con la API de pokeapi, y se le envía el id o nombre del pokemon a consultar.
    La función valida:
    - Si el pokemon exite.
    - Si el servicio de pokeapi esta o no disponible.
    - Retorna los siguientes atributos: abilities, idPokeDex, sprites, types
    """
        
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}'
        response = requests.get(url)
        dictPokeAttributes = {}
        if response.status_code == 200:
            datos_pokemon = response.json()
            dictPokeAttributes = {
                "abilities":datos_pokemon["abilities"],
                "idPokeDex":datos_pokemon["id"],
                "sprites":datos_pokemon["sprites"],
                "types":datos_pokemon["types"]
            }
            return jsonify(dictPokeAttributes)
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


class PokedexGeneralView(Resource):
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


class PokedexFilteredView(Resource):
    def get(self):
        try:
            pokemon_data = get_pokemon_with_filtered_data(request.json["id_nombre_pokemon"])
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