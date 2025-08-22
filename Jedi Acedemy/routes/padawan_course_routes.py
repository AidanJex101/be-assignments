from flask import Blueprint

import controllers

padawan_course = Blueprint('padawan_course', __name__)

@padawan_course.route('/padawan_courses', methods=['GET'])
def get_padawan_courses():
    return controllers.get_padawan_courses()

@padawan_course.route('/padawan_courses/<int:padawan_course_id>', methods=['GET'])
def get_padawan_course_by_id(padawan_course_id):
    return controllers.get_padawan_course_by_id(padawan_course_id)

@padawan_course.route('/padawan_courses', methods=['POST'])
def add_padawan_course():
    return controllers.add_padawan_course()

@padawan_course.route('/padawan_courses/<int:padawan_course_id>', methods=['PUT'])
def update_padawan_course(padawan_course_id):
    return controllers.update_padawan_course(padawan_course_id)

@padawan_course.route('/padawan_courses/<int:padawan_course_id>', methods=['DELETE'])
def delete_padawan_course(padawan_course_id):
    return controllers.delete_padawan_course(padawan_course_id)