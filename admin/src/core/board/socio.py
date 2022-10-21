from datetime import datetime

from src.core.database import db


class Socio(db.Model):

    __tablename__ = "socios"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    habilitado = db.Column(db.Boolean, default=True)
    tipo_documento = db.Column(db.String(255))
    numero_documento = db.Column(db.Integer(), unique=True, nullable=False)
    genero = db.Column(db.String(255), nullable=False)
    direccion = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.Integer(), nullable=False)
    activo = db.Column(db.Boolean, default=True)
    disciplina = db.relationship(
    'Inscripcion', back_populates='socio')
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now, nullable=False)

    def __init__(
        self,
        id_usuario,
        tipo_documento,
        numero_documento,
        genero,
        direccion,
        telefono,
    ):
        self.id_usuario = id_usuario
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono


    def update(self, **kwargs):
  
        for key in kwargs:
            setattr(self, key, kwargs[key])    


