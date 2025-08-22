from flask import jsonify, request

from db import db
from models.category import Categories, category_schema, categories_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 

# CREATE

@authenticate_return_auth
def create_category():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    post_data = request.form if request.form else request.get_json()

    new_category = Categories.new_category_obj()
    populate_object(new_category, post_data)

    try:
        db.session.add(new_category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "category created", "result": category_schema.dump(new_category)}), 201

# READ
@authenticate_return_auth
def get_all_categories():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401
    query = db.session.query(Categories).all()
    if not query:
        return jsonify({"message": "no categories found"}), 404

    return jsonify({"message": "categories found", "results": categories_schema.dump(query)}), 200


@authenticate_return_auth
def get_category_by_id(category_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()
    if not query:
        return jsonify({"message": "category not found"}), 404

    return jsonify({"message": "category found", "result": category_schema.dump(query)}), 200

# UPDATE
@authenticate_return_auth
def update_category_by_id(category_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()
    post_data = request.form if request.form else request.get_json()

    if category_query:
        populate_object(category_query, post_data)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({"message": "unable to update record"}), 400

        return jsonify({"message": "category updated", "result": category_schema.dump(category_query)}), 200
    else:
        return jsonify({"message": "category not found"}), 404
    
# DELETE

@authenticate_return_auth
def delete_category_by_id(category_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    if not category_query:
        return jsonify({"message": "category not found"}), 404

    try:
        db.session.delete(category_query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "category deleted"}), 200