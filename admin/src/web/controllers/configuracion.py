from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash

from src.core import board
from src.core.forms.configuration_form import ConfigurationForm
from src.web.helpers.auth import login_required
from src.web.helpers.permissions.user_permission import config_all_req
from src.web.helpers.percentage import percentage_to_float
from src.web.helpers.percentage import float_to_percentage


configuracion_blueprint = Blueprint(
    "configuracion", __name__, url_prefix="/configuracion"
)


@configuracion_blueprint.get("/")
@login_required
@config_all_req
def configuracion_index():
    """
    Controlador del index de la configuracion, setea los datos de la configuracion dentro del formulario
    wtforms llamado ConfigurationForm
    """
    configuracion = board.list_configuracion()
    form = ConfigurationForm(request.form)
    form.set_from_config(configuracion)
    form.porcentaje_cuota.data = float_to_percentage(
        form.porcentaje_cuota.data)
    return render_template("configuracion.html", form=form)


@configuracion_blueprint.post("/")
@login_required
@config_all_req
def configuracion_update():
    """
    Controlador del index de configuracion, valida que los datos modificados del formulario
    ConfigurationForm sean correctos, y realiza el update de los datos correspondientes
    """
    form = ConfigurationForm(request.form)
    if not form.validate:
        flash("La configuracion no se pudo editar", "danger")
        return render_template("configuracion.html", form=form)
    kwargs = {
        "elementos_pagina": form.elementos_pagina.data,
        "estado_pago": form.estado_pago.data,
        "texto_recibo": form.texto_recibo.data,
        "valor_base_cuota": form.valor_base_cuota.data,
        "porcentaje_cuota": percentage_to_float(form.porcentaje_cuota.data),
        "email_club": form.email_club.data,
        "numero_club": form.numero_club.data,
    }
    config = board.list_configuracion()
    if config.valor_base_cuota != form.valor_base_cuota.data:
        board.update_valor_cuotas(form.valor_base_cuota.data)
    board.update_configuracion(**kwargs)
    configuracion = board.list_configuracion()
    form.set_from_config(configuracion)
    flash("La configuracion se actualizo correctamente", "success")
    return render_template("configuracion.html", form=form)
