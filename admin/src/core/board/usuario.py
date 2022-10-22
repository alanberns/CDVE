from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from src.core.database import db


class Usuario(db.Model):

    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    activo = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(),
                           onupdate=datetime.now, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    roles = db.relationship("Rol", secondary="usuario_tiene_rol")
    socio = db.relationship('Socio', backref='usuario')

    def __init__(self, username, email, password, created_at, updated_at, first_name, last_name):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.created_at = created_at
        self.updated_at = updated_at
        self.first_name = first_name
        self.last_name = last_name

    def update(self, **kwargs):
        """
        Metodo para actualizar la configuracion mediante keyword arguments
        provenients de un diccionario
        """
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def verify_password(self, password):
        return check_password_hash(self.password, password)
