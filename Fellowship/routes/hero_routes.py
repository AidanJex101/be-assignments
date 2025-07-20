from flask import Blueprint
import controllers

heros = Blueprint('heros', __name__)

@heros.route('/hero', methods=['POST'])
def add_hero():
    return controllers.add_hero()

@heros.route('/hero/<hero_id>', methods=['GET'])
def get_hero_by_id(hero_id):
    return controllers.get_hero_by_id(hero_id)

@heros.route('/hero/<hero_id>', methods=['PUT'])
def update_hero(hero_id):
    return controllers.update_hero_by_id(hero_id)

@heros.route('/hero/<hero_id>', methods=['DELETE'])
def delete_hero(hero_id):
    return controllers.delete_hero_by_id(hero_id)

@heros.route('/heros', methods=['GET'])
def get_all_heros():
    return controllers.get_all_heros()

