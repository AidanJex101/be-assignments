from flask import Flask, request, jsonify

from db import db
from models.company import Company

def add_company():
    post_data = request.form if request.form else request.json

    fields = ["company_name"]
    required_fields = ["company_name"]

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data is required_fields and not field_data:
            return jsonify({'message': f'Missing required field: {field}'}), 400
        values[field] = field_data

    new_company = Company(values['company_name'])

    try:
        db.session.add(new_company)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error adding company: {str(e)}'}), 500
    
    query = db.session.query(Company).filter(company_name=values['company_name']).first()

    company = {
        'id': query.id,
        'company_name': query.company_name
    }

    return jsonify({'message': 'Company added successfully!'}), 201

def get_all_companies():
    query = db.session.query(Company).all()

    company_list = []

    for company in query:
        company_dict = {
            'id': company.id,
            'company_name': company.company_name
        }

        company_list.append(company_dict)

    return jsonify({"message": "Companies retrieved successfully!", "results": company_list}), 200

def get_company_by_id(company_id):
    query = db.session.query(Company).filter_by(id=company_id).first()

    if not query:
        return jsonify({'message': 'Company not found!'}), 404

    company = {
        'id': query.id,
        'company_name': query.company_name
    }

    return jsonify({'message': 'Company retrieved successfully!', 'result': company}), 200

def update_company(company_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Company).filter(Company.company_id == company_id).first()

    query.company_name = post_data.get('company_name', query.company_name)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error updating company: {str(e)}'}), 500
    
    company = {
        'id': query.id,
        'company_name': query.company_name
    }

    return jsonify({'message': 'Company updated successfully!', 'result': company}), 200

def delete_company(company_id):
    query = db.session.query(Company).filter(Company.id == company_id).first()

    if not query:
        return jsonify({'message': 'Company not found!'}), 404

    try:
        db.session.delete(query)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error deleting company: {str(e)}'}), 500

    return jsonify({'message': 'Company deleted successfully!'}), 200