from flask import Blueprint

import controllers

spells = Blueprint('spells', __name__)

@spells.route('/spell', methods=['POST'])
def add_spell():
    return controllers.spells_controller.add_spell()

@spells.route('/spells', methods=['GET'])
def get_spells():
    return controllers.spells_controller.get_spells()

@spells.route('/spell/<difficulty>', methods=['GET'])
def get_spells_by_difficulty(difficulty):
    return controllers.spells_controller.get_spells_by_difficulty(difficulty)

@spells.route('/spell/<int:spell_id>', methods=['PUT'])
def update_spell(spell_id):
    return controllers.spells_controller.update_spell(spell_id)

@spells.route('/spell/delete/<int:spell_id>', methods=['DELETE'])
def delete_spell(spell_id):
    return controllers.spells_controller.delete_spell(spell_id)

