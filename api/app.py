from flask import Flask
from persistent.db_utils import db
from api.routes.blacklist_route import blacklist_bp
from tests.testing_config import TestingConfig
from utils.config import Config


def create_app(config=Config):
    app = Flask(__name__)

    print(f"Ejecutando ambiente de Test: {config.TESTING}")

    app.config.from_object(config if not config.TESTING else TestingConfig)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Registro de Blueprints
    app.register_blueprint(blacklist_bp, url_prefix="/api/blacklists")

    @app.route("/")
    def home():
        return "Blacklist API"

    return app
