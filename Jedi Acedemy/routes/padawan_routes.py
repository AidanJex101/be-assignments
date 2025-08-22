from flask import Blueprint

import controllers

padawan = Blueprint('padawan', __name__)

@padawan.route('/padawans', methods=['GET'])
def get_padawans():
    return controllers.get_padawans()

@padawan.route('/padawans/<int:padawan_id>', methods=['GET'])
def get_padawan_by_id(padawan_id):
    return controllers.get_padawan_by_id(padawan_id)

@padawan.route('/padawans', methods=['POST'])
def add_padawan():
    return controllers.add_padawan()

@padawan.route('/padawans/<int:padawan_id>', methods=['PUT'])
def update_padawan(padawan_id):
    return controllers.update_padawan(padawan_id)

@padawan.route('/padawans/<int:padawan_id>', methods=['DELETE'])
def delete_padawan(padawan_id):
    return controllers.delete_padawan(padawan_id)