from datetime import datetime

from src.core.database import db


class Cuota(db.Model):

    __tablename__ = "cuotas"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nro_cuota = db.Column(db.Integer)
    estado_pago = db.Column(db.Boolean)
    fecha_vencimiento = db.Column(db.DateTime)
    valor_cuota = db.Column(db.Float)
    valor_pago = db.Column(db.Float)
    activo = db.Column(db.Boolean, default=True)
    inscripcion_id = db.Column(db.Integer, db.ForeignKey("inscripciones.id"))
    inscripcion = db.relationship('Inscripcion', back_populates="cuota")
    pago = db.relationship(
        "Pago", secondary="cuotas_pagos", back_populates="cuotas")

    def pagar(self, ammount):
        self.valor_pago = ammount
        if self.payed():
            self.estado_pago = True
        return True

    def payed(self):
        return self.valor_cuota == self.valor_pago
