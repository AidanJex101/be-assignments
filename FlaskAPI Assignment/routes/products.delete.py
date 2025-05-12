from flask import Blueprint

from controllers import products_controller

product = Blueprint('product', __name__)

@product.route('/product/delete/<product_id>', methods=["DELETE"])
def delete_product(product_id):
    return products_controller.delete_product(product_id)