from flask import jsonify, request
from db import db
from models.pokemon import Pokemon, pokemon_schema, pokemons_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth

@authenticate_return_auth
def add_pokemon():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    pokemon = Pokemon.new_pokemon_obj()
    populate_object(pokemon, post_data)
    db.session.add(pokemon)
    db.session.commit()
    return jsonify({"Message": "Pokemon Added", "result": pokemon_schema.dump(pokemon)}), 201

@authenticate_return_auth
def get_all_pokemon(auth_info):
    if auth_info.user.role == "superadmin":
        pokemon_query = db.session.query(Pokemon).all()
        return jsonify({"Message": "Pokemon Found", "result": pokemons_schema.dump(pokemon_query)}), 200
    else:
        return jsonify({"Message": "Unauthorized"}), 401


@authenticate_return_auth
def get_pokemon_by_id(pokemon_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    pokemon = db.session.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if pokemon:
        return jsonify({"Message": "Pokemon Found", "result": pokemon_schema.dump(pokemon)}), 200
    else:
        return jsonify({"Message": "Pokemon Not Found"}), 404


@authenticate_return_auth
def update_pokemon(pokemon_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    pokemon = db.session.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if not pokemon:
        return jsonify({"Message": "Pokemon Not Found"}), 404
    populate_object(pokemon, post_data)
    db.session.commit()
    return jsonify({"Message": "Pokemon Updated", "result": pokemon_schema.dump(pokemon)}), 200


@authenticate_return_auth
def delete_pokemon(pokemon_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    pokemon = db.session.query(Pokemon).filter(Pokemon.id == pokemon_id).first()
    if not pokemon:
        return jsonify({"Message": "Pokemon Not Found"}), 404
    db.session.delete(pokemon)
    db.session.commit()
    return jsonify({"Message": "Pokemon Deleted"}), 200