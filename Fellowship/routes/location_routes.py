from flask import Blueprint
import controllers

locations = Blueprint('locations', __name__)

@locations.route('/location', methods=['POST'])
def add_location():
    return controllers.add_location()

@locations.route('/location/<location_id>', methods=['GET'])
def get_location_by_id(location_id):
    return controllers.get_location_by_id(location_id)

@locations.route('/location/<location_id>', methods=['PUT'])
def update_location(location_id):
    return controllers.update_location_by_id(location_id)

@locations.route('/location/<location_id>', methods=['DELETE'])
def delete_location(location_id):
    return controllers.delete_location_by_id(location_id)

