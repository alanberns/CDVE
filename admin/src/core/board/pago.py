from src.core.database import db


class Pago(db.Model):

    __tablename__ = "pagos"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    fecha = db.Column(db.DateTime)
    monto = db.Column(db.Float)
    cuotas = db.relationship("Cuota", secondary="cuotas_pagos", back_populates="pago")


cuotas_pagos = db.Table(
    "cuotas_pagos",
    db.Column("pago_id", db.Integer, db.ForeignKey("pagos.id"), primary_key=True),
    db.Column("cuota_id", db.Integer, db.ForeignKey("cuotas.id"), primary_key=True),
)
