from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import DateTimeField
from wtforms import HiddenField
from wtforms import FieldList
from wtforms import FormField
from wtforms import BooleanField
from wtforms import DecimalField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms import StringField
from wtforms.validators import ValidationError, DataRequired, \
    Email, EqualTo, Length, NumberRange


class PagoForm(FlaskForm):
    id = HiddenField('id')
    fecha_vencimiento = DateTimeField(label=('Fecha Vencimiento'))
    valor_cuota = DecimalField(
        label=('Valor cuota'))
    estado_pago = BooleanField(label=('Estado de Pago'))
    check = BooleanField()


class EditForm(FlaskForm):
    items = FieldList(FormField(PagoForm))
    pagar = SubmitField(label=('Realizar Pago'))


class PagoSearchForm(FlaskForm):
    texto_busqueda = StringField("Buscar")
    select_busqueda = SelectField(
        "Mostrar",
        choices=((0, "Nro de Socio"), (1, "Apellido")), coerce=int)
    buscar = SubmitField(label=('Buscar'))
