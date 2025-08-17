from flask import Blueprint

import controllers

auth = Blueprint('auth', __name__)

@auth.route('/user/auth', methods=['POST'])
def authenticate_user():
    return controllers.authenticate_user()