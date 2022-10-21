#from asyncio.base_futures import _format_callbacks
from flask import Flask
from flask import render_template
from src.helpers import handlers
from src.controllers.disciplinas import disciplina_blueprint
from src.config import config
from src.core.board import database
from src.core.board import seeds



def create_app(env="development",static_folder= "static"):
    app = Flask(__name__,static_folder=static_folder )

    
    app.config.from_object(config[env])

    database.init_app(app)
    
    @app.get("/")
    def home():
        return render_template("home.html") 
    
     
    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()
    
    @app.cli.command(name="seeds")
    def seedsdb():
        seeds.run()

    
    app.register_blueprint(disciplina_blueprint)
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(500, handlers.internal_server_error)


    return app

    
