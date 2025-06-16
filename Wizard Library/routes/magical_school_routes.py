from flask import Blueprint

import controllers

magical_schools = Blueprint('magical_schools', __name__)

@magical_schools.route('/school', methods=['POST'])
def add_magical_school():
    return controllers.magical_schools_controller.add_magical_school()

@magical_schools.route('/schools', methods=['GET'])
def get_magical_schools():
    return controllers.magical_schools_controller.get_magical_schools()

@magical_schools.route('/school/<int:school_id>', methods=['GET'])
def get_magical_school(school_id):
    return controllers.magical_schools_controller.get_magical_school(school_id)

@magical_schools.route('/school/<int:school_id>', methods=['PUT'])
def update_magical_school(school_id):
    return controllers.magical_schools_controller.update_magical_school(school_id)

@magical_schools.route('/school/delete/<int:school_id>', methods=['DELETE'])
def delete_magical_school(school_id):
    return controllers.magical_schools_controller.delete_magical_school(school_id)
