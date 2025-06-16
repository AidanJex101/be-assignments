from flask import Flask, request, jsonify

from db import db
from models.magical_schools import MagicalSchools

def add_magical_school():

    post_data = request.form if request.form else request.json
    fields = ["school_name", "school_type", "location", "active"]
    required_fields = ["school_name", "school_type"]

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field in required_fields and not field_data:
            return jsonify({'message': f'Missing required field: {field}'}), 400
        values[field] = field_data

    new_school = MagicalSchools(
        school_name=values.get("school_name"),
        school_type=values.get("school_type"),
        location=values.get('location'),
        active=values.get('active', True)
    )

    try:
        db.session.add(new_school)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error adding magical school: {str(e)}'}), 500
    
    query = db.session.query(MagicalSchools).filter(MagicalSchools.school_name == values["school_name"]).first()

    school = {
        "school_id": str(query.school_id), 
        "school_name": query.school_name,
        "school_type": query.school_type,
        "location": query.location,
        "active": query.active
    }

    return jsonify({'message': 'Magical school added successfully!', "result": school}), 201

def get_magical_schools():
    query = db.session.query(MagicalSchools).all()
    if not query:
        return jsonify({'message': 'No magical schools found.'}), 404
    schools = []
    for school in query:
        schools.append({
            "school_id": str(school.school_id),
            "school_name": school.school_name,
            "school_type": school.school_type,
            "location": school.location,
            "active": school.active
        })
    return jsonify({'message': 'Schools retrieved successfully!', "schools": schools}), 200

def get_magical_school_by_id(school_id):
    query = db.session.query(MagicalSchools).filter(MagicalSchools.school_id == school_id).first()
    if not query:
        return jsonify({'message': 'Magical school not found.'}), 404
    school = {
        "school_id": str(query.school_id), 
        "school_name": query.school_name,
        "school_type": query.school_type,
        "location": query.location,
        "active": query.active 
    }
    return jsonify({'message': 'Magical school retrieved successfully!', "school": school}), 200

def update_magical_school(school_id):
    post_data = request.form if request.form else request.json
    fields = ["school_name", "school_type", "location", "active"]

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data is not None:
            values[field] = field_data

    query = db.session.query(MagicalSchools).filter(MagicalSchools.school_id == school_id).first()
    if not query:
        return jsonify({'message': 'Magical school not found.'}), 404

    for key, value in values.items():
        setattr(query, key, value)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error updating magical school: {str(e)}'}), 500

    return jsonify({'message': 'Magical school updated successfully!'}), 200

def delete_magical_school(school_id):
    query = db.session.query(MagicalSchools).filter(MagicalSchools.school_id == school_id).first()
    if not query:
        return jsonify({'message': 'Magical school not found.'}), 404

    try:
        db.session.delete(query)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error deleting magical school: {str(e)}'}), 500

    return jsonify({'message': 'Magical school deleted successfully!'}), 200