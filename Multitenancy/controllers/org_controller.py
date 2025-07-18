from flask import jsonify, request
from db import db
from models.organizations import Organizations, org_schema, orgs_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth

def add_org():
    post_data = request.form if request.form else request.get_json()
    org = Organizations.new_org_obj()
    populate_object(org, post_data)
    
    db.session.add(org)
    db.session.commit()
    
    return jsonify({"Message": "Org Added", "result": org_schema.dump(org)}), 201

@authenticate_return_auth
def get_all_orgs(auth_info):
    if auth_info.user.role == "superadmin":
        orgs_query = db.session.query(Organizations).all()
    
        return jsonify({"Message": "Orgs Found", "result": orgs_schema.dump(orgs_query)}), 200
    return jsonify({"Message": "Unauthorized"}), 401