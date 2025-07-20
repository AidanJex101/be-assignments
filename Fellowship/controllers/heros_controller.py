from flask import jsonify, request
from db import db
from models.Heros import Heros, hero_schema, heros_schema
from util.reflection import populate_object

def add_hero():
    post_data = request.form if request.form else request.get_json()
    hero = Heros().new_hero_obj()
    populate_object(hero, post_data)

    db.session.add(hero)
    db.session.commit()

    return jsonify({"Message": "hero Added", "result": hero_schema.dump(hero)}), 201

def get_all_heroes():
    heroes = Heros.query.all()
    return jsonify({"Message": "Heros found", "results": heros_schema.dump(heroes)}), 200

def get_all_alive_heroes():
    heroes = Heros.query.filter_by(is_alive=True).all()
    return jsonify({"Message": "Alive Heros found", "results": heros_schema.dump(heroes)}), 200

def get_hero_by_id(hero_id):
    
    if not hero_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    hero = Heros.query.get(hero_id)
    if not hero:
        return jsonify({"Message": "Hero not found"}), 404

    return jsonify({"Message": "Hero found", "result": hero_schema.dump(hero)}), 200

def update_hero_by_id(hero_id):
    
    if not hero_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    hero = Heros.query.get(hero_id)
    if not hero:
        return jsonify({"Message": "Hero not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(hero, post_data)

    db.session.add(hero)
    db.session.commit()

    return jsonify({"Message": "Hero updated", "result": hero_schema.dump(hero)}), 200

def delete_hero_by_id(hero_id):
    
    if not hero_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    hero = Heros.query.get(hero_id)
    if not hero:
        return jsonify({"Message": "Hero not found"}), 404

    db.session.delete(hero)
    db.session.commit()

    return jsonify({"Message": "Hero deleted"}), 200