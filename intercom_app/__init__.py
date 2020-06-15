from flask import Flask
import configuration
from werkzeug.utils import import_string


def create_app(config):
    app = Flask(__name__)
    cfg = import_string(config)()
    app.config.from_object(cfg)

    with app.app_context():
        from intercom_app import routes
        app.register_blueprint(routes.distance_calculator)
        return app
