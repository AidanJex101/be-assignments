from flask import jsonify, request
from db import db
from models.battle import Battles, battle_schema, battles_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth

def add_battle():
    post_data = request.form if request.form else request.get_json()
    battle = Battles.new_battle_obj()
    populate_object(battle, post_data)
    db.session.add(battle)
    db.session.commit()
    return jsonify({"Message": "Battle Added", "result": battle_schema.dump(battle)}), 201

@authenticate_return_auth
def get_all_battles(auth_info):
    if auth_info.user.role == "superadmin":
        battles_query = db.session.query(Battles).all()
        return jsonify({"Message": "Battles Found", "result": battles_schema.dump(battles_query)}), 200
    else:
        return jsonify({"Message": "Unauthorized"}), 401
def get_battle_by_id(battle_id):
    battle = db.session.query(Battles).filter(Battles.id == battle_id).first()
    if battle:
        return jsonify({"Message": "Battle Found", "result": battle_schema.dump(battle)}), 200
    else:
        return jsonify({"Message": "Battle Not Found"}), 404
def update_battle(battle_id):
    post_data = request.form if request.form else request.get_json()
    battle = db.session.query(Battles).filter(Battles.id == battle_id).first()
    if not battle:
        return jsonify({"Message": "Battle Not Found"}), 404    
    populate_object(battle, post_data)
    db.session.commit()
    return jsonify({"Message": "Battle Updated", "result": battle_schema.dump(battle)}), 200

def delete_battle(battle_id):   
    battle = db.session.query(Battles).filter(Battles.id == battle_id).first()
    if not battle:
        return jsonify({"Message": "Battle Not Found"}), 404
    db.session.delete(battle)
    db.session.commit()
    return jsonify({"Message": "Battle Deleted"}), 200