from flask import Flask, request, jsonify
import psycopg2
import os

from db import *
import routes
from models.company import Company

flask_host = os.environ.get('FLASK_HOST')
flask_port = os.environ.get('FLASK_PORT')

database_scheme = os.environ.get('DATABASE_SCHEME')
database_user = os.environ.get('DATABASE_USER')
database_address = os.environ.get('DATABASE_ADDRESS')
database_password = os.environ.get('DATABASE_PASSWORD')
database_name = os.environ.get('DATABASE_NAME')
database_port = os.environ.get('DATABASE_PORT')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'{database_scheme}{database_user}:{database_password}@{database_address}:{database_port}/{database_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app, db)

app.register_blueprint(routes.company)

def create_tables():
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully.")

if __name__ == '__main__':
    app.run(host=flask_host, port=flask_port)