from flask import Blueprint
from flask import render_template
from pathlib import Path
from flask import redirect
from flask import url_for
from flask import flash
from flask import request
from flask import make_response
from flask import jsonify
from src.core.forms.disciplinas_form import DisciplinaForm
from src.core.board import disciplina
from src.core import board
from src.core.board.disciplina import Disciplina
import pdfkit
from src.web.helpers.auth import login_required
from src.core.database import db
from src.web.helpers.permissions.user_permission import (
    disciplina_create_req,
    disciplina_index_req,
    disciplina_delete_req,
    disciplina_update_req,
    disciplina_show_req,
)


disciplina_blueprint = Blueprint(
    "disciplinas", __name__, url_prefix="/disciplinas")

# Paginacion del listado de Disciplinas


@disciplina_blueprint.get("/")
@login_required
@disciplina_show_req
def disciplina_index():
    elem_pagina = board.get_elementos_pagina()
    page = int(request.args.get('page', 1))
    disciplinas_pag = board.list_disciplinas_paginadas(page, elem_pagina)
    return render_template('disciplinas/disciplinas.html', disciplinas_pag=disciplinas_pag)

# Creacion de una nueva disciplina


@disciplina_blueprint.post("/")
@login_required
@disciplina_create_req
def newdcp():
    form = DisciplinaForm(request.form)
    checkDiscipline = board.find_same_discipline(
        form.nombre.data, form.categoria.data, form.entrenador.data,  form.dia.data, form.hora.data)
    if not form.validate:
        flash("No se puede hacer el ingreso de nueva disciplina")
    if (not checkDiscipline):
        disciplina = board.create_disciplina(
            nombre=form.nombre.data,
            categoria=form.categoria.data,
            entrenador=form.entrenador.data,
            dia=form.dia.data,
            hora=form.hora.data,
            costo_mensual=form.costo_mensual.data,
            estado=True,
        )
        flash("Se creo una nueva Disciplina", "success")
        return redirect(url_for('disciplinas.disciplina_index', id=disciplina.id))
    flash("Error: Disciplina Existente")
    return redirect(url_for('disciplinas.disciplina_index'))


# Actualiza la informacion de una Disciplina
@disciplina_blueprint.get("/editdiscip/<int:id>")
@login_required
@disciplina_update_req
def edit_discip(id):
    disciplina = board.get_disciplina(id)
    return render_template("disciplinas/editDisciplina.html", disciplina=disciplina)


# Crea una nueva Disciplina
@disciplina_blueprint.get("/inscribirDisciplina")
@login_required
def inscribir_Disciplina():
    return render_template('disciplinas/inscribirDisciplina.html')


# Actualiza la informacion de una Disciplina
@disciplina_blueprint.post("/update/<int:id>")
@login_required
@disciplina_update_req
def update_disciplina(id):
    disciplina = board.get_disciplina(id)
    form = DisciplinaForm()
    checkDiscipline = board.find_same_discipline(
        form.nombre.data, form.categoria.data, form.entrenador.data,  form.dia.data, form.hora.data)
    if not form.validate:
        flash("No se puede hacer el ingreso de nueva disciplina")
    if (not checkDiscipline):
        kwargs = {
            "id": id,
            "nombre": disciplina.nombre,
            "categoria": disciplina.categoria,
            "entrenador": form.entrenador.data,
            "dia": form.dia.data,
            "hora": form.hora.data,
            "costo_mensual": form.costo_mensual.data,
            "estado": disciplina.estado,
        }
        board.updatedisciplina(id, kwargs)
        flash("Se actualizo la informacion de Disciplina", "success")
        return redirect(url_for('disciplinas.disciplina_index', id=id))


# Modifica el estado Activo o Inactivo de una disciplina
@disciplina_blueprint.get("/modifyState/<int:id>")
@login_required
@disciplina_update_req
def modify_state(id):
    board.update_estado_disciplina(id)
    flash("Se cambio de Estado la Disciplina", "success")
    return redirect(url_for("disciplinas.disciplina_index", id=id))


# Retorna la lista de todas las disciplinas
@classmethod
@login_required
@disciplina_show_req
def get_disciplinas():
    disciplinas = Disciplina.list_disciplinas()
    for row in disciplinas:
        disciplina = Disciplina(row[1], row[2], row[3])
        disciplinas.append(disciplina)
    return disciplinas


# Exportacion a PDF del listado de Disciplinas
@disciplina_blueprint.get("/")
@login_required
@disciplina_show_req
def export_discip():
    disciplina_pag = board.listAll_disciplinas()
    rendered = render_template(
        "disciplinas/exportDisciplina.html", disciplina_pag=disciplina_pag
    )
    pdf = pdfkit.from_string(rendered, False)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers[
        "Content-Disposition"
    ] = "attachment; filename=Reporte_Disciplinas.pdf"
    flash("Se exporto el achivo con exito")
    return response
