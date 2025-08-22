from flask import jsonify, request

from db import db
from models.company import Companies, company_schema, companies_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate

# CREATE

@authenticate_return_auth
def create_company():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    post_data = request.form if request.form else request.get_json()

    new_company = Companies.new_company_obj()
    populate_object(new_company, post_data)

    try:
        db.session.add(new_company)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "company created", "result": company_schema.dump(new_company)}), 201

# READ

@authenticate_return_auth
def get_all_companies():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    query = db.session.query(Companies).all()
    if not query:
        return jsonify({"message": "no companies found"}), 404

    return jsonify({"message": "companies found", "results": companies_schema.dump(query)}), 200


@authenticate_return_auth
def get_company_by_id(company_id):


    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()
    if not query:
        return jsonify({"message": "company not found"}), 404

    return jsonify({"message": "company found", "result": company_schema.dump(query)}), 200

# UPDATE


@authenticate_return_auth
def update_company_by_id(company_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    company_query = db.session.query(Companies).filter(Companies.company_id == company_id).first()
    post_data = request.form if request.form else request.get_json()

    if company_query:
        populate_object(company_query, post_data)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({"message": "unable to update record"}), 400

        return jsonify({"message": "company updated", "result": company_schema.dump(company_query)}), 200

@authenticate_return_auth
def delete_company_by_id(company_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    company_query = db.session.query(Companies).filter(Companies.company_id == company_id).first()
    if not company_query:
        return jsonify({"message": "company not found"}), 404
    try:
        db.session.delete(company_query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400
    return jsonify({"message": "company deleted"}), 200
