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
    tipo_documento = StringField("Tipo Documento", validators=[DataRequired()])
    numero_documento = StringField("Numero", validators=[DataRequired()])
    numero_socio = StringField("numero_socio", validators=[DataRequired()])
    genero = StringField("genero", validators=[DataRequired()])
    direccion = StringField("direccion", validators=[DataRequired()])
    telefono = StringField("telefono", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    submit = SubmitField("Guardar")


class DocumentoForm(FlaskForm):
    apellido = StringField("Apellido")
    habilitado = SelectField(
            "Mostrar",
            choices=((0, "Todos"), (1, "Activos"), (2, "Inactivos")), coerce=int)
    submit = SubmitField("Buscar")