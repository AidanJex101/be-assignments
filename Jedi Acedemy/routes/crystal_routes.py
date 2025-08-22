from flask import Blueprint

import controllers

crystal = Blueprint('crystal', __name__)

@crystal.route('/crystals', methods=['GET'])
def get_crystals():
    return controllers.get_crystals()

@crystal.route('/crystals/<int:crystal_id>', methods=['GET'])
def get_crystal_by_id(crystal_id):
    return controllers.get_crystal_by_id(crystal_id)

@crystal.route('/crystals', methods=['POST'])
def add_crystal():
    return controllers.add_crystal()

@crystal.route('/crystals/<int:crystal_id>', methods=['PUT'])
def update_crystal(crystal_id):
    return controllers.update_crystal(crystal_id)

@crystal.route('/crystals/<int:crystal_id>', methods=['DELETE'])
def delete_crystal(crystal_id):
    return controllers.delete_crystal(crystal_id)