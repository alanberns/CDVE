from datetime import datetime

from src.core.database import db


class Socio(db.Model):

    __tablename__ = "socios"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))


    habilitado = db.Column(db.Boolean, default=True)
    tipo_documento = db.Column(db.String(255))
    numero_documento = db.Column(db.Integer())
    genero = db.Column(db.String(255))
    numero_socio = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.Integer())
    email = db.Column(db.String(255))
    activo = db.Column(db.Boolean, default=True)

    def __init__(
        self,
        id_usuario,
        tipo_documento,
        numero_documento,
        genero,
        numero_socio,
        direccion,
        telefono,
        email,
    ):
        self.id_usuario = id_usuario
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.genero = genero
        self.numero_socio = numero_socio
        self.direccion = direccion
        self.telefono = telefono
        self.email = email


    def update(self, **kwargs):
  
        for key in kwargs:
            setattr(self, key, kwargs[key])    # falta relacion con cuota y disciplina
