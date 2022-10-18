from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from src.core.database import db


class Usuario(db.Model):

    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(255))
    mail = db.Column(db.String(255))
    contraseña = db.Column(db.String(255))

    def __init__(self,username,mail,contraseña):
        self.username = username
        self.mail = mail
        self.contraseña = generate_password_hash(contraseña)

    def verify_password(self,contraseña):
        return check_password_hash(self.contraseña,contraseña)
    
