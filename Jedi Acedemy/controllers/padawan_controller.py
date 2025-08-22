from flask import jsonify, request

from db import db
from models.padawan import Padawans, padawans_schema, padawan_schema

from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 


@authenticate_return_auth
def get_padawans():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401
    
    padawan_query = db.session.query(Padawans).all()
    return jsonify({"Message": "Padawans Found", "result": padawans_schema.dump(padawan_query)}), 200

@authenticate_return_auth
def get_padawan_by_id(padawan_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    padawan = db.session.query(Padawans).filter(Padawans.id == padawan_id).first()
    if padawan:
        return jsonify({"Message": "Padawan Found", "result": padawan_schema.dump(padawan)}), 200
    else:
        return jsonify({"Message": "Padawan Not Found"}), 404
    
@authenticate_return_auth
def add_padawan():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    padawan = Padawans.new_padawan_obj()
    populate_object(padawan, post_data)
    db.session.add(padawan)
    db.session.commit()
    return jsonify({"Message": "Padawan Added", "result": padawan_schema.dump(padawan)}), 201

@authenticate_return_auth
def update_padawan(padawan_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    padawan = db.session.query(Padawans).filter(Padawans.id == padawan_id).first()
    if not padawan:
        return jsonify({"Message": "Padawan Not Found"}), 404
    populate_object(padawan, post_data)
    db.session.commit()
    return jsonify({"Message": "Padawan Updated", "result": padawan_schema.dump(padawan)}), 200

@authenticate_return_auth
def delete_padawan(padawan_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    padawan = db.session.query(Padawans).filter(Padawans.id == padawan_id).first()
    if not padawan:
        return jsonify({"Message": "Padawan Not Found"}), 404
    db.session.delete(padawan)
    db.session.commit()
    return jsonify({"Message": "Padawan Deleted"}), 200