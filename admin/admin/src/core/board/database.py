from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def init_app(app):
    """
    Inicializacion de la BD
    """
    db.init_app(app)
    config_db(app)

#se crean las tablas, si las tablas exiten, no las crea, y si no existe las agrega
def config_db(app):
    @app.before_first_request
    def init_database():
        db.create_all()


    # @app.teardown_request
    # def close_session(exception=None):
    #     db.session.remove()

def reset_db():
    """
    Borra todas las tablas y luego las vuelve a crear
    """
    print("Borrando base de datos")
    db.drop_all()
    print("Volviendo a crear las tablas")
    db.create_all()
    print("Done!")



