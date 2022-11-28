from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length, NumberRange


class DisciplinaNewForm(FlaskForm):
    nombre = StringField(
        label=("nombre"), validators=[DataRequired(), Length(min=4, max=255)]
    )
    categoria = StringField(
        label=("categoria"), validators=[DataRequired(), Length(min=4, max=255)]
    )
    entrenador = StringField(
        label=("entrenador"), validators=[DataRequired(), Length(min=4, max=255)]
    )
    dia = StringField(
        label=("dia"), validators=[DataRequired(), Length(min=5, max=255)]
    )
    hora = StringField(
        label=("hora"), validators=[DataRequired(), Length(min=4, max=255)]
    )
    costo_mensual = IntegerField(
        label=("costo_mensual"),
        validators=[DataRequired(), NumberRange(min=1, max=500000)],
    )


def set_from_disciplinas(self, disciplina):
    self.nombre.data = disciplina.nombre
    self.categoria.data = disciplina.categoria
    self.entrenador.data = disciplina.entrenador
    self.dia.data = disciplina.dia
    self.hora.data = disciplina.hora
    self.costo_mensual.data = disciplina.costo_mensual
