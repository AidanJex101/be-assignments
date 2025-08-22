from flask import jsonify, request

from db import db
from models.crystal import Crystals, crystals_schema, crystal_schema

from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 

@authenticate_return_auth
def get_crystals():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401
    
    crystal_query = db.session.query(Crystals).all()
    return jsonify({"Message": "Crystals Found", "result": crystals_schema.dump(crystal_query)}), 200

@authenticate_return_auth
def get_crystal_by_id(crystal_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    crystal = db.session.query(Crystals).filter(Crystals.id == crystal_id).first()
    if crystal:
        return jsonify({"Message": "Crystal Found", "result": crystal_schema.dump(crystal)}), 200
    else:
        return jsonify({"Message": "Crystal Not Found"}), 404
    
@authenticate_return_auth
def add_crystal():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    crystal = Crystals.new_crystal_obj()
    populate_object(crystal, post_data)
    db.session.add(crystal)
    db.session.commit()
    return jsonify({"Message": "Crystal Added", "result": crystal_schema.dump(crystal)}), 201

@authenticate_return_auth
def update_crystal(crystal_id):
    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    crystal = db.session.query(Crystals).filter(Crystals.id == crystal_id).first()
    if not crystal:
        return jsonify({"Message": "Crystal Not Found"}), 404
    populate_object(crystal, post_data)
    db.session.commit()
    return jsonify({"Message": "Crystal Updated", "result": crystal_schema.dump(crystal)}), 200

@authenticate_return_auth
def delete_crystal(crystal_id):
    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    crystal = db.session.query(Crystals).filter(Crystals.id == crystal_id).first()
    if not crystal:
        return jsonify({"Message": "Crystal Not Found"}), 404
    db.session.delete(crystal)
    db.session.commit()
    return jsonify({"Message": "Crystal Deleted"}), 200