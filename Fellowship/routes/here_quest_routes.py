from flask import Blueprint
import controllers

hero_quest = Blueprint('hero_quest', __name__)

@hero_quest.route('/hero-quest', methods=['POST'])
def add_hero_to_quest():
    return controllers.hero_quest_controller.add_hero_to_quest()

@hero_quest.route('/hero/<hero_id>', methods=['GET'])
def get_all_by_hero_id(hero_id):
    return controllers.hero_quest_controller.get_all_by_hero_id(hero_id)