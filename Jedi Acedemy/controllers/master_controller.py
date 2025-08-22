from flask import jsonify, request

from db import db
from models.master import Masters, masters_schema, master_schema

from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 

@authenticate_return_auth
def get_masters():
    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401
    
    master_query = db.session.query(Masters).all()
    return jsonify({"Message": "Masters Found", "result": masters_schema.dump(master_query)}), 200

@authenticate_return_auth
def get_master_by_id(master_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    master = db.session.query(Masters).filter(Masters.id == master_id).first()
    if master:
        return jsonify({"Message": "Master Found", "result": master_schema.dump(master)}), 200
    else:
        return jsonify({"Message": "Master Not Found"}), 404

@authenticate_return_auth
def add_master():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    master = Masters.new_master_obj()
    populate_object(master, post_data)
    db.session.add(master)
    db.session.commit()
    return jsonify({"Message": "Master Added", "result": master_schema.dump(master)}), 201

@authenticate_return_auth
def update_master(master_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    master = db.session.query(Masters).filter(Masters.id == master_id).first()
    if not master:
        return jsonify({"Message": "Master Not Found"}), 404
    populate_object(master, post_data)
    db.session.commit()
    return jsonify({"Message": "Master Updated", "result": master_schema.dump(master)}), 200

@authenticate_return_auth
def delete_master(master_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    master = db.session.query(Masters).filter(Masters.id == master_id).first()
    if not master:
        return jsonify({"Message": "Master Not Found"}), 404
    db.session.delete(master)
    db.session.commit()
    return jsonify({"Message": "Master Deleted"}), 200