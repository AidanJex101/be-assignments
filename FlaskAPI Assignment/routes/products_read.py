from flask import Blueprint

from controllers import products_controller

product = Blueprint('product', __name__)

@product.route('/products', methods=["GET"])
def read_products():
    return products_controller.read_products()

@product.route('/products/active', methods=["GET"])
def read_active_products():
    return products_controller.read_active_products()

@product.route('/products/<product_id>', methods=["GET"])
def read_product_by_id(product_id):
    return products_controller.read_product_by_id(product_id)