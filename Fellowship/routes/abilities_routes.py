from flask import Blueprint
import controllers

abilities = Blueprint('abilities', __name__)

@abilities.route('/ability', methods=['POST'])
def add_ability():
    return controllers.add_ability()

@abilities.route('/ability/<ability_id>', methods=['PUT'])
def update_ability(ability_id):
    return controllers.update_ability_by_id(ability_id)

@abilities.route('/ability/<ability_id>', methods=['DELETE'])
def delete_ability(ability_id):
    return controllers.delete_ability_by_id(ability_id)