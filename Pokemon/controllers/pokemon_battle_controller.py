from flask import jsonify, request
from db import db
from models.pokemon_battle_xref import PokemonBattleXref, pokemon_battle_xref_schema, pokemon_battles_xref_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth

@authenticate_return_auth
def get_all_pokemon_battles():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "Unauthorized"}), 401
    
    pokemon_battles = PokemonBattleXref.query.all()
    return jsonify({"message": "Pokemon battles retrieved successfully", "result": pokemon_battles_xref_schema.dump(pokemon_battles)}), 200

@authenticate_return_auth
def get_pokemon_battle_by_id(auth_info, pokemon_battle_id):

    if auth_info.user.role != "superadmin":
        return jsonify({"message": "Unauthorized"}), 401
    
    pokemon_battle = PokemonBattleXref.query.filter_by(pokemon_battle_id=pokemon_battle_id).first()
    if pokemon_battle:
        return jsonify({"message": "Pokemon battle found", "result": pokemon_battle_xref_schema.dump(pokemon_battle)}), 200
    else:
        return jsonify({"message": "Pokemon battle not found"}), 404

@authenticate_return_auth
def add_pokemon_battle():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.get_json()
    pokemon_battle = PokemonBattleXref.new_pokemon_battle_xref_obj()
    populate_object(pokemon_battle, post_data)
    db.session.add(pokemon_battle)
    db.session.commit()
    return jsonify({"message": "Pokemon battle added", "result": pokemon_battle_xref_schema.dump(pokemon_battle)}), 201

@authenticate_return_auth
def update_pokemon_battle(pokemon_battle_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.get_json()
    pokemon_battle = PokemonBattleXref.query.filter_by(pokemon_battle_id=pokemon_battle_id).first()
    if not pokemon_battle:
        return jsonify({"message": "Pokemon battle not found"}), 404
    populate_object(pokemon_battle, post_data)
    db.session.commit()
    return jsonify({"message": "Pokemon battle updated", "result": pokemon_battle_xref_schema.dump(pokemon_battle)}), 200

@authenticate_return_auth
def delete_pokemon_battle(pokemon_battle_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "Unauthorized"}), 401

    pokemon_battle = PokemonBattleXref.query.filter_by(pokemon_battle_id=pokemon_battle_id).first()
    if not pokemon_battle:
        return jsonify({"message": "Pokemon battle not found"}), 404
    db.session.delete(pokemon_battle)
    db.session.commit()
    return jsonify({"message": "Pokemon battle deleted"}), 200