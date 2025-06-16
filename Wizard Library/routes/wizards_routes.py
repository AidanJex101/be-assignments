from flask import Blueprint

import controllers

wizards = Blueprint('wizards', __name__)

@wizards.route('/wizard', methods=['POST'])
def add_wizard():
    return controllers.wizards_controller.add_wizard()

@wizards.route('/wizards', methods=['GET'])
def get_wizards():
    return controllers.wizards_controller.get_wizards()

@wizards.route('/wizard/active', methods=['GET'])
def get_active_wizards():
    return controllers.wizards_controller.get_active_wizards()

@wizards.route('/wizard/<magical_power_level>', methods=['GET'])
def get_wizards_by_power_level(magical_power_level):
    return controllers.wizards_controller.get_wizards_by_power_level(magical_power_level)

@wizards.route('/wizard/<school_name>', methods=['GET'])
def get_wizards_by_school(school_name):
    return controllers.wizards_controller.get_wizards_by_school(school_name)

@wizards.route('/wizard/<int:wizard_id>', methods=['PUT'])
def update_wizard(wizard_id):
    return controllers.wizards_controller.update_wizard(wizard_id)

@wizards.route('/wizard/delete/<int:wizard_id>', methods=['DELETE'])
def delete_wizard(wizard_id):
    return controllers.wizards_controller.delete_wizard(wizard_id)


