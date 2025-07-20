from flask import Blueprint
import controllers

quests = Blueprint('quests', __name__)

@quests.route('/quest', methods=['POST'])
def add_quest():
    return controllers.add_quest()

@quests.route('/quest/<quest_id>', methods=['GET'])
def get_quest_by_id(quest_id):
    return controllers.get_quest_by_id(quest_id)

@quests.route('/quest/<quest_id>', methods=['PUT'])
def update_quest(quest_id):
    return controllers.update_quest_by_id(quest_id)

@quests.route('/quest/<quest_id>', methods=['DELETE'])
def delete_quest(quest_id):
    return controllers.delete_quest_by_id(quest_id)

@quests.route('/quests/<difficulty_level>', methods=['GET'])
def get_quests_by_difficulty(difficulty_level):
    return controllers.get_quest_by_difficulty(difficulty_level)

@quests.route('/quest/<quest_id>/complete', methods=['PUT'])
def complete_quest(quest_id):
    return controllers.update_quest_completed_status_by_id(quest_id)
