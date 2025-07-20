from flask import jsonify, request
from db import db
from models.Races import Races, race_schema, races_schema
from util.reflection import populate_object

def add_race():
    post_data = request.form if request.form else request.get_json()
    race = Races().new_race_obj()
    populate_object(race, post_data)

    db.session.add(race)
    db.session.commit()

    return jsonify({"Message": "Added race", "result": race_schema.dump(race)}), 201

def get_all_races():
    races = Races.query.all()
    return jsonify({"Message": "Races found", "results": races_schema.dump(races)}), 200

def get_race_by_id(race_id):
    if not race_id:
        return jsonify({"Message": "ID parameter is required"}), 400
    
    race = Races.query.get(race_id)
    if not race:
        return jsonify({"Message": "No races found with the specified ID"}), 404
    
    return jsonify({"Message": "Races found", "results": races_schema.dump(race)}), 200

def update_race_by_id(race_id):
    if not race_id:
        return jsonify({"Message": "ID parameter is required"}), 400
    
    race = Races.query.get(race_id)
    if not race:
        return jsonify({"Message": "ID is required"}), 404
    
    post_data = request.form if request.form else request.get_json()
    populate_object(race, post_data)
                    
    db.session.add(race)
    db.session.commit()

    return jsonify({"Message": "Race updated", "result": race_schema.dump(race)}), 200

def delete_race_by_id(race_id):
    
    if not race_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    race = Races.query.get(race_id)
    if not race:
        return jsonify({"Message": "race not found"}), 404

    db.session.delete(race)
    db.session.commit()

    return jsonify({"Message": "race deleted"}), 200

    
