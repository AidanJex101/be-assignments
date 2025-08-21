from flask import jsonify, request

from db import db
from models.product_category_xref import ProductCategoryXref, product_category_xref_schema, product_category_xrefs_schema
from util.reflection import populate_object

def create_product_category_xref():
    post_data = request.form if request.form else request.get_json()

    new_xref = ProductCategoryXref.new_xref_obj()
    populate_object(new_xref, post_data)

    try:
        db.session.add(new_xref)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "product-category xref created", "result": product_category_xref_schema.dump(new_xref)}), 201

def add_category_to_product(product_id, category_id):
    post_data = request.form if request.form else request.get_json()

    new_xref = ProductCategoryXref(product_id=product_id, category_id=category_id)
    populate_object(new_xref, post_data)

    try:
        db.session.add(new_xref)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "category added to product", "result": product_category_xref_schema.dump(new_xref)}), 201