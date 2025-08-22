from flask import Blueprint

import controllers 

warranties = Blueprint('warranties', __name__)

@warranties.route('/warranty', methods=['POST'])
def create_warranty():
    return controllers.create_warranty()

@warranties.route('/warranty/<warranty_id>', methods=['GET'])
def get_warranty_by_id(warranty_id):
    return controllers.get_warranty_by_id(warranty_id)

@warranties.route('/warranties', methods=['GET'])
def get_all_warranties():
    return controllers.get_all_warranties()

@warranties.route('/warranty/<warranty_id>', methods=['PUT'])
def update_warranty_by_id(warranty_id):
    return controllers.update_warranty_by_id(warranty_id)

@warranties.route('/warranty/<warranty_id>', methods=['DELETE'])
def delete_warranty_by_id(warranty_id):
    return controllers.delete_warranty_by_id(warranty_id)