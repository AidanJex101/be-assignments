from flask import jsonify, request

from db import db
from models.warranty import Warranties, warranty_schema, warranties_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate

# CREATE

@authenticate_return_auth
def create_warranty():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    post_data = request.form if request.form else request.get_json()

    new_warranty = Warranties.new_warranty_obj()
    populate_object(new_warranty, post_data)

    try:
        db.session.add(new_warranty)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "warranty created", "result": warranty_schema.dump(new_warranty)}), 201

# READ
@authenticate_return_auth
def get_all_warranties():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    query = db.session.query(Warranties).all()
    if not query:
        return jsonify({"message": "no warranties found"}), 404

    return jsonify({"message": "warranties found", "results": warranties_schema.dump(query)}), 200

@authenticate_return_auth
def get_warranty_by_id(warranty_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()
    if not query:
        return jsonify({"message": "warranty not found"}), 404

    return jsonify({"message": "warranty found", "result": warranty_schema.dump(query)}), 200

# UPDATE
@authenticate_return_auth
def update_warranty_by_id(warranty_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    warranty_query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()
    post_data = request.form if request.form else request.get_json()

    if warranty_query:
        populate_object(warranty_query, post_data)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({"message": "unable to update record"}), 400

        return jsonify({"message": "warranty updated", "result": warranty_schema.dump(warranty_query)}), 200
    else:
        return jsonify({"message": "warranty not found"}), 404
    
# DELETE
@authenticate_return_auth
def delete_warranty_by_id(warranty_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    warranty_query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    if not warranty_query:
        return jsonify({"message": "warranty not found"}), 404

    try:
        db.session.delete(warranty_query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "warranty deleted"}), 200