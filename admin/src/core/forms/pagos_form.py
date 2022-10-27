from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import DateTimeField, HiddenField, FieldList, FormField, BooleanField, DecimalField, SubmitField
from wtforms.validators import ValidationError, DataRequired, \
    Email, EqualTo, Length, NumberRange


class PagoForm(FlaskForm):
    id = HiddenField('id')
    fecha_vencimiento = DateTimeField(label=('Fecha Vencimiento'))
    valor_cuota = DecimalField(
        label=('Valor cuota'))
    estado_pago = BooleanField(label=('Estado de Pago'))
    check = BooleanField()


# class _SubForm(Form):
#     # The HiddenField later contains the id of the data record.
#     id = HiddenField('id')
#     excluded = SelectField('Exclude', choices=EXCLUDED_CHOICES, validators=[DataRequired()])

#     # The constructor is overwritten in order to bypass further fields for the csrf token.
#     def __init__(self, csrf_enabled=False, *args, **kwargs):
#         super(_SubForm, self).__init__(csrf_enabled=csrf_enabled, *args, **kwargs)


class EditForm(FlaskForm):
    items = FieldList(FormField(PagoForm))
    pagar = SubmitField(label=('Realizar Pago'))
