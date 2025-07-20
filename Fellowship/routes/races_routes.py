from flask import Blueprint
import controllers

races = Blueprint('races', __name__ )

@races.route('/race', methods=['POST'])
def add_race():
    return controllers.add_race()

@races.route('/race/<race_id>', methods=['GET'])
def get_race_by_id(race_id):
    return controllers.get_race_by_id(race_id)

@races.route('/race/<race_id>', methods=['PUT'])
def update_race_by_id(race_id):
    return controllers.update_race_by_id(race_id)

@races.route('/race/delete/<race_id>', methods=['DELETE'])
def delete_race_by_id(race_id):
    return controllers.delete_race_by_id(race_id)

@races.route('/races', methods=['GET'])
def get_all_races():
    return controllers.get_all_races()