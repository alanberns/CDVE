from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, \
    Email, EqualTo, Length, NumberRange


class InscripcionForm(FlaskForm):
    pass
