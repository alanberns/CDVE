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
    page = request.args.get('page', default=1, type=int)
    inscripciones = board.get_inscripciones(page)
    return render_template("pagos/pagos.html", inscripciones=inscripciones)


@pago_blueprint.get("/cuotas/<int:inscripcion_id>")
@login_required
@pago_show_req
def cuotas_index(inscripcion_id):
    board.set_nro_cuota_by_inscripcion(inscripcion_id)
    cuotas = board.get_cuotas_by_inscripcion_id(inscripcion_id)
    form = EditForm(data={"items": cuotas})
    return render_template("pagos/cuotas.html", cuotas=cuotas, form=form)


@pago_blueprint.post("/pago")
@login_required
def pago():
    form = EditForm(request.form)
    if not form.validate_on_submit():
        flash("Hubo un error al seleccionar las cuotas", "danger")
        return redirect(url_for('pagos.pagos_index'))
    cuota_ids = [cuota["id"]for cuota in form.items.data if cuota["check"]]
    cuotas = board.get_cuotas_by_ids(cuota_ids)
    config = board.list_configuracion()
    return render_template("pagos/pago.html", cuotas=cuotas)
