from flask import jsonify, request
from flask_bcrypt import generate_password_hash

from db import db
from models.users import Users, users_schema, user_schema
from models.trainer import Trainers
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 

@authenticate_return_auth
def add_user():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    
    trainer_id = post_data.get('trainer_id')

    new_user = Users.new_user_obj()
    new_user.password = generate_password_hash(new_user.password).decode('utf-8')
    
    if trainer_id:
        trainer_query = db.session.query(Trainers).filter(Trainers.trainer_id == trainer_id).first()
        if trainer_query is None:
            return jsonify({"message": "Trainer id is required"}), 404

    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"Message": "User Added", "result": user_schema.dump(new_user)}), 201


@authenticate_return_auth
def get_all_users():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    users_query = db.session.query(Users).all()

    if users_query is None:
        return jsonify({"Message": "No Users Found"}), 404
    
    return jsonify({"Message": "Users Found", "results": users_schema.dump(users_query)}), 200

@authenticate_return_auth
def get_user_by_id(user_id, auth_info):
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()
    
    if auth_info.user.role == "superadmin" or user_id == str(auth_info.user.user_id):
        return jsonify({"Message": "User Found", "result": user_schema.dump(user_query)}), 200
    
    return jsonify({"Message": "Unauthorized"}), 401