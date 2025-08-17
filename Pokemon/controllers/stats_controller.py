from flask import jsonify, request
from db import db
from models.stats import Stats, stat_schema, stats_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth


def add_stat():
    post_data = request.form if request.form else request.get_json()
    stat = Stats.new_stat_obj()
    populate_object(stat, post_data)
    db.session.add(stat)
    db.session.commit()
    return jsonify({"Message": "Stat Added", "result": stat_schema.dump(stat)}), 201

@authenticate_return_auth
def get_all_stats(auth_info):
    if auth_info.user.role == "superadmin":
        stats_query = db.session.query(Stats).all()
        return jsonify({"Message": "Stats Found", "result": stats_schema.dump(stats_query)}), 200
    else:
        return jsonify({"Message": "Unauthorized"}), 401
    
def get_stat_by_id(stat_id):
    stat = db.session.query(Stats).filter(Stats.id == stat_id).first()
    if stat:
        return jsonify({"Message": "Stat Found", "result": stat_schema.dump(stat)}), 200
    else:
        return jsonify({"Message": "Stat Not Found"}), 404
    
def update_stat(stat_id):
    post_data = request.form if request.form else request.get_json()
    stat = db.session.query(Stats).filter(Stats.id == stat_id).first()
    if not stat:
        return jsonify({"Message": "Stat Not Found"}), 404
    populate_object(stat, post_data)
    db.session.commit()
    return jsonify({"Message": "Stat Updated", "result": stat_schema.dump(stat)}), 200

def delete_stat(stat_id):
    stat = db.session.query(Stats).filter(Stats.id == stat_id).first()
    if not stat:
        return jsonify({"Message": "Stat Not Found"}), 404
    db.session.delete(stat)
    db.session.commit()
    return jsonify({"Message": "Stat Deleted"}), 200