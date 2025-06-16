from flask import Blueprint

import controllers

wizard_specializations = Blueprint('wizard_specializations', __name__)

@wizard_specializations.route('/wizard/specialize', methods=['POST'])
def add_wizard_specialization():
    return controllers.wizard_specializations_controller.add_wizard_specialization()