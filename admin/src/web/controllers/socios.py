from flask import Blueprint
from flask import render_template
from flask import request, redirect, url_for, flash
from flask import make_response
from src.core.forms.socio_form import (
    SocioForm,
    DocumentoForm,
    CarnetUpload,
    CarnetExport,
)
from src.web.helpers.auth import login_required
from src.web.helpers.uploads_path import getUploadsPath
from src.core import board
import pdfkit
import csv
import io
import os
from datetime import datetime
from qrcode import QRCode
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
    elementos_pagina = board.get_elementos_pagina()
    page = int(request.args.get("page", 1))
    if form.validate_on_submit():
        form = DocumentoForm(request.form)
        apellido = form.apellido.data
        habilitado = form.habilitado.data
        clear = True
        socios_pag = board.filter_socios(apellido, habilitado, page, elementos_pagina)

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
            output = io.StringIO()
            csvdata = ["Socio #", "Apellido", "Nombre", "Documento", "Genero", "Email", "Estado"]
            writer = csv.writer(output)
            writer.writerow(csvdata)
            for socio in socios_pag.items:
                if socio[0].habilitado:
                    estado="Habilitado"
                else:
                    estado="Deshabilitado"
                csvdata = [
                    socio[0].id,
                    socio[1].last_name,
                    socio[1].first_name,
                    f"{socio[0].tipo_documento} {socio[0].numero_documento}",
                    socio[0].genero,
                    socio[1].email,
                    estado,
                ]
                writer.writerow(csvdata)
            response = make_response(output.getvalue())
            response.headers["Content-Type"] = "application/csv"
            response.headers[
                "Content-Disposition"
            ] = "attachment; filename=listado_socios.csv"
            return response
    else:
        configuracion = board.list_configuracion()

        
        clear = False
        socios_pag = board.list_socios_join_users(page, elementos_pagina)
    return render_template("socios/socios.html", socios_pag=socios_pag, form=form, clear=clear)


@socio_blueprint.route("/<int:socio_id>/delete", methods=["get", "post"])
@login_required
@socio_delete_req
def soft_delete_socio(socio_id):
    """
    Eliminado lógico.
    """
    board.soft_delete_socio(socio_id)
    board.delete_carnet(socio_id)
    return redirect(url_for("socios.socios_index"))


@socio_blueprint.route("/<int:usuario_id>/add", methods=["get", "post"])
@login_required
@socio_create_req
def add_socio(usuario_id):
    """
    Agregado de un socio dado un id de Usuario.
    Se le asigna el rol de socio al usuario
    """
    form = SocioForm()
    if form.validate_on_submit():
        if board.exist_socio_documento(form.tipo_documento.data, form.numero_documento.data):
            kwargs = {
                "id_usuario": usuario_id,
                "tipo_documento": form.tipo_documento.data,
                "numero_documento": form.numero_documento.data,
                "genero": form.genero.data,
                "direccion": form.direccion.data,
                "telefono": form.telefono.data,
            }
            board.create_socio(**kwargs)

            # Asignar rol de socio
            roles = board.get_roles()
            for rol in roles:
                if rol.nombre == "Socio":
                    rol_socio = rol
                    board.asignar_rol(rol_socio.id, usuario_id)
                    flash(
                        "Se asignó el rol al usuario y se creo el perfil de socio",
                        "success",
                    )

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
    query = board.find_socio_join_usuario_by_id(socio_id)
    socio = query[0]
    usuario = query[1]
    form = SocioForm()
    if form.validate_on_submit():
        if board.exist_socio_documento_update(socio_id, form.tipo_documento.data, form.numero_documento.data):
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
    return render_template("socios/create_socio.html", form=form, editar=True, usuario=usuario)


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
    inscripciones = board.get_inscripcion_by_socio_id(socio_id)
    socio = query[0]
    usuario = query[1]
    return render_template("socios/socio.html", socio=socio, usuario=usuario, form=form, inscripciones=inscripciones)


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
    if socio.habilitado:
        disciplina = board.find_disciplina_by_id(disciplina_id)
        board.socio_assign_disciplina(socio, disciplina)
        board.create_cuotas_by_inscripcion(socio, disciplina)
        flash("El socio fue inscripto satisfactoriamente.", "success")
    else:
        flash("El socio no está habilitado.", "danger")
    return redirect(url_for("inscripciones.inscripciones_index"))


@socio_blueprint.route("/<int:socio_id>/ver_carnet", methods=["get", "post"])
@login_required
@socio_show_req
def ver_carnet(socio_id):
    socio = board.find_socio_by_id(socio_id)
    usuario = board.get_usuario(socio.id_usuario)

    socio_info = {
        "nombre": usuario.first_name,
        "apellido": usuario.last_name,
        "numero": socio.id,
        "numero_documento": socio.numero_documento,
        "tipo_documento": socio.tipo_documento,
        "fecha_alta": usuario.created_at,
        "estado": socio.habilitado,
    }
    carnet = board.get_carnet(socio_id)
    estado = not board.es_moroso(socio_id)
    form = CarnetExport()
    if request.method == "POST":
        rendered = render_template(
            "socios/carnet_export.html",
            socio=socio_info,
            imagen=carnet.url_imagen,
            qr=carnet.url_qr,
            estado=estado,
        )
        options = {"enable-local-file-access": None}
        pdf = pdfkit.from_string(rendered, False, options=options)
        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        response.headers[
            "Content-Disposition"
        ] = "attachment; filename=carnet_socio.pdf"
        return response
    temp = carnet.url_imagen.split("/")
    imagen = temp[len(temp) - 2] + "/" + temp[len(temp) - 1]
    temp = carnet.url_qr.split("/")
    qr = temp[len(temp) - 2] + "/" + temp[len(temp) - 1]
    return render_template(
        "socios/carnet.html",
        socio=socio_info,
        imagen=imagen,
        qr=qr,
        estado=estado,
        form=form,
    )


@socio_blueprint.route("/<int:socio_id>/carnet", methods=["POST", "GET"])
@login_required
@socio_create_req
def alta_carnet(socio_id):
    """
    Genera el carnet para un socio.
    """
    if not board.get_carnet(socio_id):
        form = CarnetUpload()
        if form.validate_on_submit():
            datenow = datetime.now()
            nameimg = getUploadsPath(f"{datenow}img.jpg")
            nameqr = getUploadsPath(f"{datenow}qr.jpg")
            form.image.data.save(nameimg)
            data = f"{request.host_url[:-1]}{url_for('socios.ver_carnet', socio_id=socio_id)}"
            qr = QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
            img.save(nameqr)
            kwargs = {
                "id_socio": socio_id,
                "url_imagen": nameimg,
                "url_qr": nameqr,
            }
            board.create_carnet(**kwargs)
            return redirect(url_for("socios.ver_carnet", socio_id=socio_id))
    else:
        return redirect(url_for("socios.socios_index"))
    socio = board.find_socio_by_id(socio_id)
    usuario = board.get_usuario(socio.id_usuario)
    return render_template(
        "socios/carnet_alta.html",
        form=form,
        apellido=usuario.last_name,
        nombre=usuario.first_name,
    )
