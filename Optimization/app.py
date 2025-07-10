# In app.py


from flask import Flask, jsonify, request
import psycopg2
import os

    # Imported Marshmallow class object from flask_marshmallow module
from flask_marshmallow import Marshmallow

from db import *
from util.blueprints import register_blueprints
from util.reflection import populate_object
    # Updated import from models to include the schema pairs
from models.company import Companies, company_schema, companies_schema
from models.categories import Categories, category_schema, categories_schema
from models.product import Products, product_schema, products_schema

flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_PORT")

database_scheme = os.environ.get("DATABASE_SCHEME")
database_user = os.environ.get("DATABASE_USER")
database_address = os.environ.get("DATABASE_ADDRESS")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)

register_blueprints(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f'{database_scheme}{database_user}:{database_password}@{database_address}:{database_port}/{database_name}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)

    # Instantiated Marshmallow class object
ma = Marshmallow(app)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created")


if __name__ == '__main__':
    create_tables()
    app.run(host=flask_host, port=flask_port)