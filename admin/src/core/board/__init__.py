from src.core.database import db
from src.core.board.usuario import Usuario
from src.core.board.configuracion import Configuracion


def list_usuarios():
    return Usuario.query.all()

def create_usuario(**kwargs):
    usuario = Usuario(**kwargs)
    db.session.add(usuario)
    db.session.commit()

def list_configuracion():
    """
    Lista los datos de la configuracion, devuelve una sola tupla
    """
    return Configuracion.query.all()

def update_configuracion(**kwargs):
    """
    Actualiza los datos de la configuracion
    """
    configuracion = Configuracion.query.first()
    configuracion.update(**kwargs)
    db.session.merge(configuracion)
    db.session.commit()