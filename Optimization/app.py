# In app.py


from flask import Flask, jsonify, request
import psycopg2
import os

    
from flask_marshmallow import Marshmallow

from db import *
from util.blueprints import register_blueprints


flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_PORT")

database_password = os.environ.get("DATABASE_PASSWORD")
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

   
ma = Marshmallow(app)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created")


if __name__ == '__main__':
    create_tables()
    app.run(host=flask_host, port=flask_port)