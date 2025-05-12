from flask import Blueprint

from controllers import products_controller

product = Blueprint('product', __name__)

@product.route('/product/<product_id>', methods=["PUT"])
def update_product(product_id):
    return products_controller.update_product(product_id)

@product.route('/product/activity/<product_id>', methods=["PUT"])
def update_active(product_id):
    return products_controller.update_active(product_id)