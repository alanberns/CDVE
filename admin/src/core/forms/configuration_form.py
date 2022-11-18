from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms import IntegerField
from wtforms import DecimalField
from wtforms import EmailField
from wtforms.validators import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length
from wtforms.validators import NumberRange


class ConfigurationForm(FlaskForm):
    elementos_pagina = IntegerField(
        label=("Elementos por Pagina"),
        validators=[DataRequired(), NumberRange(min=1, max=50)],
    )
    estado_pago = BooleanField(label=("Mostrar tabla de pagos"))
    texto_recibo = StringField(
        label=("Texto para encabezado del recibo"),
        validators=[DataRequired(), Length(max=255)],
    )
    valor_base_cuota = DecimalField(
        label=("Valor base para la cuota"), validators=[DataRequired()]
    )
    porcentaje_cuota = DecimalField(
        label=("Porcentaje de recargo cuotas adeudadas"),
        validators=[DataRequired(), NumberRange(min=0, max=10000)],
    )
    editar = SubmitField(label=("Editar"))
    email_club = EmailField(label=("Email del Club"),)
    numero_club = StringField(label=("Numero telefono del club"))

    def set_from_config(self, configuracion):
        config = configuracion
        self.elementos_pagina.data = config.elementos_pagina
        self.estado_pago.data = config.estado_pago
        self.texto_recibo.data = config.texto_recibo
        self.valor_base_cuota.data = config.valor_base_cuota
        self.porcentaje_cuota.data = config.porcentaje_cuota
        self.email_club.data = config.email_club
        self.numero_club.data = config.numero_club
