from flask import Blueprint

import controllers

master = Blueprint('master', __name__)

@master.route('/masters', methods=['GET'])
def get_masters():
    return controllers.get_masters()

@master.route('/masters/<int:master_id>', methods=['GET'])
def get_master_by_id(master_id):
    return controllers.get_master_by_id(master_id)

@master.route('/masters', methods=['POST'])
def add_master():
    return controllers.add_master()

@master.route('/masters/<int:master_id>', methods=['PUT'])
def update_master(master_id):
    return controllers.update_master(master_id)

@master.route('/masters/<int:master_id>', methods=['DELETE'])
def delete_master(master_id):
    return controllers.delete_master(master_id)