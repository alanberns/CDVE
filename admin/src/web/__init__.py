from unicodedata import name
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
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
from src.web.controllers.perfil import perfil_blueprint
from src.web.controllers.disciplinas import disciplina_blueprint
from src.web.controllers.api import api_blueprint
from flask_wtf.csrf import CSRFProtect
# from flask_cors import CORS
from src.web.helpers.auth import login_required
from src.web.helpers.percentage import float_to_percentage


def create_app(env="development", static_folder="static"):
    app = Flask(__name__, instance_relative_config=True,
                static_folder=static_folder)
    app.config.from_object(config[env])
    #CORS(app)
    #app.config['CORS_HEADERS'] = 'Content-Type'
    csrf = CSRFProtect()
    csrf.init_app(app)
    csrf.exempt(api_blueprint)
    database.init_app(app)

    @app.get("/")
    def entry():
        database.reset_db()
        seeds.run()
        return redirect(url_for('auth.login'))

    @app.get("/home")
    @login_required
    def home():
        return render_template("home.html")

    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(configuracion_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(socio_blueprint)
    app.register_blueprint(pago_blueprint)
    app.register_blueprint(perfil_blueprint)
    app.register_blueprint(disciplina_blueprint)
    app.register_blueprint(api_blueprint)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(401, handlers.unauthorized)
    app.register_error_handler(500, handlers.internal_server_error)
    app.register_error_handler(403, handlers.forbbiden)
    app.register_error_handler(400, handlers.bad_request)

    app.jinja_env.globals.update(is_authenticated=auth.is_authenticated)
    app.jinja_env.globals.update(has_permission=auth.has_permission)
    app.jinja_env.globals.update(float_to_percentage=float_to_percentage)

    @app.cli.command(name="seeds")
    def seeds_configuracion():
        database.init_app(app)
        seeds.run()
        print("Datos creados correctamente")

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    return app
