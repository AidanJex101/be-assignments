from flask import Blueprint

import controllers

PokemonBattle = Blueprint('PokemonBattle', __name__)

@PokemonBattle.route('/pokemon_battle', methods=['GET'])
def get_pokemon_battles():
    return controllers.get_all_pokemon_battles()

@PokemonBattle.route('/pokemon_battle/<int:pokemon_battle_id>', methods=['GET'])
def get_pokemon_battle(battle_id):
    return controllers.get_pokemon_battle_by_id(battle_id)

@PokemonBattle.route('/pokemon_battle', methods=['POST'])
def create_pokemon_battle():
    return controllers.add_pokemon_battle()

@PokemonBattle.route('/pokemon_battle/<int:pokemon_battle_id>', methods=['PUT'])
def update_pokemon_battle(battle_id):
    return controllers.update_pokemon_battle(battle_id)

@PokemonBattle.route('/pokemon_battle/<int:pokemon_battle_id>', methods=['DELETE'])
def delete_pokemon_battle(battle_id):
    return controllers.delete_pokemon_battle(battle_id)