from flask import Blueprint
from flask import render_template
from flask import request

from src.core import board


configuracion_blueprint = Blueprint("configuracion", __name__, url_prefix="/configuracion")

@configuracion_blueprint.get("/")
def configuracion_index():
    configuracion = board.list_configuracion()
    return render_template("configuracion.html", configuracion=configuracion)

@configuracion_blueprint.post("/")
def configuracion_update():
    kwargs = {
        "elementos_pagina": request.form.get("elementos_pagina"),
        "estado_pago": True if request.form.get("estado_pago") else False,
        "estado_info_contactos": True if request.form.get("estado_info_contactos") else False,
        "texto_recibo": request.form.get("texto_recibo"),
        "valor_base_cuota": request.form.get("valor_base_cuota"),
        "porcentaje_cuota": request.form.get("porcentaje_cuota"),
    }
    board.update_configuracion(**kwargs)
    configuracion = board.list_configuracion()
    return render_template("configuracion.html", configuracion=configuracion)
