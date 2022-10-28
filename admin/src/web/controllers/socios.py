from flask import Blueprint
from flask import render_template
from flask import request, redirect, url_for, flash
from src.core.forms.socio_form import SocioForm, DocumentoForm
from src.web.helpers.auth import login_required
from src.core import board


socio_blueprint = Blueprint("socios", __name__, url_prefix="/socios")


@socio_blueprint.route("/", methods=["get", "post"])
@login_required
def socios_index():
    """
    Página principal de socios. Lista y filtrado de socios.
    """
    form = DocumentoForm()
    configuracion = board.list_configuracion()
    elementos_pagina = configuracion.elementos_pagina
    page = int(request.args.get('page', 1))
    if form.validate_on_submit():
        apellido = form.apellido.data
        habilitado = form.habilitado.data
        if habilitado == 0:
            if apellido:
                socios_pag = board.find_socio_by_apellido(
                    apellido, page, elementos_pagina)
            else:
                socios_pag = board.list_socios_join_users(
                    page, elementos_pagina)
        else:
            if habilitado == 1:
                activo = True
            else:
                activo = False
            if apellido:
                socios_pag = board.find_socio_habilitado_by_apellido(
                    apellido, activo, page, elementos_pagina)
            else:
                socios_pag = board.list_socios_habilitado(
                    activo, page, elementos_pagina)
    else:
        socios_pag = board.list_socios_join_users(page, elementos_pagina)
    return render_template("socios/socios.html", socios_pag=socios_pag, form=form)


@socio_blueprint.route("/<int:socio_id>/delete", methods=["get", "post"])
@login_required
def soft_delete_socio(socio_id):
    """
    Eliminado lógico.
    """
    board.soft_delete_socio(socio_id)
    return redirect(url_for("socios.socios_index"))


@socio_blueprint.route("/<int:usuario_id>/add", methods=["get", "post"])
@login_required
def add_socio(usuario_id):
    """
    Agregado de un socio dado un id de Usuario.
    """
    form = SocioForm()
    if form.validate_on_submit():
        if (board.exist_socio_documento(form.numero_documento.data)):
            kwargs = {
                "id_usuario": usuario_id,
                "tipo_documento": form.tipo_documento.data,
                "numero_documento": form.numero_documento.data,
                "genero": form.genero.data,
                "direccion": form.direccion.data,
                "telefono": form.telefono.data,
            }
            board.create_socio(**kwargs)
            return redirect(url_for("usuarios.view_usuario", id=usuario_id))
        else:
            flash("El documento ingresado pertenece a otro Socio", "danger")
    return render_template("socios/create_socio.html", form=form, title="Crear Socio")


@socio_blueprint.route("/<int:socio_id>/update", methods=["get", "post"])
@login_required
def update_socio(socio_id):
    """
    Edición de un socio cargando su información en un formulario.
    """
    socio = board.find_socio_by_id(socio_id)
    form = SocioForm()
    if form.validate_on_submit():
        if (board.exist_socio_documento_id(form.numero_documento.data, socio_id)):
            kwargs = {
                "id_usuario": 2,
                "tipo_documento": form.tipo_documento.data,
                "numero_documento": form.numero_documento.data,
                "genero": form.genero.data,
                "direccion": form.direccion.data,
                "telefono": form.telefono.data,
            }
            board.update_socio(socio_id, **kwargs)
            return redirect(url_for("socios.socios_index"))
        else:
            flash("El documento ingresado pertenece a otro Socio", "danger")
    else:
        form.direccion.data = socio.direccion
        form.genero.data = socio.genero
        form.numero_documento.data = socio.numero_documento
        form.tipo_documento.data = socio.tipo_documento
        form.telefono.data = socio.telefono
    return render_template("socios/create_socio.html", form=form, title="Editar Socio")


@socio_blueprint.route("/<int:socio_id>/switch", methods=["get", "post"])
@login_required
def switch_state_socio(socio_id):
    """
    Cambio de estado de un socio, habilitado o deshabilitado.
    """
    board.switch_state_socio(socio_id)
    return redirect(url_for("socios.socios_index"))


@socio_blueprint.route("/<int:socio_id>/", methods=["get", "post"])
@login_required
def ver_socio(socio_id):
    """
    Muestra la información de un socio y las posibles operaciones.
    """
    form = SocioForm()
    query = board.find_socio_join_usuario_by_id(socio_id)
    socio = query[0]
    usuario = query[1]
    return render_template("socios/socio.html", socio=socio, usuario=usuario, form=form)
