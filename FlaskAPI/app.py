from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route('/string')
# def respond_string():
#     return 'Here is a response with a python string'

# @app.route('/html')
# def respond_html():
#     return '<h1 align="center" style="color: blue;">Here is a response with HTML</h1>'

# # @app.route('/json')
# # def respond_json():
# #     def addition():
# #         count = 1 + 1
# #         return count
# #     sum = addition()
# #     return jsonify({"message": f'Here is a response with text and another return {sum}'})

# @app.route('/json/<number>')
# def respond_json(number):
#     return jsonify({"message": f'Here is a response with the sent slug {number}'})

# product_records = [
#     {
#         "product_id": 1,
#         "name": "Hasbro Gaming Clue Game",
#         "description": "One murder... 6 suspects...",
#         "price": 9.95
#     },
#     {
#         "product_id": 2,
#         "name": "Monopoly Board Game The Classic Edition, 2-8 players",
#         "description" : "Relive the Monopoly experiences...", 
#         "price": 35.50
#     }
# ]

# @app.route('/product/<product_id>')
# def get_products_by_id(product_id):
#     for product in product_records:
#         if product['product_id'] == int(product_id):
#             return jsonify({"message": "products found", "results": product}, 200)
#     return jsonify({"message": f'Product with id {product_id} not found.'}, 404)


@app.route('/whatsmymethod', methods=["POST"])
def create_method():
    return jsonify({"message": "POST: You have created a record"}) , 201

@app.route('/whatsmymethod', methods=["GET"])
def get_method():
    return jsonify({"message": "GET: Here is your record to read"}), 200

@app.route('/whatsmymethod', methods=["PUT"])
def update_method():
    return jsonify({"message": "PUT: You have setup new values for a record"}), 200


@app.route('/whatsmymethod', methods=["PATCH"])
def patch_method():
    return jsonify({"message": "PATCH: You made a change to one field in a record"}), 200


@app.route('/whatsmymethod', methods=["DELETE"])
def delete_method():
    return jsonify({"message": "No DELETE. Use deactivate instead"}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8086')