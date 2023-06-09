from datetime import datetime

from src.core.database import db


class Disciplina(db.Model):

    __tablename__ = "disciplinas"
    id = db.Column(
        db.Integer, db.Sequence("seq_reg_id", start=8, increment=1), primary_key=True
    )
    nombre = db.Column(db.String(50))
    categoria = db.Column(db.String(50))
    entrenador = db.Column(db.String(50))
    dia = db.Column(db.String(50))
    hora = db.Column(db.String(50))
    costo_mensual = db.Column(db.Integer)
    estado = db.Column(db.Boolean)
    socio = db.relationship("Inscripcion", back_populates="disciplina")

    def __init__(self, nombre, categoria, entrenador, dia, hora, costo_mensual,estado):
          self.nombre = nombre
          self.categoria = categoria
          self.entrenador = entrenador
          self.dia = dia
          self.hora = hora
          self.costo_mensual = costo_mensual
          self.estado = estado


    def update(self, **kwargs):
        for key in kwargs:
           setattr(self, key,kwargs[key])

           
   









