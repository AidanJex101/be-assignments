from flask import Blueprint

import controllers

lightsaber = Blueprint('lightsaber', __name__)

@lightsaber.route('/lightsabers', methods=['GET'])
def get_lightsabers():
    return controllers.get_lightsabers()

@lightsaber.route('/lightsabers/<int:lightsaber_id>', methods=['GET'])
def get_lightsaber_by_id(lightsaber_id):
    return controllers.get_lightsaber_by_id(lightsaber_id)

@lightsaber.route('/lightsabers', methods=['POST'])
def add_lightsaber():
    return controllers.add_lightsaber()

@lightsaber.route('/lightsabers/<int:lightsaber_id>', methods=['PUT'])
def update_lightsaber(lightsaber_id):
    return controllers.update_lightsaber(lightsaber_id)

@lightsaber.route('/lightsabers/<int:lightsaber_id>', methods=['DELETE'])
def delete_lightsaber(lightsaber_id):
    return controllers.delete_lightsaber(lightsaber_id)