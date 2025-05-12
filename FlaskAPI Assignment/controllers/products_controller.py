from flask import jsonify, request

from data import product_records

def read_products():
    if len(product_records) == 0:
        return jsonify({"message": f'Products could not be found.'}), 400
    return jsonify({"message": "product found", "results": product_records}), 200
    
def read_active_products():
    active_products = []
    for product in product_records:
        if product["active"]:
            active_products.append(product)
    if len(active_products) > 0:
        return jsonify({"message": f'Active products found', "result": active_products}, 200)
    return jsonify({"message": f'No active products found'}, 400)
    

def read_product_by_id(id):
    for product in product_records:
        if product['product_id'] == int(id):
            return jsonify({"message": f'Product found.', "result": product}, 200)
    return jsonify({"message": f'No product found.'}, 400)


def create_product():
    data = request.form if request.form else request.get_json
    for product in product_records:
        if product["product_id"] == data["product_id"]:
            return jsonify({"Message": f'Product could not be added'}, 401)
    product = {}
    product['product_id'] = data['product_id']
    product['name'] = data['name']
    product['description'] = data['description']
    product['price'] = data['price']
    product_records.append(product)
    return jsonify({"message": f"Product {product['name']} has been added."}), 200

def update_product(id):
    data = request.form if request.form else request.get_json()
    product = {}
    product['product_id'] = data.get('product_id', id)
    if not product['product_id']:
        return jsonify({"message": 'product_id is required'}), 400
    for record in product_records:
        if record['product_id'] == product['product_id']:
            product = record
    product['name'] = data.get('name', product['name'])
    product['description'] = data.get('description', product['description'])
    product['price'] = data.get('price', product['price'])
    product_records.append(product)
    return jsonify({"message": f"Product {product['name']} has been updated."}), 200

def update_active(id):
    data = request.form if request.form else request.get_json()
    product = {}
    product['product_id'] = data.get('product_id', id)
    if not product['product_id']:
        return jsonify({"message": 'product_id is required'}), 400
    for record in product_records:
        if record['product_id'] == product['product_id']:
            product = record
    if product["active"]:
        product['active'] == False
    else:
        product['active'] == True
    product_records.append(product)
    return jsonify({"message": f"Product {product['name']} active status has been updated."}), 200

def delete_product(id):
    for record in product_records:
        if record['product_id'] == int(id):
            return jsonify({"message": f"Product {record['name']} has been deleted.", "result": record}), 201
    return jsonify({"message"f'Product {id} could not be found'}, 400)