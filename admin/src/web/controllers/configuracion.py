from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash

from src.core import board
from src.core.forms.configuration_form import ConfigurationForm
from src.web.helpers.auth import login_required
from src.web.helpers.permissions.user_permission import config_all_req

configuracion_blueprint = Blueprint(
    "configuracion", __name__, url_prefix="/configuracion"
)


@configuracion_blueprint.get("/")
@login_required
@config_all_req
def configuracion_index():
    configuracion = board.list_configuracion()
    form = ConfigurationForm(request.form)
    form.set_from_config(configuracion)
    return render_template("configuracion.html", form=form)


@configuracion_blueprint.post("/")
@login_required
@config_all_req
def configuracion_update():
    form = ConfigurationForm(request.form)
    if not form.validate:
        flash("La configuracion no se pudo editar", "danger")
        return render_template("configuracion.html", form=form)
    kwargs = {
        "elementos_pagina": form.elementos_pagina.data,
        "estado_pago": form.estado_pago.data,
        "estado_info_contactos": form.estado_info_contactos.data,
        "texto_recibo": form.texto_recibo.data,
        "valor_base_cuota": form.valor_base_cuota.data,
        "porcentaje_cuota": form.porcentaje_cuota.data,
    }
    config = board.list_configuracion()
    if config.valor_base_cuota != form.valor_base_cuota.data:
        board.update_valor_cuotas(form.valor_base_cuota.data)
    board.update_configuracion(**kwargs)
    configuracion = board.list_configuracion()
    form.set_from_config(configuracion)
    flash("La configuracion se actualizo correctamente", "success")
    return render_template("configuracion.html", form=form)
