from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, IntegerField
from wtforms.validators import ValidationError, DataRequired, \
    Email, Length, NumberRange


class UsuarioNuevoForm(FlaskForm):
    email = EmailField(label=('Email'), validators=[DataRequired()])
    username = StringField(
        label=('Nombre de usuario'),
        validators=[DataRequired(),
                    Length(min=3,max=255)])
    password = PasswordField(
        label=('Contraseña'),
        validators=[DataRequired(),
                    Length(min=5, max=50)])
    first_name = StringField(
        label=('Nombre'),
        validators=[DataRequired(),
                    Length(min=3,max=255)])
    last_name = StringField(
        label=('Apellido'),
        validators=[DataRequired(),
                    Length(min=3,max=255)])
    enviar = SubmitField(label=('Enviar'))

    """
    Validacion personalizada
    def validate_username(self, username):
        valid_chars = " qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMÁÉÚÍÓáéíóú"
        for char in username.data:
            if char not in valid_chars:
                raise ValidationError(
                    f"Character {char} is not allowed in username.")
    """


class ModificarUsuarioForm(FlaskForm):
    email = EmailField(label=('Email'), validators=[DataRequired()])
    username = StringField(
        label=('Nombre de usuario'),
        validators=[DataRequired(),
                    Length(min=3,max=255)])
    first_name = StringField(
        label=('Nombre'),
        validators=[DataRequired(),
                    Length(min=3,max=255)])
    last_name = StringField(
        label=('Apellido'),
        validators=[DataRequired(),
                    Length(min=3,max=255)])
    modificar = SubmitField(label=('Modificar'))

    def set_from_usuarios(self, usuario):
        self.email.data = usuario.email
        self.username.data = usuario.username
        self.first_name.data = usuario.first_name
        self.last_name.data = usuario.last_name
