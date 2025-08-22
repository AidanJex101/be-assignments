from flask import jsonify, request

from db import db
from models.course import Courses, courses_schema, course_schema

from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 

authenticate_return_auth
def get_courses():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401
    
    course_query = db.session.query(Courses).all()
    return jsonify({"Message": "Courses Found", "result": courses_schema.dump(course_query)}), 200


@authenticate_return_auth
def get_course_by_id(course_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    course = db.session.query(Courses).filter(Courses.id == course_id).first()
    if course:
        return jsonify({"Message": "Course Found", "result": course_schema.dump(course)}), 200
    else:
        return jsonify({"Message": "Course Not Found"}), 404
    
@authenticate_return_auth
def add_course():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    course = Courses.new_course_obj()
    populate_object(course, post_data)
    db.session.add(course)
    db.session.commit()
    return jsonify({"Message": "Course Added", "result": course_schema.dump(course)}), 201

@authenticate_return_auth
def update_course(course_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    post_data = request.form if request.form else request.json
    course = db.session.query(Courses).filter(Courses.id == course_id).first()
    if not course:
        return jsonify({"Message": "Course Not Found"}), 404
    populate_object(course, post_data)
    db.session.commit()
    return jsonify({"Message": "Course Updated", "result": course_schema.dump(course)}), 200

@authenticate_return_auth
def delete_course(course_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"Message": "Unauthorized"}), 401

    course = db.session.query(Courses).filter(Courses.id == course_id).first()
    if not course:
        return jsonify({"Message": "Course Not Found"}), 404
    db.session.delete(course)
    db.session.commit()
    return jsonify({"Message": "Course Deleted"}), 200