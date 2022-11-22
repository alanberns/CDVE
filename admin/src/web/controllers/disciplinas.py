from flask import Blueprint
from flask import render_template
from pathlib import Path
from flask import redirect
from flask import url_for
from flask import flash
from flask import request
from flask import make_response

from src.core.forms.disciplinas_form import DisciplinaNewForm
from src.core.board import disciplina
from src.core import board
from src.core.board.disciplina import Disciplina
import pdfkit
#from src.web.helpers.auth import login_required
#from src.core.database import db



disciplina_blueprint = Blueprint("disciplinas", __name__, url_prefix="/disciplinas")

#Paginacion del listado de Disciplinas 
@disciplina_blueprint.get ("/")
#@login_required
def disciplina_index():
   elem_pagina = board.get_elementos_pagina()
   page = int(request.args.get('page', 1))
   disciplinas_pag = board.list_disciplinas(page, elem_pagina)
   return render_template('/disciplinas/disciplinas.html', disciplinas_pag= disciplinas_pag)

#Creacion de una nueva disciplina
@disciplina_blueprint.post("/")
#@login_required
def newdcp():
   form = DisciplinaNewForm(request.form)
   if not form.validate:
      flash("No se puede hacer el ingreso de nueva disciplina")
   else:
       disciplina = board.create_disciplina(
       nombre= form.nombre.data,
       categoria= form.categoria.data,
       entrenador= form.entrenador.data,
       dia = form.dia.data,
       hora = form.hora.data,
       costo_mensual = form.costo_mensual.data,
       estado = True,
      )
   flash ("Se agrego una nueva Disciplina", "success")
   return redirect(url_for('disciplinas.disciplina_index', id=disciplina.id))
  
       
   
# Actualiza la informacion de una Disciplina
@disciplina_blueprint.get("/editdiscip/<int:id>")
#@login_required
def edit_discip(id):
   disciplina = board.get_disciplina(id)
   return render_template('/disciplinas/editDisciplina.html', disciplina=disciplina)


@disciplina_blueprint.post("/")
#@login_required
def updatedsp(id):
   form = DisciplinaNewForm(request.form)
   if not form.validate:
      flash("No se puede actualizar la  disciplina")
   else:
      kwargs = {
           "id": Disciplina.id,
           "nombre": form.nombre.data,
           "categoria": form.categoria.data,
           "entranador": form.entrenador.data,
           "dia": form.dia.data,
           "hora": form.hora.data,
           "costo_mensual": form.costo_mensual.data,
       }
      board.update_disciplina(id, **kwargs)
      return redirect(url_for('disciplinas.disciplina_index', id=disciplina.id))


# Modifica el estado Activo o Inactivo de una disciplina
@disciplina_blueprint.get("/modifyState/<int:id>")
#@login_required
def modify_state(id):
   board.update_estado_disciplina(id)
   flash ("Se cambio de Estado la Disciplina", "success")
   return redirect(url_for('disciplinas.disciplina_index', id=id))
   

# Retorna la lista de todas las disciplinas
@classmethod
#@login_required
def get_disciplinas():
    disciplinas = Disciplina.list_disciplinas()
    for row in disciplinas:
      disciplina=Disciplina(row[1], row[2], row[3])
      disciplinas.append(disciplina)
    return disciplinas


#Exportacion a PDF del listado de Disciplinas
@disciplina_blueprint.get("/")
#@login_required
def export_discip():
   disciplina_pag = board.listAll_disciplinas()
   rendered = render_template("/disciplinas/exportDisciplina.html",disciplina_pag = disciplina_pag)
   pdf = pdfkit.from_string(rendered,False)
   response = make_response(pdf)
   response.headers['Content-Type'] = 'application/pdf'
   response.headers['Content-Disposition'] = 'attachment; filename=Reporte_Disciplinas.pdf'
   return response



