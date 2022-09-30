from datetime import datetime

from src.core.database import db


class Usuario(db.Model):

    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(255))
    