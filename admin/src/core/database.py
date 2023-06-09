from flask_sqlalchemy import SQLAlchemy

"""
Inicializacion de la BD
"""
db = SQLAlchemy()

"Enlazar la app Flask con la base datos que acabamos de crear"


def init_app(app):

    db.init_app(app)
    config_db(app)


def reset_db():
    """
    Borra todas las tablas y luego las vuelve a crear
    """
    print("Borrando base de datos")
    db.drop_all()
    print("Volviendo a crear las tablas")
    db.create_all()


def config_db(app):
    @app.before_first_request
    def init_database():
        db.create_all()

    # @app.teardown_request
    # def close_session(exception=None):
    #     db.session.remove()
