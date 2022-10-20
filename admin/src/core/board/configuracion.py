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

    def __init__(self, elementos_pagina,estado_pago,estado_info_contactos,texto_recibo,valor_base_cuota,porcentaje_cuota):
        self.elementos_pagina = elementos_pagina
        self.estado_pago = estado_pago
        self.estado_info_contactos = estado_info_contactos
        self.texto_recibo = texto_recibo
        self.valor_base_cuota = valor_base_cuota
        self.porcentaje_cuota = porcentaje_cuota

    def update(self,**kwargs):
        """
        Metodo para actualizar la configuracion mediante keyword arguments
        provenients de un diccionario
        """
        for key in kwargs:
            setattr(self, key, kwargs[key])

