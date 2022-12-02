import string
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

pago_blueprint = Blueprint("pagos", __name__, url_prefix="/pagos")


@pago_blueprint.get("/")
@login_required
@pago_index_req
def pagos_index():
    """
    Controlador del index de pagos, devuelve los pagos de forma paginada, por defecto la pagina es 1.
    Ademas setea el filtro, que por defecto esta en 0.
    filtro 0  se filtra por nro_socio, filtro 1 se filtra por apellido.
    """
    form = PagoSearchForm()
    page = request.args.get("page", default=1, type=int)
    filter = request.args.get("filter", default=0, type=int)
    error = request.args.get("error", type=int)
    form.select_busqueda.data = filter
    pagos = board.list_pagos(page)
    return render_template("pagos/pagos.html", pagos=pagos, form=form, error=error)


@pago_blueprint.post("/searching")
@login_required
@pago_index_req
def pagos_searching():
    """
    Ruta intermedia, su unica funcion es validar los datos del formulario de busqueda,
    y luego le pasa los parametros a la vista de busqueda para que maneje los datos
    por GET.
    """
    form = PagoSearchForm(request.form)
    if not form.validate:
        abort(400)
    page = request.args.get("page", default=1, type=int)
    filtro = form.select_busqueda.data
    busqueda = form.texto_busqueda.data
    if filtro == 0:  # Caso en que se ingreso alguna letra para buscar por nro_socio
        try:
            int(busqueda)
        except ValueError:
            return redirect(url_for("pagos.pagos_index", filtro=filtro, error=1))
    return redirect(
        url_for("pagos.pagos_search", page=page,
                filtro=filtro, busqueda=busqueda)
    )


@pago_blueprint.get("/search")
@login_required
@pago_index_req
def pagos_search():
    """
    Controlador de la busqueda de pagos, recibe el filtro, la pagina(por defecto 1) y el texto buscado
    y los setea, antes de devolver el template, paginado y filtrado segun corresponda.
    filtro 0  se filtra por nro_socio, filtro 1 se filtra por apellido.
    """
    page = request.args.get("page", default=1, type=int)
    filtro = request.args.get("filtro", type=int)
    busqueda = request.args.get("busqueda", type=str)
    pagos = board.get_pagos_search_paginated(page, filtro, busqueda)
    return render_template(
        "pagos/search.html", pagos=pagos, filtro=filtro, busqueda=busqueda
    )


@pago_blueprint.post("/")
@login_required
@pago_index_req
def pagos_busqueda_index():
    """
    Controlador para el index de pagos, en caso de que se haya realizado una busqueda.
    Valida el formulario y setea la pagina, el texto, y el filtro.
    Devuelve los resultados paginados
    """
    form = PagoSearchForm()
    if not form.validate:
        abort(400)
    page = request.args.get("page", default=1, type=int)
    filter = form.select_busqueda.data
    texto_busqueda = form.texto_busqueda.data
    pagos = board.get_pagos_search_paginated(page, filter, texto_busqueda)
    return render_template("pagos/pagos.html", pagos=pagos, form=form)


@pago_blueprint.get("/inscripciones")
@login_required
@pago_index_req
def inscripciones_index():
    """
    Controlador del index de inscripciones, muestra el listado de inscripciones para disciplinas activas
    y las devuelve en forma paginada.
    """
    page = request.args.get("page", default=1, type=int)
    inscripciones = board.get_inscripciones(page)
    return render_template("pagos/inscripciones.html", inscripciones=inscripciones)


@pago_blueprint.get("/cuotas/<int:inscripcion_id>")
@login_required
@pago_show_req
def cuotas_index(inscripcion_id):
    """
    Controlador del index de cuotas, recibe por url la id de una inscripcion de una disciplina valida
    y devuelve el listado de cuotas paginadas.
    """
    board.set_nro_cuota_by_inscripcion(inscripcion_id)
    cuotas = board.get_cuotas_by_inscripcion_id(inscripcion_id)
    form = EditForm(data={"items": cuotas})
    return render_template("pagos/cuotas.html", cuotas=cuotas, form=form)


@pago_blueprint.post("/pago")
@login_required
def pago():
    """
    Controlador de la accion de pagar. Recibe un formulario con una o multiples cuotas, una vez
    validado muestra el monto, la fecha y el numero de la cuota, ademas del total a a pagar.
    """
    form = EditForm(request.form)
    if not form.validate_on_submit():
        flash("Hubo un error al seleccionar las cuotas", "danger")
        return redirect(url_for("pagos.pagos_index"))
    cuota_ids = [cuota["id"] for cuota in form.items.data if cuota["check"]]
    cuotas = board.get_cuotas_by_ids(cuota_ids)
    config = board.list_configuracion()  # para calcular el porcentaje por mora
    return render_template("pagos/pago.html", cuotas=cuotas, cuota_ids=cuota_ids)


@pago_blueprint.get("/recibos")
@login_required
@pago_index_req
def recibo():
    """
    Controlador del comprobante de pago, recibe la id de un pago, si se valida, devuelve un pdf
    con un resumen de las cuotas pagadas, el monto y datos del usuario.
    """
    pago_id = request.args.get("pago_id", type=int)
    if not pago_id:
        abort(400)
    pago = board.get_pago_by_id(pago_id)
    config = board.list_configuracion()
    rendered = render_template(
        "pagos/comprobante_template.html", pago=pago, config=config
    )
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=comprobante.pdf"
    return response


@pago_blueprint.get("/confirm")
@login_required
@pago_index_req
def confirm_pago():
    """
    Controlador que valida que el pago se haya realizado correctamente. Si fue exitoso
    devuelve el mensaje de que el pago se realizo correctamente, si falla envia mensaje de error.
    En ambos casos se redirige al index de pagos.
    """
    args_dict = request.args.to_dict(flat=False)
    if not request.args.to_dict(flat=False):
        abort(400)
    cuota_ids = args_dict["cuotas"]
    if not cuota_ids:
        flash("Hubo un error al registrar el pago", "danger")
        return redirect(url_for("pagos.pagos_index"))
    board.generate_payment(cuota_ids)
    flash("El pago se realizo de manera satisfactoria", "success")
    return redirect(url_for("pagos.pagos_index"))
