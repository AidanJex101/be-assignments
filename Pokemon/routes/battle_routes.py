from flask import Blueprint

import controllers

battle = Blueprint('battle', __name__)

@battle.route('/battles', methods=['GET'])
def get_battles():
    return controllers.get_all_battles()

@battle.route('/battles/<int:battle_id>', methods=['GET'])
def get_battle(battle_id):
    return controllers.get_battle_by_id(battle_id)

@battle.route('/battles', methods=['POST'])
def create_battle():
    return controllers.add_battle()

@battle.route('/battles/<int:battle_id>', methods=['PUT'])
def update_battle(battle_id):
    return controllers.update_battle(battle_id)

@battle.route('/battles/<int:battle_id>', methods=['DELETE'])
def delete_battle(battle_id):
    return controllers.delete_battle(battle_id)