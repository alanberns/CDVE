from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    IntegerField,
    DecimalField,
)
from wtforms.validators import (
    ValidationError,
    DataRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
)


class ConfigurationForm(FlaskForm):
    elementos_pagina = IntegerField(
        label=("Elementos por Pagina"),
        validators=[DataRequired(), NumberRange(min=1, max=50)],
    )
    estado_pago = BooleanField(label=("Mostrar tabla de pagos"))
    estado_info_contactos = BooleanField(label=("Mostrar Info de contactos"))
    texto_recibo = StringField(
        label=("Texto para encabezado del recibo"),
        validators=[DataRequired(), Length(max=255)],
    )
    valor_base_cuota = DecimalField(
        label=("Valor base para la cuota"), validators=[DataRequired()]
    )
    porcentaje_cuota = DecimalField(
        label=("Porcentaje de recargo cuotas adeudadas"),
        validators=[DataRequired(), NumberRange(min=0, max=1)],
    )
    editar = SubmitField(label=("Editar"))

    def set_from_config(self, configuracion):
        config = configuracion
        self.elementos_pagina.data = config.elementos_pagina
        self.estado_pago.data = config.estado_pago
        self.estado_info_contactos.data = config.estado_info_contactos
        self.texto_recibo.data = config.texto_recibo
        self.valor_base_cuota.data = config.valor_base_cuota
        self.porcentaje_cuota.data = config.porcentaje_cuota
