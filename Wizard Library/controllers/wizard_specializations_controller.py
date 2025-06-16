from flask import Flask, request, jsonify

from db import db
from models.wizard_specializations import WizardSpecializations

def add_wizard_specialization():
    post_data = request.form if request.form else request.json
    fields = ["wizard_id", "specialization_name", "description", "active"]
    required_fields = ["wizard_id", "specialization_name"]

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field in required_fields and not field_data:
            return jsonify({'message': f'Missing required field: {field}'}), 400
        values[field] = field_data

    new_specialization = WizardSpecializations(
        specialization_name=values.get("specialization_name"),
        description=values.get("description"),
        active=values.get('active', True)
    )

    try:
        db.session.add(new_specialization)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error adding wizard specialization: {str(e)}'}), 500
    
    query = db.session.query(WizardSpecializations).filter(WizardSpecializations.specialization_name == values["specialization_name"]).first()

    specialization = {
        "wizard_id": str(query.wizard_id),
        "specialization_id": str(query.specialization_id),
        "specialization_name": query.specialization_name,
        "description": query.description,
        "active": query.active
    }