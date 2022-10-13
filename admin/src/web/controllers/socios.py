from flask import Blueprint
from flask import render_template
from flask import request

from src.core import board


socio_blueprint = Blueprint("socios", __name__, url_prefix="/socios")


@socio_blueprint.get("/")
def socio_index():
    socios = board.list_socios()
    return render_template("socios.html", socios=socios)


@socio_blueprint.get("/add")
def add_socio_view():
    return render_template("nuevoSocio.html")


@socio_blueprint.post("/")
def add_socio():
    kwargs = {
        "id_usuario": request.form.get("id_usuario"),
        "tipo_documento": request.form.get("tipo_documento"),
        "numero_documento": request.form.get("numero_documento"),
        "numero_socio": request.form.get("numero_socio"),
        "genero": request.form.get("genero"),
        "direccion": request.form.get("direccion"),
        "telefono": request.form.get("telefono"),
        "email": request.form.get("email"),
    }
    board.create_socio(**kwargs)
    socios = board.list_socios()
    return render_template("socios.html", socios=socios)
