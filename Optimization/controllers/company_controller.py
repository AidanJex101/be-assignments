from flask import jsonify, request

from db import db
from models.company import Companies, company_schema, companies_schema
from util.reflection import populate_object

# CREATE
def create_company():
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
def get_all_companies():
    query = db.session.query(Companies).all()
    if not query:
        return jsonify({"message": "no companies found"}), 404

    return jsonify({"message": "companies found", "results": companies_schema.dump(query)}), 200

def get_company_by_id(company_id):
    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()
    if not query:
        return jsonify({"message": "company not found"}), 404

    return jsonify({"message": "company found", "result": company_schema.dump(query)}), 200

# UPDATE
def update_company_by_id(company_id):
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
