from flask import Blueprint
from flask import render_template
from flask import request, redirect, url_for, flash
from src.web.controllers.forms import SocioForm, DocumentoForm

from src.core import board


socio_blueprint = Blueprint("socios", __name__, url_prefix="/socios")


@socio_blueprint.route("/", methods=["get", "post"])
def socios_index():
    form = DocumentoForm()
    if form.validate_on_submit():
        apellido = form.apellido.data
        habilitado = form.habilitado.data
        if habilitado == 0:
            if apellido:
                socios = board.find_socio_by_apellido(apellido)
            else:
                socios = board.list_socios()
        else:
            if habilitado == 1: 
                activo = True
            else: 
                activo = False
            if apellido:
                socios = board.find_socio_habilitado_by_apellido(apellido, activo)
            else:
                socios = board.list_socios_habilitado(activo)
    else:
        socios = board.list_socios()
    return render_template("socios.html", socios=socios, form=form)


@socio_blueprint.route("/<int:socio_id>/delete", methods=["get", "post"])
def soft_delete_socio(socio_id):
    board.soft_delete_socio(socio_id)
    return redirect(url_for("socios.socios_index"))


@socio_blueprint.route("/add", methods=["get", "post"])
def add_socio():
    form = SocioForm()
    if form.validate_on_submit():
        kwargs = {
            "id_usuario": 1,
            "tipo_documento": form.tipo_documento.data,
            "numero_documento": form.numero_documento.data,
            "numero_socio": form.numero_socio.data,
            "genero": form.genero.data,
            "direccion": form.direccion.data,
            "telefono": form.telefono.data,
            "email": form.email.data,
        }
        board.create_socio(**kwargs)
        return redirect(url_for("socios.socios_index"))
    return render_template("create_socio.html", form=form)


@socio_blueprint.route("/<int:socio_id>/update", methods=["get", "post"])
def update_socio(socio_id):
    socio = board.find_socio_by_id(socio_id)
    form = SocioForm()
    if form.validate_on_submit():
        kwargs = {
            "id_usuario": 2,
            "tipo_documento": form.tipo_documento.data,
            "numero_documento": form.numero_documento.data,
            "numero_socio": form.numero_socio.data,
            "genero": form.genero.data,
            "direccion": form.direccion.data,
            "telefono": form.telefono.data,
            "email": form.email.data,
        }
        board.update_socio(socio_id, **kwargs)
        return redirect(url_for("socios.socios_index"))
    else:
        form.direccion.data = socio.direccion
        form.email.data = socio.email
        form.genero.data = socio.genero
        form.numero_documento.data = socio.numero_documento
        form.tipo_documento.data = socio.tipo_documento
        form.telefono.data = socio.telefono
        form.numero_socio.data = socio.numero_socio
    return render_template("create_socio.html", form=form)


@socio_blueprint.route("/<int:socio_id>/switch", methods=["get", "post"])
def switch_state_socio(socio_id):
    board.switch_state_socio(socio_id)
    return redirect(url_for("socios.socios_index"))


@socio_blueprint.route("/<int:socio_id>/", methods=["get", "post"])
def ver_socio(socio_id):
    socio = board.find_socio_by_id(socio_id)
    return render_template("socio.html", socio=socio)
