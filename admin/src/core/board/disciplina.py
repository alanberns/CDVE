#from datetime import datetime

from src.core.board.database import db

class Disciplina(db.Model):

     __tablename__ = "disciplinas"
     id = db.Column(db.Integer, db.Sequence("seq_reg_id", start=8, increment=1 ), primary_key= True)
     nombre = db.Column(db.String(50))
     categoria = db.Column(db.String(50))
     entrenador = db.Column(db.String(50))
     dia = db.Column(db.String(50))
     hora = db.Column(db.String(50))
     costo_mensual = (db.Column(db.Integer))
     estado = (db.Column(db.Boolean))

     def __init__(self, nombre, categoria, entrenador, dia, hora, costo_mensual):
          self.nombre = nombre
          self.categoria = categoria
          self.entrenador = entrenador
          self.dia = dia
          self.hora = hora
          self.costo_mensual = costo_mensual

     def to_JSON(self):
          return { 
          'nombre': self.nombre,
          'categoria': self.categoria,
          'entrenador': self.entrenador,
          'dia': self.dia,
          'hora': self.hora,
          'costo_mensual': self.costo_mensual
          }














