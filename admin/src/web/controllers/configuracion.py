from flask import Blueprint
from flask import render_template
from flask import request

from src.core import board


configuracion_blueprint = Blueprint("configuracion", __name__, url_prefix="/configuracion")

@configuracion_blueprint.get("/")
def configuracion_index():
    configuracion = board.list_configuracion()
    return render_template("configuracion.html", configuracion=configuracion)
