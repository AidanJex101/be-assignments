from flask import jsonify, request

from db import db
from models.temple import Temples, temples_schema, temple_schema

from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 

@authenticate_return_auth
def get_temples():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401
    
    temple_query = db.session.query(Temples).all()
    return jsonify({"Message": "Temples Found", "result": temples_schema.dump(temple_query)}), 200

@authenticate_return_auth
def get_temple_by_id(temple_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    temple = db.session.query(Temples).filter(Temples.id == temple_id).first()
    if temple:
        return jsonify({"Message": "Temple Found", "result": temple_schema.dump(temple)}), 200
    else:
        return jsonify({"Message": "Temple Not Found"}), 404
    
@authenticate_return_auth
def add_temple():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    temple = Temples.new_temple_obj()
    populate_object(temple, post_data)
    db.session.add(temple)
    db.session.commit()
    return jsonify({"Message": "Temple Added", "result": temple_schema.dump(temple)}), 201

@authenticate_return_auth
def update_temple(temple_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    temple = db.session.query(Temples).filter(Temples.id == temple_id).first()
    if not temple:
        return jsonify({"Message": "Temple Not Found"}), 404
    populate_object(temple, post_data)
    db.session.commit()
    return jsonify({"Message": "Temple Updated", "result": temple_schema.dump(temple)}), 200

@authenticate_return_auth
def delete_temple(temple_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    temple = db.session.query(Temples).filter(Temples.id == temple_id).first()
    if not temple:
        return jsonify({"Message": "Temple Not Found"}), 404
    db.session.delete(temple)
    db.session.commit()
    return jsonify({"Message": "Temple Deleted"}), 200