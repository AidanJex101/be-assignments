import routes


def register_blueprints(app):
    app.register_blueprint(routes.orgs)
    app.register_blueprint(routes.users)
    app.register_blueprint(routes.auth)
    