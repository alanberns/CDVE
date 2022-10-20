#from datetime import datetime

from src.core.board.database import db

class Issue(db.Model):

     __tablename__ = "issues"
     id = db.Column(db.Integer, primary_key= True, unique= True)
     nombre = db.Column(db.String(50))
     categoria = db.Column(db.String(50))
     entrenador = db.Column(db.String(50))
     dia = db.Column(db.String(50))
     hora = db.Column(db.String(50))
     costo_mensual = db.Column(db.Integer)
     activo = db.Column(db.String(50))







