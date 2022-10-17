from datetime import datetime

from src.core.database import db


class Cuota(db.Model):

    __tablename__ = "cuota"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    # id_inscripcion = db.Column(db.Integer) FK
    estado_pago = db.Column(db.Boolean)
    fecha_vencimiento = db.Column(db.Datetime)
    fecha_pago = db.Column(db.Datetime)
    valor_cuota = db.Column(db.Float)
    valor_pago = db.Column(db.Float)
