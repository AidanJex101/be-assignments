from flask import Blueprint

import controllers

course = Blueprint('course', __name__)

@course.route('/courses', methods=['GET'])
def get_courses():
    return controllers.get_courses()

@course.route('/courses/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    return controllers.get_course_by_id(course_id)

@course.route('/courses', methods=['POST'])
def add_course():
    return controllers.add_course()

@course.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    return controllers.update_course(course_id)

@course.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    return controllers.delete_course(course_id)