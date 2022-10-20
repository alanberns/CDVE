from unicodedata import name
from flask import Flask
from flask import render_template

from src.core import database
from src.web.config import config
from src.web.helpers import auth
from src.web.helpers import handlers
from src.core import seeds
from src.web.controllers.usuarios import usuario_blueprint
from src.web.controllers.configuracion import configuracion_blueprint
from src.web.controllers.auth import auth_blueprint
from src.web.controllers.socios import socio_blueprint
from src.web.controllers.pagos import pago_blueprint
from flask_wtf.csrf import CSRFProtect


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
#    csrf = CSRFProtect()
#    csrf.init_app(app)
    database.init_app(app)

    @app.get("/")
    def home():
        return render_template("home.html")

    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(configuracion_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(socio_blueprint)
    app.register_blueprint(pago_blueprint)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(401, handlers.unauthorized)
    app.register_error_handler(500, handlers.internal_server_error)

    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)

    @app.cli.command(name="seeds")
    def seeds_configuracion():
        database.init_app(app)
        seeds.run()
        print("Datos creados correctamente")

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    return app
