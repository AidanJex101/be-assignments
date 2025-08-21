# In routes > product_routes.py


from flask import Blueprint

import controllers 

products = Blueprint('products', __name__)

@products.route('/product', methods=['POST'])
def create_product():
    return controllers.create_product()

@products.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return controllers.get_product_by_id(product_id)

@products.route('/products', methods=['GET'])
def get_all_products():
    return controllers.get_all_products()

@products.route('/product/<product_id>', methods=['PUT'])
def update_product_by_id(product_id):
    return controllers.update_product_by_id(product_id)

@products.route('/product/active', methods=['GET'])
def get_active_products():
    return controllers.get_active_products()

@products.route('/products/company/<company_id>', methods=['GET'])
def get_products_by_company(company_id):
    return controllers.get_products_by_company(company_id)

@products.route('/product', methods=['DELETE'])
def delete_product(product_id):
    return controllers.delete_product_by_id(product_id)