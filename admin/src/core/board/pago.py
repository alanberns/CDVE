from src.core.database import db


class Pago(db.Model):

    __tablename__ = "pagos"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    fecha = db.Column(db.DateTime)
    monto = db.Column(db.Float)
    cuotas = db.relationship("Cuota", secondary="cuotas_pagos", back_populates="pago")
    comprobante = db.Column(db.String(255))

    @property
    def serialize(self):
        """Devuelve instancias de Pago en formato json"""
        return {
            "id": self.id,
            "fecha": self.fecha,
            "monto": self.monto,
            "cuotas": [cuota.nro_cuota for cuota in self.cuotas],
            "comprobante": self.comprobante,
        }


cuotas_pagos = db.Table(
    "cuotas_pagos",
    db.Column("pago_id", db.Integer, db.ForeignKey("pagos.id"), primary_key=True),
    db.Column("cuota_id", db.Integer, db.ForeignKey("cuotas.id"), primary_key=True),
)
