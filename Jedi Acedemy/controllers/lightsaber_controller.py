from flask import jsonify, request

from db import db
from models.lightsaber import Lightsabers, lightsabers_schema, lightsaber_schema

from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 


@authenticate_return_auth
def get_lightsabers():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401
    
    lightsaber_query = db.session.query(Lightsabers).all()
    return jsonify({"Message": "Lightsabers Found", "result": lightsabers_schema.dump(lightsaber_query)}), 200

@authenticate_return_auth
def get_lightsaber_by_id(lightsaber_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    lightsaber = db.session.query(Lightsabers).filter(Lightsabers.id == lightsaber_id).first()
    if lightsaber:
        return jsonify({"Message": "Lightsaber Found", "result": lightsaber_schema.dump(lightsaber)}), 200
    else:
        return jsonify({"Message": "Lightsaber Not Found"}), 404

@authenticate_return_auth
def add_lightsaber():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    lightsaber = Lightsabers.new_lightsaber_obj()
    populate_object(lightsaber, post_data)
    db.session.add(lightsaber)
    db.session.commit()
    return jsonify({"Message": "Lightsaber Added", "result": lightsaber_schema.dump(lightsaber)}), 201

@authenticate_return_auth
def update_lightsaber(lightsaber_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    lightsaber = db.session.query(Lightsabers).filter(Lightsabers.id == lightsaber_id).first()
    if not lightsaber:
        return jsonify({"Message": "Lightsaber Not Found"}), 404
    populate_object(lightsaber, post_data)
    db.session.commit()
    return jsonify({"Message": "Lightsaber Updated", "result": lightsaber_schema.dump(lightsaber)}), 200

@authenticate_return_auth
def delete_lightsaber(lightsaber_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    lightsaber = db.session.query(Lightsabers).filter(Lightsabers.id == lightsaber_id).first()
    if not lightsaber:
        return jsonify({"Message": "Lightsaber Not Found"}), 404
    db.session.delete(lightsaber)
    db.session.commit()
    return jsonify({"Message": "Lightsaber Deleted"}), 200