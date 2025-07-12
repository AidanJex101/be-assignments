from flask import Flask, jsonify, request
import psycopg2
import os

from db import *
from models.company import Companies
from models.category import Categories
from models.product import Products
from models.product_category_xref import products_categories_association_table
from models.warranty import Warranties


app = Flask(__name__)

flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_POST")

database_scheme = os.environ.get("DATABASE_SCHEME")
database_user = os.environ.get("DATABASE_USER")
database_address = os.environ.get("DATABASE_ADDRESS")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")
database_password = os.environ.get("DATABASE_PASSWORD")

app.config['SQLALCHEMY_DATABASE_URI'] = f'{database_scheme}{database_user}:{database_password}@{database_address}:{database_port}/{database_name}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")

create_tables()

if __name__ == '__main__':
    app.run(host=flask_host, port=flask_port)


@app.route('/company', methods=['POST'])
def add_company():
    post_data = request.form if request.form else request.json

    fields = ['company_name']
    required_fields = ['company_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)

        if field_data in required_fields and not field_data:
            return jsonify({"message": f'{field} is required'}), 400

        values[field] = field_data

    new_company = Companies(values['company_name'])

    try:
        db.session.add(new_company)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    query = db.session.query(Companies).filter(Companies.company_name == values['company_name']).first()

    company = {
        "company_id": query.company_id,
        "company_name": query.company_name
    }

    return jsonify({"message": "company created", "result": company}), 201

@app.route('/companies')
def get_all_companies():
    query = db.session.query(Companies).all()

    print(query)

    company_list = []

    for company in query:
        company_dict = {
            'company_id': company.company_id,
            'company_name': company.company_name
        }

        company_list.append(company_dict)

    return jsonify({"message": "companies found", "results": company_list}), 200

@app.route('/company/<company_id>', methods=["GET"])
def get_company_by_id(company_id):
    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()
    if not query:
        return jsonify({"message": f"company does not exist"}), 400

    company = {
        'company_id': query.product_id,
        'company_name': query.product_name,
    }

    return jsonify({"message": "company found", "results": company}), 200

@app.route('/company/<company_id>', methods=['PUT'])
def update_company_by_id(company_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    query.company_name = post_data.get("company_name", query.company_name)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400

    return jsonify({"message": "product updated", "results": query}), 200

@app.route('/company/delete/<company_id>', methods=['DELETE'])
def delete_company(company_id):
    query = db.session.query(Companies).filter(Companies.company_id == company_id).first()

    if not query:
        return jsonify({"message": f"Company by id {company_id} does not exist"}), 400    

    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "company deleted", "results": query}), 200

@Products.route('/product/<product_id>')
def get_product_by_id(product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()
    if not query:
        return jsonify({"message": f"product does not exist"}), 400

    print(query)

    company_dict = {
        'company_id': query.company.company_id,
        'company_name': query.company.company_name
    }

    if query.warranty:
        warranty_dict = {
            'warranty_id': query.warranty.warranty_id,
            'warranty_months': query.warranty.warranty_months
        }
    else:
        warranty_dict = {}

    product = {
        'product_id': query.product_id,
        'product_name': query.product_name,
        'description': query.description,
        'price': query.price,
        'active': query.active,
        'company': company_dict,
        'warranty': warranty_dict
    }

    return jsonify({"message": "product found", "results": product}), 200

@Products.route('/product/category', methods=['POST'])
def create_product_category():
    post_data = request.form if request.form else request.get_json()

    fields = ['product_id', 'category_id']
    required_fields = ['product_id', 'category_id']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({"message": f'{field} is required'}), 400

        values[field] = field_data

    product_query = db.session.query(Products).filter(Products.product_id == values['product_id']).first()
    category_query = db.session.query(Categories).filter(Categories.category_id == values['category_id']).first()

    if product_query and category_query:
        product_query.categories.append(category_query)

        db.session.commit()

        categories_list = []

        for category in product_query.categories:
            categories_list.append({
                "category_id": category.category_id,
                "category_name": category.category_name
            })

        company_dict = {
            "company_id": product_query.company.company_id,
            "company_name": product_query.company.company_name
        }

        product = {
            'product_id': product_query.product_id,
            'product_name': product_query.product_name,
            'description': product_query.description,
            'price': product_query.price,
            'active': product_query.active,
            'company': company_dict,
            'categories': categories_list,
        }

    return jsonify({"message": "category added to product", "result": product}), 201


@Products.route('/product/<product_id>', methods=['GET'])
def get_product(product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()
    if not query:
        return jsonify({"message": f"product does not exist"}), 400

    categories_list = []

    for category in query.categories:
        categories_list.append({
            "category_id": category.category_id,
            "category_name": category.category_name
        })

    company_dict = {
        'company_id': query.companies.company_id,
        'company_name': query.companies.company_name
    }

    if query.warranty:
        warranty_dict = {
            'warranty_id': query.warranty.warranty_id,
            'warranty_months': query.warranty.warranty_months
        }
    else:
        warranty_dict = {}

    product = {
        'product_id': query.product_id,
        'product_name': query.product_name,
        'description': query.description,
        'price': query.price,
        'active': query.active,
        'company': company_dict,
        'warranty': warranty_dict,
        'categories': categories_list,
    }

    return jsonify({"message": "product found", "result": product}), 200

@app.route('/product', methods=['POST'])
def add_company():
    post_data = request.form if request.form else request.json

    fields = ['product_name', 'description', 'price', 'active', 'company', 'warranty', 'categories']
    required_fields = ['product_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)

        if field_data in required_fields and not field_data:
            return jsonify({"message": f'{field} is required'}), 400

        values[field] = field_data

    new_product = Products(values['product_name'])

    try:
        db.session.add(new_product)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    query = db.session.query(Products).filter(Products.product_name == values['product_name']).first()

    company_dict = {
        'company_id': query.companies.company_id,
        'company_name': query.companies.company_name
    }

    categories_list = []

    for category in query.categories:
        categories_list.append({
            "category_id": category.category_id,
            "category_name": category.category_name
        })

    product = {
            'product_id': query.product_id,
            'product_name': query.product_name,
            'description': query.description,
            'price': query.price,
            'active': query.active,
            'company': company_dict,
            'categories': categories_list,
        }

    return jsonify({"message": "product created", "result": product}), 201


@app.route('/products')
def get_all_companies():
    query = db.session.query(Products).all()

    print(query)

    product_list = []

    for product in query:
        product_dict = {
            'product_id': product.product_id,
            'product_name': product.product_name,
            'description': product.description,
            'price': product.price,
            'company': product.company, 
            'categories': product.categories
        }

        product_list.append(product_dict)

    return jsonify({"message": "companies found", "results": product_list}), 200


@app.route('/product/<product_id>', methods=['PUT'])
def update_product_by_id(product_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Products).filter(Products.product_id == product_id).first()

    query.product_name = post_data.get("product_name", query.product_name)
    query.description = post_data.get("description", query.product_name)
    query.price = post_data.get("price", query.price)
    query.company = post_data.get("company", query.company)
    query.categories = post_data.get("categories", query.categories)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400

    return jsonify({"message": "product updated", "results": query}), 200

@app.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    query = db.session.query(Products).filter(Products.product_id == product_id).first()

    if not query:
        return jsonify({"message": f"product by id {product_id} does not exist"}), 400    

    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "product deleted", "results": query}), 200

@app.route('/category', methods=['POST'])
def add_category():
    post_data = request.form if request.form else request.get_json()

    fields = ['category_name']
    required_fields = ['category_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required_fields and not field_data:
            return jsonify({"message": f'{field} is required'}), 400

        values[field] = field_data

    new_category = Categories(values['category_name'])

    try:
        db.session.add(new_category)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    query = db.session.query(Categories).filter(Categories.category_name == values['category_name']).first()

    values['category_id'] = query.category_id

    return jsonify({"message": "category created", "result": values}), 201

@app.route('/categories')
def get_all_companies():
    query = db.session.query(Categories).all()

    print(query)

    category_list = []

    for category in query:
        category_dict = {
            'category_id': category.category_id,
            'category_name': category.category_name
        }

        category_list.append(category_dict)

    return jsonify({"message": "categories found", "results": category_list}), 200


@app.route('/category/<category_id>', methods=['PUT'])
def update_category_by_id(category_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    query.category_name = post_data.get("category_name", query.category_name)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400

    return jsonify({"message": "category updated", "results": query}), 200

@app.route('/category/delete/<category_id>', methods=['DELETE'])
def delete_category(category_id):
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    if not query:
        return jsonify({"message": f"category by id {category_id} does not exist"}), 400    

    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "category deleted", "results": query}), 200


@app.route('/warranty', methods=['POST'])
def add_warranty():
    post_data = request.form if request.form else request.json

    fields = ['warranty_months', 'product_id']
    required_fields = ['warranty_months', 'product_id']

    values = {}

    for field in fields:
        field_data = post_data.get(field)

        if field_data in required_fields and not field_data:
            return jsonify({"message": f'{field} is required'}), 400

        values[field] = field_data

    new_company = Warranties(values['warranty_months'])

    try:
        db.session.add(new_company)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400

    query = db.session.query(Warranties).filter(Warranties.warranty_months == values['warranty_months']).first()

    warranty = {
        "warranty_id": query.warranty_id,
        "warranty_months": query.warranty_months,
        "product_id": query.product_id
    }

    return jsonify({"message": "warranty created", "result": warranty}), 201

@app.route('/warranty/<warranty_id>', methods=["GET"])
def get_warranty_by_id(warranty_id):
    query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()
    if not query:
        return jsonify({"message": f"warranty does not exist"}), 400

    warranty = {
        'warranty_id': query.warranty_id,
        'warranty_months': query.warranty_months,
        'product_id': query.product_id
    }

    return jsonify({"message": "warranty found", "results": warranty}), 200


@app.route('/warranty/<warranty_id>', methods=['PUT'])
def update_warranty_by_id(warranty_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    query.warranty_months = post_data.get("warranty_months", query.warranty_months)
    query.product_id = post_data.get("product_id", query.product_id)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400

    return jsonify({"message": "product updated", "results": query}), 200

@app.route('/warranty/delete/<warranty_id>', methods=['DELETE'])
def delete_warranty(warranty_id):
    query = db.session.query(Warranties).filter(Warranties.warranty_id == warranty_id).first()

    if not query:
        return jsonify({"message": f"warranty by id {warranty_id} does not exist"}), 400    

    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400

    return jsonify({"message": "warranty deleted", "results": query}), 200