from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from src.core.forms.pagos_form import EditForm
from src.core import board
from src.web.helpers.auth import login_required

pago_blueprint = Blueprint(
    "pagos", __name__, url_prefix="/pagos")


@pago_blueprint.get("/")
@login_required
def pagos_index():
    inscripciones = board.get_inscripciones()
    return render_template("pagos/pagos.html", inscripciones=inscripciones)


@pago_blueprint.get("/cuotas/<int:inscripcion_id>")
@login_required
def cuotas_index(inscripcion_id):
    cuotas = board.get_cuotas_by_inscripcion_id(inscripcion_id)
    form = EditForm(data={"items": cuotas})
    return render_template("pagos/cuotas.html", cuotas=cuotas, form=form)


@pago_blueprint.post("/pago")
@login_required
def pago():
    form = EditForm(request.form)
    if form.validate_on_submit():
        [board.pagar_cuota_by_id(cuota["id"])
         for cuota in form.items.data if cuota["check"]]
        flash("Pago realizado correctamente", "success")
    return redirect(url_for('pagos.pagos_index'))
