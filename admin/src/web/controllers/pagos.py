from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash

from src.core import board
from src.web.helpers.auth import login_required

pago_blueprint = Blueprint(
    "pagos", __name__, url_prefix="/pagos")


@pago_blueprint.get("/")
@login_required
def pagos_index():

    inscripciones = board.get_inscripciones()
    return render_template("pagos/pagos.html", inscripciones=inscripciones)
