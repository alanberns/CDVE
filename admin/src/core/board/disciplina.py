# from datetime import datetime

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
    estado = db.Column(db.String(50))
    socio = db.relationship("Inscripcion", back_populates="disciplina")
