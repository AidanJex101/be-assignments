from flask import Blueprint
import controllers

realms = Blueprint('realms', __name__)

@realms.route('/realm', methods=['POST'])
def add_realm():
    return controllers.add_realm()

@realms.route('/realm/<realm_id>', methods=['GET'])
def get_realm_by_id(realm_id):
    return controllers.get_realm_by_id(realm_id)

@realms.route('/realm/<realm_id>', methods=['PUT'])
def update_realm_by_id(realm_id):
    return controllers.update_realm_by_id(realm_id)

@realms.route('/realm/<realm_id>', methods=['DELETE'])
def delete_realm_by_id(realm_id):
    return controllers.delete_realm_by_id(realm_id)