

from flask import jsonify, request

from db import db
from models.product import Products, product_schema, products_schema
from models.category import Categories
from util.reflection import populate_object

# CREATE

def create_product():
    post_data = request.form if request.form else request.get_json()

    new_product = Products.new_product_obj()
    populate_object(new_product, data)

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "product created", "result": product_schema.dump(new_product)}), 201

# READ



# UPDATE

def update_product_by_id(product_id):
    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()
    post_data = request.form if request.form else request.get_json()

    if product_query:
        populate_object(product_query, post_data)

        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify({"message": "unable to update record"}), 400

        return jsonify({"message": "products found", "results": product_schema.dump(query)}), 200

# DELETE