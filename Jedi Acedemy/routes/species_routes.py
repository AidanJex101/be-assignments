from flask import Blueprint

import controllers

species = Blueprint('species', __name__)

@species.route('/species', methods=['GET'])
def get_species():
    return controllers.get_species()

@species.route('/species/<int:species_id>', methods=['GET'])
def get_species_by_id(species_id):
    return controllers.get_species_by_id(species_id)

@species.route('/species', methods=['POST'])
def add_species():
    return controllers.add_species()

@species.route('/species/<int:species_id>', methods=['PUT'])
def update_species(species_id):
    return controllers.update_species(species_id)

@species.route('/species/<int:species_id>', methods=['DELETE'])
def delete_species(species_id):
    return controllers.delete_species(species_id)