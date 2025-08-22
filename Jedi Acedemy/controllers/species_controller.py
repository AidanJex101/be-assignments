from flask import jsonify, request

from db import db
from models.species import Species, species_schema, species_list_schema

from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 

@authenticate_return_auth
def get_species():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401
    
    species_query = db.session.query(Species).all()
    return jsonify({"Message": "Species Found", "result": species_list_schema.dump(species_query)}), 200

@authenticate_return_auth
def get_species_by_id(species_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    species = db.session.query(Species).filter(Species.id == species_id).first()
    if species:
        return jsonify({"Message": "Species Found", "result": species_schema.dump(species)}), 200
    else:
        return jsonify({"Message": "Species Not Found"}), 404
    
@authenticate_return_auth
def add_species():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    species = Species.new_species_obj()
    populate_object(species, post_data)
    db.session.add(species)
    db.session.commit()
    return jsonify({"Message": "Species Added", "result": species_schema.dump(species)}), 201

@authenticate_return_auth
def update_species(species_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    species = db.session.query(Species).filter(Species.id == species_id).first()
    if not species:
        return jsonify({"Message": "Species Not Found"}), 404
    populate_object(species, post_data)
    db.session.commit()
    return jsonify({"Message": "Species Updated", "result": species_schema.dump(species)}), 200

@authenticate_return_auth
def delete_species(species_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    species = db.session.query(Species).filter(Species.id == species_id).first()
    if not species:
        return jsonify({"Message": "Species Not Found"}), 404
    db.session.delete(species)
    db.session.commit()
    return jsonify({"Message": "Species Deleted"}), 200