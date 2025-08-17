from flask import Blueprint

import controllers

stats = Blueprint('stats', __name__)

@stats.route('/stats', methods=['GET'])
def get_stats():
    return controllers.get_all_stats()

@stats.route('/stats/<int:stat_id>', methods=['GET'])
def get_stat(stat_id):
    return controllers.get_stat_by_id(stat_id)

@stats.route('/stats', methods=['POST'])
def create_stat():
    return controllers.add_stat()

@stats.route('/stats/<int:stat_id>', methods=['PUT'])
def update_stat(stat_id):
    return controllers.update_stat(stat_id)

@stats.route('/stats/<int:stat_id>', methods=['DELETE'])
def delete_stat(stat_id):
    return controllers.delete_stat(stat_id)