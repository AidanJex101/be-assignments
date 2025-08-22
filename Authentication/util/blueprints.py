
from routes.product_routes import products
from routes.category_routes import categories
from routes.company_routes import companies
from routes.warranty_routes import warranties
from routes.auth_routes import auth
from routes.user_routes import users


def register_blueprints(app):
    app.register_blueprint(products)
    app.register_blueprint(categories)
    app.register_blueprint(companies)
    app.register_blueprint(warranties)
    app.register_blueprint(auth)
    app.register_blueprint(users)
