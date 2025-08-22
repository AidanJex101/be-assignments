from flask import Blueprint

import controllers

temple = Blueprint('temple', __name__)

@temple.route('/temples', methods=['GET'])
def get_temples():
    return controllers.get_temples()

@temple.route('/temples/<int:temple_id>', methods=['GET'])
def get_temple_by_id(temple_id):
    return controllers.get_temple_by_id(temple_id)

@temple.route('/temples', methods=['POST'])
def add_temple():
    return controllers.add_temple()

@temple.route('/temples/<int:temple_id>', methods=['PUT'])
def update_temple(temple_id):
    return controllers.update_temple(temple_id)

@temple.route('/temples/<int:temple_id>', methods=['DELETE'])
def delete_temple(temple_id):
    return controllers.delete_temple(temple_id)