from datetime import datetime

from src.core.database import db


class Configuracion(db.Model):
    """
    Crea la tabla configuracion con las columnas listadas a continuacion.
    """
    __tablename__ = "configuracion"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    elementos_pagina = db.Column(db.Integer)
    estado_pago = db.Column(db.Boolean)
    texto_recibo = db.Column(db.String(255))
    valor_base_cuota = db.Column(db.Float)
    porcentaje_cuota = db.Column(db.Float)
    email_club = db.Column(db.String(255))
    numero_club = db.Column(db.String(50))

    def __init__(
        self,
        elementos_pagina,
        estado_pago,
        texto_recibo,
        valor_base_cuota,
        porcentaje_cuota,
        email_club,
        numero_club,
    ):
        self.elementos_pagina = elementos_pagina
        self.estado_pago = estado_pago
        self.texto_recibo = texto_recibo
        self.valor_base_cuota = valor_base_cuota
        self.porcentaje_cuota = porcentaje_cuota
        self.email_club = email_club
        self.numero_club = numero_club

    def update(self, **kwargs):
        """
        Metodo para actualizar la configuracion mediante keyword arguments
        provenients de un diccionario
        """
        for key in kwargs:
            setattr(self, key, kwargs[key])

    @property
    def serialize_info_club(self):
        """Devuelve email y telefono en formato json"""
        return {
            "email": self.email_club,
            "phone": self.numero_club,
        }
