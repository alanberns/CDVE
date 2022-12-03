import string
from flask import Blueprint
from flask import render_template
from flask import request
from src.core import board
from src.web.helpers.auth import login_required
from src.web.helpers.permissions.user_permission import pago_index_req, pago_show_req

inscripciones_blueprint = Blueprint("inscripciones", __name__,
                                    url_prefix="/inscripciones")


@inscripciones_blueprint.get("/")
@login_required
@pago_index_req
def inscripciones_index():
    """
    Controlador del index de inscripciones, muestra el listado de inscripciones para disciplinas activas
    y las devuelve en forma paginada.
    """
    page = request.args.get("page", default=1, type=int)
    inscripciones = board.get_inscripciones(page)
    return render_template("inscripciones/inscripciones.html", inscripciones=inscripciones)
