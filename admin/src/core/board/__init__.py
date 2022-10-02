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
    return Configuracion.query.all()

def create_or_update_configuracion(**kwargs):
    configuracion = Configuracion(**kwargs)
    db.session.merge(configuracion)
    db.session.commit()