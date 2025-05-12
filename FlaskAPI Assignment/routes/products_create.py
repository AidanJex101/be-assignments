from flask import Blueprint

from controllers import products_controller

product = Blueprint('product', __name__)

@product.route('/product', methods=["POST"])
def create_product():
    return products_controller.create_product()