from flask import Flask, request, jsonify

from db import db
from models.spells import Spells

def add_spell():
    post_data = request.form if request.form else request.json
    fields = ["school_id", "spell_name", "spell_type", "power_level", "active"]
    required_fields = ["school_id", "spell_name"]

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field in required_fields and not field_data:
            return jsonify({'message': f'Missing required field: {field}'}), 400
        values[field] = field_data

    new_spell = Spells(
        school_id=values.get("school_id"),
        spell_name=values.get("spell_name"),
        spell_type=values.get('spell_type'),
        power_level=values.get('power_level'),
        active=values.get('active', True)
        )
    
    try:
        db.session.add(new_spell)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error adding spell: {str(e)}'}), 500
    
    query = db.session.query(Spells).filter(Spells.spell_name == values["spell_name"]).first()

    spell = {
        "spell_id": str(query.spell_id),
        "school_id": str(query.school_id),
        "spell_name": query.spell_name,
        "spell_type": query.spell_type,
        "power_level": query.power_level,
        "active": query.active
    }
    return jsonify({'message': 'Spell added successfully!', "result": spell}), 201

def get_spells():
    query = db.session.query(Spells).all()
    if not query:
        return jsonify({'message': 'No spells found.'}), 404
    spells = []
    for spell in query:
        spells.append({
            "spell_id": str(spell.spell_id),
            "school_id": str(spell.school_id),
            "spell_name": spell.spell_name,
            "spell_type": spell.spell_type,
            "power_level": spell.power_level,
            "active": spell.active
        })
    return jsonify({'message': 'Spells retrieved successfully!', "spells": spells}), 200

def get_spell_by_difficulty(difficulty):
    query = db.session.query(Spells).filter(Spells.power_level == difficulty).all()
    if not query:
        return jsonify({'message': 'No spells found for the specified difficulty.'}), 404
    spells = []
    for spell in query:
        spells.append({
            "spell_id": str(spell.spell_id),
            "school_id": str(spell.school_id),
            "spell_name": spell.spell_name,
            "spell_type": spell.spell_type,
            "power_level": spell.power_level,
            "active": spell.active
        })
    return jsonify({'message': 'Spells retrieved successfully!', "spells": spells}), 200

def update_spell(spell_id):
    post_data = request.form if request.form else request.json
    fields = ["school_id", "spell_name", "spell_type", "power_level", "active"]
    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data is not None:
            values[field] = field_data

    query = db.session.query(Spells).filter(Spells.spell_id == spell_id).first()
    if not query:
        return jsonify({'message': 'Spell not found.'}), 404

    for key, value in values.items():
        setattr(query, key, value)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error updating spell: {str(e)}'}), 500

    return jsonify({'message': 'Spell updated successfully!'}), 200

def delete_spell(spell_id):
    query = db.session.query(Spells).filter(Spells.spell_id == spell_id).first()
    if not query:
        return jsonify({'message': 'Spell not found.'}), 404

    try:
        db.session.delete(query)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error deleting spell: {str(e)}'}), 500

    return jsonify({'message': 'Spell deleted successfully!'}), 200