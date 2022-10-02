from datetime import datetime

from src.core.database import db


class Configuracion(db.Model):

    __tablename__ = "configuracion"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    elementos_pagina = db.Column(db.Integer)
    estado_pago = db.Column(db.Boolean)
    estado_info_contactos = db.Column(db.Boolean)
    texto_recibo = db.Column(db.String(255))
    valor_base_cuota = db.Column(db.Integer)
    porcentaje_cuota = db.Column(db.Float)