from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired


class AuthForm(FlaskForm):
    email = EmailField(label=('Email'), validators=[DataRequired()])
    contraseña = PasswordField(
        label=('Contraseña'), validators=[DataRequired()])
    submit = SubmitField(label=('Ingresar'))
