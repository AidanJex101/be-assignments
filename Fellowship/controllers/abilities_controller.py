from flask import jsonify, request
from db import db
from models.Abilities import Abilities, ability_schema, abilities_schema
from util.reflection import populate_object

def add_ability():
    post_data = request.form if request.form else request.get_json()
    ability = Abilities().new_ability_obj()
    populate_object(ability, post_data)

    db.session.add(ability)
    db.session.commit()

    return jsonify({"Message": "Ability Added", "result": ability_schema.dump(ability)}), 201

def update_ability_by_id(ability_id):
    
    if not ability_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    ability = Abilities.query.get(ability_id)
    if not ability:
        return jsonify({"Message": "Ability not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(ability, post_data)

    db.session.add(ability)
    db.session.commit()

    return jsonify({"Message": "Ability updated", "result": ability_schema.dump(ability)}), 200

def delete_ability_by_id(ability_id):
    
    if not ability_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    ability = Abilities.query.get(ability_id)
    if not ability:
        return jsonify({"Message": "Ability not found"}), 404

    db.session.delete(ability)
    db.session.commit()

    return jsonify({"Message": "Ability deleted"}), 200