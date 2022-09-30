from flask import Flask
from flask import render_template

from src.web.config import config
from src.web.helpers import handlers


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    @app.get("/")
    def home():
        return render_template("home.html")

    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)

    return app