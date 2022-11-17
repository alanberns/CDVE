from flask import Blueprint
from flask import render_template
from flask import request, redirect, url_for, flash, send_file
from flask import make_response
from src.core.forms.socio_form import SocioForm, DocumentoForm
from src.web.helpers.auth import login_required
from src.core import board
import pdfkit
import csv
import os

from src.web.helpers.permissions.user_permission import (
    socio_create_req,
    socio_index_req,
    socio_delete_req,
    socio_update_req,
    socio_show_req,
)

socio_blueprint = Blueprint("socios", __name__, url_prefix="/socios")


@socio_blueprint.route("/", methods=["get", "post"])
@login_required
@socio_index_req
def socios_index():
    """
    Página principal de socios. Lista, filtrado y exportado de socios.
    """
    form = DocumentoForm()
    configuracion = board.list_configuracion()
    elementos_pagina = configuracion.elementos_pagina
    page = int(request.args.get("page", 1))
    if form.validate_on_submit():
        apellido = form.apellido.data
        habilitado = form.habilitado.data
        if habilitado == 0:
            if apellido:
                socios_pag = board.find_socio_by_apellido(
                    apellido, page, elementos_pagina
                )
            else:
                socios_pag = board.list_socios_join_users(page, elementos_pagina)
        else:
            if habilitado == 1:
                activo = True
            else:
                activo = False
            if apellido:
                socios_pag = board.find_socio_habilitado_by_apellido(
                    apellido, activo, page, elementos_pagina
                )
            else:
                socios_pag = board.list_socios_habilitado(
                    activo, page, elementos_pagina
                )
        if form.exportpdf.data:
            rendered = render_template(
                "socios/socios_export.html", socios_pag=socios_pag
            )
            pdf = pdfkit.from_string(rendered, False)
            response = make_response(pdf)
            response.headers["Content-Type"] = "application/pdf"
            response.headers[
                "Content-Disposition"
            ] = "attachment; filename=listado_socios.pdf"
            return response
        if form.exportcsv.data:
            with open('src/web/templates/socios/socios.csv', 'w', newline='') as csvfile:
                fieldnames = ['Apellido', 'Nombre', 'Documento', 'Genero', 'Email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for socio in socios_pag.items:
                    writer.writerow({'Apellido':socio[1].last_name,'Nombre':socio[1].first_name, 'Documento':socio[0].numero_documento, 'Genero':socio[0].genero, 'Email':socio[1].email})
                csv_dir  = "templates/socios"
                csv_file = "socios.csv"
                csv_path = os.path.join(csv_dir, csv_file)
            return send_file(csv_path, as_attachment=True)
    else:
        socios_pag = board.list_socios_join_users(page, elementos_pagina)
    return render_template("socios/socios.html", socios_pag=socios_pag, form=form)


@socio_blueprint.route("/<int:socio_id>/delete", methods=["get", "post"])
@login_required
@socio_delete_req
def soft_delete_socio(socio_id):
    """
    Eliminado lógico.
    """
    board.soft_delete_socio(socio_id)
    return redirect(url_for("socios.socios_index"))


@socio_blueprint.route("/<int:usuario_id>/add", methods=["get", "post"])
@login_required
@socio_create_req
def add_socio(usuario_id):
    """
    Agregado de un socio dado un id de Usuario.
    """
    form = SocioForm()
    if form.validate_on_submit():
        if board.exist_socio_documento(form.numero_documento.data):
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
@socio_update_req
def update_socio(socio_id):
    """
    Edición de un socio cargando su información en un formulario.
    """
    socio = board.find_socio_by_id(socio_id)
    form = SocioForm()
    if form.validate_on_submit():
        if board.exist_socio_documento_id(form.numero_documento.data, socio_id):
            kwargs = {
                "id_usuario": socio.id_usuario,
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
@socio_update_req
def switch_state_socio(socio_id):
    """
    Cambio de estado de un socio, habilitado o deshabilitado.
    """
    board.switch_state_socio(socio_id)
    return redirect(url_for("socios.socios_index"))


@socio_blueprint.route("/<int:socio_id>/", methods=["get", "post"])
@login_required
@socio_show_req
def ver_socio(socio_id):
    """
    Muestra la información de un socio y las posibles operaciones.
    """
    form = SocioForm()
    query = board.find_socio_join_usuario_by_id(socio_id)
    socio = query[0]
    usuario = query[1]
    return render_template("socios/socio.html", socio=socio, usuario=usuario, form=form)


@socio_blueprint.route("/<int:socio_id>/inscribir", methods=["get", "post"])
@login_required
@socio_update_req
def inscribir_socio(socio_id):
    """
    Muestra las disciplinas disponibles para inscribir a un socio.
    """

    disciplinas = board.list_disciplinas_not_socio(socio_id)
    return render_template(
        "socios/inscribir.html", socio_id=socio_id, disciplinas=disciplinas
    )


@socio_blueprint.route(
    "/<int:socio_id>/inscribir/<int:disciplina_id>", methods=["get", "post"]
)
@login_required
@socio_update_req
def inscribir_socio_disciplina(socio_id, disciplina_id):
    """
    Inscripción de un socio a una disciplina.
    """

    socio = board.find_socio_by_id(socio_id)
    disciplina = board.find_disciplina_by_id(disciplina_id)
    board.socio_assign_disciplina(socio, disciplina)
    board.create_cuotas_by_inscripcion(socio, disciplina)
    return redirect(url_for("socios.ver_socio", socio_id=socio_id))
