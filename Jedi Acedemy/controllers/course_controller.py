from flask import jsonify, request

from db import db
from models.course import Courses, courses_schema, course_schema
from models.master import Masters, masters_schema, master_schema
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate 


def get_courses():
    