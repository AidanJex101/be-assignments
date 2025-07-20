from flask import jsonify, request
from db import db
from models.Location import Location, location_schema, locations_schema
from util.reflection import populate_object

def add_location():
    post_data = request.form if request.form else request.get_json()
    location = Location().new_location_obj()
    populate_object(location, post_data)

    db.session.add(location)
    db.session.commit()

    return jsonify({"Message": "Location Added", "result": location_schema.dump(location)}), 201

def get_location_by_id(location_id):
   
    if not location_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    location = Location.query.get(location_id)
    if not location:
        return jsonify({"Message": "Location not found"}), 404

    return jsonify({"Message": "Location found", "result": location_schema.dump(location)}), 200

def update_location_by_id(location_id):
   
    if not location_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    location = Location.query.get(location_id)
    if not location:
        return jsonify({"Message": "Location not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(location, post_data)

    db.session.add(location)
    db.session.commit()

    return jsonify({"Message": "Location updated", "result": location_schema.dump(location)}), 200

def delete_location_by_id(location_id):
   
    if not location_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    location = Location.query.get(location_id)
    if not location:
        return jsonify({"Message": "Location not found"}), 404

    db.session.delete(location)
    db.session.commit()

    return jsonify({"Message": "Location deleted"}), 200