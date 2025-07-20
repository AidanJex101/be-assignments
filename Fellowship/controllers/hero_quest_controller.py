from flask import jsonify, request
from db import db
from models.hero_quest import HeroQuest, hero_quest_schema, hero_quests_schema
from util.reflection import populate_object

def add_hero_to_quest():
    post_data = request.form if request.form else request.get_json()
    hero_quest = HeroQuest().new_hero_quest_obj()
    populate_object(hero_quest, post_data)

    db.session.add(hero_quest)
    db.session.commit()

    return jsonify({"Message": "Hero added to quest", "result": hero_quest_schema.dump(hero_quest)}), 201

def get_all_by_hero_id(hero_id):
    
    if not hero_id:
        return jsonify({"Message": "Hero ID parameter is required"}), 400

    hero_quests = HeroQuest.query.filter_by(hero_id=hero_id).all()
    if not hero_quests:
        return jsonify({"Message": "No quests found for the specified hero"}), 404

    return jsonify({"Message": "Hero quests found", "results": hero_quests_schema.dump(hero_quests)}), 200
    