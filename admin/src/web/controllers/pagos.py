from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from src.core.forms.pagos_form import EditForm
from src.core import board
from src.web.helpers.auth import login_required
from src.web.helpers.permissions.user_permission import pago_index_req, pago_show_req
from datetime import datetime

pago_blueprint = Blueprint(
    "pagos", __name__, url_prefix="/pagos")


@pago_blueprint.get("/")
@login_required
@pago_index_req
def pagos_index():
    inscripciones_query = board.get_inscripciones()
    inscripciones = []
    for inscripcion in inscripciones_query:
        usuario = board.find_socio_join_usuario_by_id(inscripcion.socio_id)
        inscripciones.append([inscripcion, usuario[1]])
    return render_template("pagos/pagos.html", inscripciones=inscripciones)


@pago_blueprint.get("/cuotas/<int:inscripcion_id>")
@login_required
@pago_show_req
def cuotas_index(inscripcion_id):
    cuotas = board.get_cuotas_by_inscripcion_id(inscripcion_id)
    form = EditForm(data={"items": cuotas})
    return render_template("pagos/cuotas.html", cuotas=cuotas, form=form)


@pago_blueprint.post("/pago")
@login_required
def pago():
    form = EditForm(request.form)
    if form.validate_on_submit():
        cuota_ids = [cuota["id"]for cuota in form.items.data if cuota["check"]]
        board.pay_cuotas_by_ids(cuota_ids)
        flash("Pago realizado correctamente", "success")
    return redirect(url_for('pagos.pagos_index'))
