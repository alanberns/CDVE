from src.core.database import db
from src.core.board.usuario import Usuario


def list_usuarios():
    return Usuario.query.all()

def create_usuario(**kwargs):
    usuario = Usuario(**kwargs)
    db.session.add(usuario)
    db.session.commit()