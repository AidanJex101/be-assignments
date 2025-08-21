from flask import jsonify, request

from db import db
from models.warranty import Warranties, warranty_schema, warranties_schema
from util.reflection import populate_object

# CREATE
def create_warranty():
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
def get_all_warranties():
    query = db.session.query(Warranties).all()
    if not query:
        return jsonify({"message": "no warranties found"}), 404

    return jsonify({"message": "warranties found", "results": warranties_schema.dump(query)}), 200

def get_warranty_by_id(warranty_id):
    query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()
    if not query:
        return jsonify({"message": "warranty not found"}), 404

    return jsonify({"message": "warranty found", "result": warranty_schema.dump(query)}), 200

# UPDATE
def update_warranty_by_id(warranty_id):
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
def delete_warranty_by_id(warranty_id):
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