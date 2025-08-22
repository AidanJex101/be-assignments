from flask import jsonify, request
from db import db
from models.location import Locations, location_schema, locations_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth


@authenticate_return_auth
def add_location():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    location = Locations.new_location_obj()
    populate_object(location, post_data)
    db.session.add(location)
    db.session.commit()
    return jsonify({"Message": "Location Added", "result": location_schema.dump(location)}), 201

@authenticate_return_auth
def get_all_locations(auth_info):
    if auth_info.user.role == "superadmin":
        locations_query = db.session.query(Locations).all()
        return jsonify({"Message": "Locations Found", "result": locations_schema.dump(locations_query)}), 200
    else:
        return jsonify({"Message": "Unauthorized"}), 401


@authenticate_return_auth
def get_location_by_id(location_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    location = db.session.query(Locations).filter(Locations.id == location_id).first()
    if location:
        return jsonify({"Message": "Location Found", "result": location_schema.dump(location)}), 200
    else:
        return jsonify({"Message": "Location Not Found"}), 404


@authenticate_return_auth
def update_location(location_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    location = db.session.query(Locations).filter(Locations.id == location_id).first()
    if not location:
        return jsonify({"Message": "Location Not Found"}), 404
    populate_object(location, post_data)
    db.session.commit()
    return jsonify({"Message": "Location Updated", "result": location_schema.dump(location)}), 200


@authenticate_return_auth
def delete_location(location_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    location = db.session.query(Locations).filter(Locations.id == location_id).first()
    if not location:
        return jsonify({"Message": "Location Not Found"}), 404
    db.session.delete(location)
    db.session.commit()
    return jsonify({"Message": "Location Deleted"}), 200