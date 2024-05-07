from flask import Flask


def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .example import routes

        app.register_blueprint(routes.example_bp)

        return app
