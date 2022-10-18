from src.core.database import db


class Usuario_tiene_rol(db.Model):

    __tablename__ = "usuario_tiene_rol"
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), primary_key=True)
    rol_id = db.Column(db.Integer, db.ForeignKey("roles.id"), primary_key=True)