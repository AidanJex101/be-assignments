from flask import Blueprint

import controllers 

categories = Blueprint('categories', __name__)

@categories.route('/category', methods=['POST'])
def create_category():
    return controllers.create_category()

@categories.route('/category/<category_id>', methods=['GET'])
def get_category_by_id(category_id):
    return controllers.get_category_by_id(category_id)

@categories.route('/categories', methods=['GET'])
def get_all_categories():
    return controllers.get_all_categories()

@categories.route('/category/<category_id>', methods=['PUT'])
def update_category_by_id(category_id):
    return controllers.update_category_by_id(category_id)

@categories.route('/category/<category_id>', methods=['DELETE'])
def delete_category_by_id(category_id):
    return controllers.delete_category_by_id(category_id)