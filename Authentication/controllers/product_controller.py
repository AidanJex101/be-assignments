

from flask import jsonify, request

from db import db
from models.product import Products, product_schema, products_schema
from models.category import Categories
from util.reflection import populate_object
from lib.authenticate import authenticate_return_auth, authenticate

# CREATE

@authenticate_return_auth
def create_product():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    post_data = request.form if request.form else request.get_json()

    new_product = Products.new_product_obj()
    populate_object(new_product, post_data)

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    return jsonify({"message": "product created", "result": product_schema.dump(new_product)}), 201

# READ

@authenticate_return_auth
def get_all_products():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    query = db.session.query(Products).all()
    if not query:
        return jsonify({"message": "no products found"}), 404

    return jsonify({"message": "products found", "results": products_schema.dump(query)}), 200


@authenticate_return_auth
def get_product_by_id(product_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    query = db.session.query(Products).filter(Products.product_id == product_id).first()
    if not query:
        return jsonify({"message": "product not found"}), 404

    return jsonify({"message": "product found", "result": product_schema.dump(query)}), 200

@authenticate_return_auth
def get_active_products():

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    query = db.session.query(Products).filter(Products.active == True).all()
    if not query:
        return jsonify({"message": "no active products found"}), 404

    return jsonify({"message": "active products found", "results": products_schema.dump(query)}), 200


@authenticate_return_auth
def get_products_by_company(company_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    query = db.session.query(Products).filter(Products.company_id == company_id).all()
    if not query:
        return jsonify({"message": "no products found for this company"}), 404

    return jsonify({"message": "products found for this company", "results": products_schema.dump(query)}), 200

# UPDATE

@authenticate_return_auth
def update_product_by_id(product_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401


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

@authenticate_return_auth
def delete_product_by_id(product_id):

    auth_info = request.auth_info
    if auth_info.user.role != "superadmin":
        return jsonify({"message": "unauthorized"}), 401

    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not product_query:
        return jsonify({"message": "product not found"}), 404

    try:
        db.session.delete(product_query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "product deleted"}), 200