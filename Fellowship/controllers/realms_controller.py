from flask import jsonify, request
from db import db
from models.Realms import Realms, realm_schema, realms_schema
from util.reflection import populate_object

def add_realm():
    post_data = request.form if request.form else request.get_json()
    realm = Realms().new_realm_obj()
    populate_object(realm, post_data)

    db.session.add(realm)
    db.session.commit()

    return jsonify({"Message": "Realm Added", "result": realm_schema.dump(realm)}), 201


def get_realm_by_id(realm_id):
    
    if not realm_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    realm = Realms.query.get(realm_id)
    if not realm:
        return jsonify({"Message": "Realm not found"}), 404

    return jsonify({"Message": "Realm found", "result": realm_schema.dump(realm)}), 200

def update_realm_by_id(realm_id):
    
    if not realm_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    realm = Realms.query.get(realm_id)
    if not realm:
        return jsonify({"Message": "Realm not found"}), 404

    post_data = request.form if request.form else request.get_json()
    populate_object(realm, post_data)

    db.session.add(realm)
    db.session.commit()

    return jsonify({"Message": "Realm updated", "result": realm_schema.dump(realm)}), 200

def delete_realm_by_id(realm_id):
    
    if not realm_id:
        return jsonify({"Message": "ID parameter is required"}), 400

    realm = Realms.query.get(realm_id)
    if not realm:
        return jsonify({"Message": "Realm not found"}), 404

    db.session.delete(realm)
    db.session.commit()

    return jsonify({"Message": "Realm deleted"}), 200
