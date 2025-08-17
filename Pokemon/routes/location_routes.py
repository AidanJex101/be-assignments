from flask import Blueprint

import controllers

location = Blueprint('location', __name__)

@location.route('/locations', methods=['GET'])
def get_locations():
    return controllers.get_all_locations()

@location.route('/locations/<int:location_id>', methods=['GET'])
def get_location(location_id):
    return controllers.get_location_by_id(location_id)

@location.route('/locations', methods=['POST'])
def create_location():
    return controllers.add_location()

@location.route('/locations/<int:location_id>', methods=['PUT'])
def update_location(location_id):
    return controllers.update_location(location_id)

@location.route('/locations/<int:location_id>', methods=['DELETE'])
def delete_location(location_id):
    return controllers.delete_location(location_id)