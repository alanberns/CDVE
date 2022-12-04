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
    inscripcion = db.relationship("Inscripcion", back_populates="cuota")
    pago = db.relationship("Pago", secondary="cuotas_pagos", back_populates="cuotas")

    def pagar(self):
        self.valor_pago = self.valor_cuota
        self.estado_pago = True
        return self.estado_pago

    def payed(self):
        return self.valor_cuota == self.valor_pago

    @property
    def serialize(self):
        """Devuelve instancias de Pago en formato json"""
        return {
            "id": self.id,
            "fecha": self.fecha_vencimiento,
            "monto": self.valor_cuota,
            "nro_cuota": self.nro_cuota,
            "estado": self.estado_pago,
        }
