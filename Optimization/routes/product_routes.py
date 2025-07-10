# In routes > product_routes.py


from flask import Blueprint

import controllers.product_controller

products = Blueprint('products', __name__)

@products.route('/product/<product_id>', methods=['PUT'])
def update_product_by_id(product_id):
    return product_controller.update_product_by_id(product_id)