from flask import jsonify, request

from db import db
from models.padawan_course import PadawanCourses, padawan_courses_schema, padawan_course_schema

from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 

@authenticate_return_auth
def get_padawan_courses():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401
    
    padawan_course_query = db.session.query(PadawanCourses).all()
    return jsonify({"Message": "Padawan Courses Found", "result": padawan_courses_schema.dump(padawan_course_query)}), 200

@authenticate_return_auth
def get_padawan_course_by_id(padawan_course_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    padawan_course = db.session.query(PadawanCourses).filter(PadawanCourses.id == padawan_course_id).first()
    if padawan_course:
        return jsonify({"Message": "Padawan Course Found", "result": padawan_course_schema.dump(padawan_course)}), 200
    else:
        return jsonify({"Message": "Padawan Course Not Found"}), 404
    
@authenticate_return_auth
def add_padawan_course():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    padawan_course = PadawanCourses.new_padawan_course_obj()
    populate_object(padawan_course, post_data)
    db.session.add(padawan_course)
    db.session.commit()
    return jsonify({"Message": "Padawan Course Added", "result": padawan_course_schema.dump(padawan_course)}), 201

@authenticate_return_auth
def update_padawan_course(padawan_course_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    padawan_course = db.session.query(PadawanCourses).filter(PadawanCourses.id == padawan_course_id).first()
    if not padawan_course:
        return jsonify({"Message": "Padawan Course Not Found"}), 404
    populate_object(padawan_course, post_data)
    db.session.commit()
    return jsonify({"Message": "Padawan Course Updated", "result": padawan_course_schema.dump(padawan_course)}), 200


@authenticate_return_auth
def delete_padawan_course(padawan_course_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    padawan_course = db.session.query(PadawanCourses).filter(PadawanCourses.id == padawan_course_id).first()
    if not padawan_course:
        return jsonify({"Message": "Padawan Course Not Found"}), 404
    db.session.delete(padawan_course)
    db.session.commit()
    return jsonify({"Message": "Padawan Course Deleted"}), 200