from flask import jsonify, request
from db import db
from models.Quests import Quests, quest_schema, quests_schema
from util.reflection import populate_object

def add_quest():
    post_data = request.form if request.form else request.get_json()
    quest = Quests().new_quest_obj()
    populate_object(quest, post_data)

    db.session.add(quest)
    db.session.commit()

    return jsonify({"Message": "quest Added", "result": quest_schema.dump(quest)}), 201

def get_quest_by_difficulty(difficulty):

    if not difficulty:
        return jsonify({"Message": "Difficulty parameter is required"}), 400

    quests = Quests.query.filter_by(difficulty=difficulty).all()
    if not quests:
        return jsonify({"Message": "No quests found for the specified difficulty"}), 404

    return jsonify({"Message": "Quests found", "results": quests_schema.dump(quests)}), 200

def get_quest_by_id(quest_id):
    
    if not quest_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    quest = Quests.query.get(quest_id)
    if not quest:
        return jsonify({"Message": "Quest not found"}), 404

    return jsonify({"Message": "Quest found", "result": quest_schema.dump(quest)}), 200

def update_quest_by_id(quest_id):
    
    if not quest_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    quest = Quests.query.get(quest_id)
    if not quest:
        return jsonify({"Message": "Quest not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(quest, post_data)

    db.session.add(quest)
    db.session.commit()

    return jsonify({"Message": "Quest updated", "result": quest_schema.dump(quest)}), 200

def update_quest_completed_status_by_id(quest_id):
    
    if not quest_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    quest = Quests.query.get(quest_id)
    if not quest:
        return jsonify({"Message": "Quest not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(quest, post_data)

    db.session.add(quest)
    db.session.commit()

    return jsonify({"Message": "Quest completed", "result": quest_schema.dump(quest)}), 200

def delete_quest_by_id(quest_id):
    
    if not quest_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    quest = Quests.query.get(quest_id)
    if not quest:
        return jsonify({"Message": "Quest not found"}), 404

    db.session.delete(quest)
    db.session.commit()

    return jsonify({"Message": "Quest deleted"}), 200