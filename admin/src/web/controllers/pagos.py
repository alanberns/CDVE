from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import make_response
from flask import abort
from src.core.forms.pagos_form import EditForm, PagoSearchForm
from src.core import board
from src.web.helpers.auth import login_required
from src.web.helpers.permissions.user_permission import pago_index_req, pago_show_req
from datetime import datetime
import pdfkit

pago_blueprint = Blueprint(
    "pagos", __name__, url_prefix="/pagos")


@pago_blueprint.get("/")
@login_required
@pago_index_req
def pagos_index():
    form = PagoSearchForm()
    page = request.args.get('page', default=1, type=int)
    pagos = board.list_pagos(page)
    return render_template("pagos/pagos.html", pagos=pagos, form=form)


@pago_blueprint.post("/")
@login_required
@pago_index_req
def pagos_busqueda_index():
    form = PagoSearchForm()
    if not form.validate:
        abort(500)
    page = request.args.get('page', default=1, type=int)
    filter = form.select_busqueda.data
    texto_busqueda = form.texto_busqueda.data
    pagos = board.get_pagos_search_paginated(page, filter, texto_busqueda)
    return render_template("pagos/pagos.html", pagos=pagos, form=form)


@pago_blueprint.get("/inscripciones")
@login_required
@pago_index_req
def inscripciones_index():
    page = request.args.get('page', default=1, type=int)
    inscripciones = board.get_inscripciones(page)
    return render_template("pagos/inscripciones.html", inscripciones=inscripciones)


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
    config = board.list_configuracion()  # para calcular el porcentaje por mora
    return render_template("pagos/pago.html", cuotas=cuotas, cuota_ids=cuota_ids)


@pago_blueprint.get("/recibos")
@login_required
@pago_index_req
def recibo():
    pago_id = request.args.get('pago_id', type=int)
    pago = board.get_pago_by_id(pago_id)
    config = board.list_configuracion()
    rendered = render_template(
        "pagos/comprobante_template.html", pago=pago, config=config)
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=comprobante.pdf'
    return response


@pago_blueprint.get("/confirm")
@login_required
@pago_index_req
def confirm_pago():
    cuota_ids = request.args.to_dict(flat=False)["cuotas"]
    if not cuota_ids:
        flash("Hubo un error al registrar el pago", "danger")
        return redirect(url_for('pagos.pagos_index'))
    board.generate_payment(cuota_ids)
    flash("El pago se realizo de manera satisfactoria", "success")
    return redirect(url_for('pagos.pagos_index'))
