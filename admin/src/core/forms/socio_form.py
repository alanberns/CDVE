from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired()])

    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )

    submit = SubmitField("Login")


class SocioForm(FlaskForm):
    tipo_documento = SelectField(
        "Tipo de Documento",
        choices=(("", "--Seleccionar--"), ("DNI", "DNI"), ("LE", "LE"), ("LC", "LC")), coerce=str, validators=[DataRequired()])
    numero_documento = StringField("Número", validators=[DataRequired()])
    genero = SelectField(
        "Género",
        choices=(("", "--Seleccionar--"), ("Femenino", "Femenino"), ("Masculino", "Masculino"), ("Otro", "Otro")), coerce=str, validators=[DataRequired()])
    direccion = StringField("Dirección", validators=[DataRequired()])
    telefono = StringField("Teléfono", validators=[DataRequired()])
    submit = SubmitField("Guardar")


class DocumentoForm(FlaskForm):
    apellido = StringField("Apellido")
    habilitado = SelectField(
            "Mostrar",
            choices=((0, "Todos"), (1, "Activos"), (2, "Inactivos")), coerce=int)
    submit = SubmitField("Buscar")