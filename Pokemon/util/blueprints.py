import routes


def register_blueprints(app):
    app.register_blueprint(routes.users)
    app.register_blueprint(routes.auth)
    app.register_blueprint(routes.trainer)
    app.register_blueprint(routes.pokemon)
    app.register_blueprint(routes.PokemonBattle)
    app.register_blueprint(routes.battle)
    app.register_blueprint(routes.stats)
    app.register_blueprint(routes.location)

    return app