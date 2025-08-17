from flask import jsonify, request
from db import db
from models.trainer import Trainers, trainer_schema, trainers_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth

def add_trainer():
    post_data = request.form if request.form else request.get_json()
    trainer = Trainers.new_trainer_obj()
    populate_object(trainer, post_data)
    db.session.add(trainer)
    db.session.commit()

    return jsonify({"Message": "Trainer Added", "result": trainer_schema.dump(trainer)}), 201

@authenticate_return_auth
def get_all_trainers(auth_info):
    if auth_info.user.role == "superadmin":
        trainers_query = db.session.query(Trainers).all()
        return jsonify({"Message": "Trainers Found", "result": trainers_schema.dump(trainers_query)}), 200
    else:
        return jsonify({"Message": "Unauthorized"}), 401
    

def get_trainer_by_id(trainer_id):
    trainer = db.session.query(Trainers).filter(Trainers.id == trainer_id).first()
    if trainer:
        return jsonify({"Message": "Trainer Found", "result": trainer_schema.dump(trainer)}), 200
    else:
        return jsonify({"Message": "Trainer Not Found"}), 404
    
def update_trainer(trainer_id):
    post_data = request.form if request.form else request.get_json()
    trainer = db.session.query(Trainers).filter(Trainers.id == trainer_id).first()

    if not trainer:
        return jsonify({"Message": "Trainer Not Found"}), 404
    
    populate_object(trainer, post_data)
    db.session.commit()
    return jsonify({"Message": "Trainer Updated", "result": trainer_schema.dump(trainer)}), 200

def delete_trainer(trainer_id):
    trainer = db.session.query(Trainers).filter(Trainers.id == trainer_id).first()
    
    if not trainer:
        return jsonify({"Message": "Trainer Not Found"}), 404
    
    db.session.delete(trainer)
    db.session.commit()
    return jsonify({"Message": "Trainer Deleted"}), 200