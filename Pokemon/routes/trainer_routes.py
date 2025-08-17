from flask import Blueprint

import controllers

trainer = Blueprint('trainer', __name__)

@trainer.route('/trainers', methods=['GET'])
def get_trainers():
    return controllers.get_all_trainers()

@trainer.route('/trainers/<int:trainer_id>', methods=['GET'])
def get_trainer(trainer_id):
    return controllers.get_trainer_by_id(trainer_id)

@trainer.route('/trainers', methods=['POST'])
def create_trainer():
    return controllers.add_trainer()

@trainer.route('/trainers/<int:trainer_id>', methods=['PUT'])
def update_trainer(trainer_id):
    return controllers.update_trainer(trainer_id)

@trainer.route('/trainers/<int:trainer_id>', methods=['DELETE'])
def delete_trainer(trainer_id):
    return controllers.delete_trainer(trainer_id)