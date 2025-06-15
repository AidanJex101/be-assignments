from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__all__ = ['db', 'init_db']

db = SQLAlchemy()

def init_db(app=None, db=None):
    if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
        db.init_app(app)
    else:
        raise ValueError("app must be a Flask instance and db must be a SQLAlchemy instance")