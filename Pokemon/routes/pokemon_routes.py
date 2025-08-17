from flask import Blueprint

import controllers

pokemon = Blueprint('pokemon', __name__)

@pokemon.route('/pokemon', methods=['GET'])
def get_pokemon():
    return controllers.get_all_pokemon()

@pokemon.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def get_pokemon_by_id(pokemon_id):
    return controllers.get_pokemon_by_id(pokemon_id)

@pokemon.route('/pokemon', methods=['POST'])
def create_pokemon():
    return controllers.add_pokemon()

@pokemon.route('/pokemon/<int:pokemon_id>', methods=['PUT'])
def update_pokemon(pokemon_id):
    return controllers.update_pokemon(pokemon_id)

@pokemon.route('/pokemon/<int:pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    return controllers.delete_pokemon(pokemon_id)