from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField, FileField, IntegerField, widgets
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from flask_wtf.file import FileField, FileRequired


class SocioForm(FlaskForm):
    tipo_documento = SelectField(
        "Tipo de Documento",
        choices=(("", "--Seleccionar--"), ("DNI", "DNI"), ("LE", "LE"), ("LC", "LC")),
        coerce=str,
        validators=[DataRequired()],
    )
    numero_documento = IntegerField("Número", validators=[DataRequired(), NumberRange(max=999999999)])
    genero = SelectField(
        "Género",
        choices=(
            ("", "--Seleccionar--"),
            ("Femenino", "Femenino"),
            ("Masculino", "Masculino"),
            ("Otro", "Otro"),
        ),
        coerce=str,
        validators=[DataRequired()],
    )
    direccion = StringField("Dirección", validators=[DataRequired()])
    telefono = IntegerField("Teléfono", validators=[Optional(), NumberRange(max=999999999)])
    submit = SubmitField("Guardar")


class DocumentoForm(FlaskForm):
    apellido = StringField("Apellido")
    habilitado = SelectField(
        "Mostrar", choices=((0, "Todos"), (1, "Activos"), (2, "Inactivos")), coerce=int
    )
    submit = SubmitField(label="Buscar")
    exportpdf = SubmitField(label="Exportar pdf")
    exportcsv = SubmitField(label="Exportar csv")


class CarnetUpload(FlaskForm):
    image = FileField(validators=[FileRequired()])
    submit = SubmitField("Upload")


class CarnetExport(FlaskForm):
    submit = SubmitField("Export")
