from flask import Flask, request, jsonify

from db import db
from models.wizards import Wizards

def add_wizard():
    post_data = request.form if request.form else request.json

    fields = ["school_id", "wizard_name", "house", "year_enrolled", "magical_power_level", "active"]
    required_fields = ["school_id", "wizard_name"]

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data is required_fields and not field_data:
            return jsonify({'message': f'Missing required field: {field}'}), 400
        values[field] = field_data

    new_wizard = Wizards(school_id=values.get("school_id"), 
                        wizard_name=values.get("wizard_name"),
                        house=values.get('house'),
                        year_enrolled=values.get('year_enrolled'),
                        magical_power_level=values.get('magical_power_level'),
                        active=values.get('active', True))

    try:
        db.session.add(new_wizard)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error adding wizard: {str(e)}'}), 500
    
    query = db.session.query(Wizards).filter(Wizards.wizard_name == values["wizard_name"]).first()

    wizard = {
        "wizard_id": str(query.wizard_id),
        "school_id": str(query.school_id),
        "wizard_name": query.wizard_name,
        "house": query.house,
        "year_enrolled": query.year_enrolled,
        "magical_power_level": query.magical_power_level,
        "active": query.active
    }

    return jsonify({'message': 'Company added successfully!', "result": wizard}), 201


def get_wizards():
    query = db.session.query(Wizards).all()

    if not query:
        return jsonify({'message': 'No wizards found.'}), 404

    wizards = []
    for wizard in query:
        wizards.append({
            "wizard_id": str(wizard.wizard_id),
            "school_id": str(wizard.school_id),
            "wizard_name": wizard.wizard_name,
            "house": wizard.house,
            "year_enrolled": wizard.year_enrolled,
            "magical_power_level": wizard.magical_power_level,
            "active": wizard.active
        })

    return jsonify({'message': 'Wizards retrieved successfully!', 'result': wizards}), 200

def get_active_wizards():
    query = db.session.query(Wizards).filter(Wizards.active == True).all()

    if not query:
        return jsonify({'message': 'No active wizards found.'}), 404

    active_wizards = []
    for wizard in query:
        active_wizards.append({
            "wizard_id": str(wizard.wizard_id),
            "school_id": str(wizard.school_id),
            "wizard_name": wizard.wizard_name,
            "house": wizard.house,
            "year_enrolled": wizard.year_enrolled,
            "magical_power_level": wizard.magical_power_level,
            "active": wizard.active
        })

    return jsonify({'message': 'Active wizards retrieved successfully!', 'result': active_wizards}), 200

def get_wizard_by_power_level(power_level):
    query = db.session.query(Wizards).filter(Wizards.magical_power_level == power_level).all()

    if not query:
        return jsonify({'message': 'No wizards found for the specified power level.'}), 404

    wizards = []
    for wizard in query:
        wizards.append({
            "wizard_id": str(wizard.wizard_id),
            "school_id": str(wizard.school_id),
            "wizard_name": wizard.wizard_name,
            "house": wizard.house,
            "year_enrolled": wizard.year_enrolled,
            "magical_power_level": wizard.magical_power_level,
            "active": wizard.active
        })

    return jsonify({'message': 'Wizards retrieved successfully!', 'result': wizards}), 200

def get_wizard_by_school_name(school_name):

    query = db.session.query(Wizards).join(Wizards.school).filter(MagicalSchools.school_name == school_name).all()
    if not query:
        return jsonify({'message': 'No wizards found for the specified school name.'}), 404
    wizards = []
    for wizard in query:
        wizards.append({
            "wizard_id": str(wizard.wizard_id),
            "school_id": str(wizard.school_id),
            "wizard_name": wizard.wizard_name,
            "house": wizard.house,
            "year_enrolled": wizard.year_enrolled,
            "magical_power_level": wizard.magical_power_level,
            "active": wizard.active
        })
    return jsonify({'message': 'Wizards retrieved successfully!', 'result': wizards}), 200

def update_wizard(wizard_id):
    post_data = request.form if request.form else request.json

    fields = ["school_id", "wizard_name", "house", "year_enrolled", "magical_power_level", "active"]
    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data is not None:
            values[field] = field_data

    query = db.session.query(Wizards).filter(Wizards.wizard_id == wizard_id).first()

    if not query:
        return jsonify({'message': 'Wizard not found.'}), 404

    for key, value in values.items():
        setattr(query, key, value)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error updating wizard: {str(e)}'}), 500

    return jsonify({'message': 'Wizard updated successfully!'}), 200

def delete_wizard(wizard_id):
    query = db.session.query(Wizards).filter(Wizards.wizard_id == wizard_id).first()

    if not query:
        return jsonify({'message': 'Wizard not found.'}), 404

    try:
        db.session.delete(query)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error deleting wizard: {str(e)}'}), 500

    return jsonify({'message': 'Wizard deleted successfully!'}), 200