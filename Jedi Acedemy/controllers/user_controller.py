from flask import jsonify, request
from flask_bcrypt import generate_password_hash

from db import db
from models.app_users import AppUsers, app_users_schema, app_user_schema
from models.organizations import Organizations
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 


def add_user():
    post_data = request.form if request.form else request.get_json()
    
    org_id = post_data.get('ord_id')

    new_user = AppUsers.new_user_obj()
    new_user.password = generate_password_hash(new_user.password).decode('utf-8')
    
    if org_id:
        org_query = db.session.query(Organizations).filter(Organizations.org_id == org_id).first()
        if org_query is None:
            return jsonify({"message": "Org id is required"}), 404

    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"Message": "User Added", "result": app_user_schema.dump(new_user)}), 201


@authenticate
def get_all_users():

    users_query = db.session.query(AppUsers).all()

    if users_query is None:
        return jsonify({"Message": "No Users Found"}), 404
    
    return jsonify({"Message": "Users Found", "results": app_users_schema.dump(users_query)}), 200

@authenticate_return_auth
def get_user_by_id(user_id, auth_info):
    user_query = db.session.query(AppUsers).filter(AppUsers.user_id == user_id).first()
    
    if auth_info.user.role == "superadmin" or user_id == str(auth_info.user.user_id):
        return jsonify({"Message": "User Found", "result": app_user_schema.dump(user_query)}), 200
    
    return jsonify({"Message": "Unauthorized"}), 401